# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from celery import task,shared_task
from decimal import Decimal
import json
import requests
from rest_framework.response import Response
from .models import TransactionResponse

import logging
logger = logging.getLogger(__name__)

@task
def send_create_b2c_transaction(request,access_token):
	"""
	Task to send create b2c transaction request
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
	headers = {"Authorization": "Bearer %s" % access_token}

	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)

@task
def send_create_b2b_transaction(request,access_token):
	"""
	Task to send create b2b transaction request asynchronously
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
	headers = {"Authorization": "Bearer %s" % access_token}

	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)

@task
def send_register_c_to_b_url(request,access_token):
	"""
	Task to send create ctob transaction request asynchronously
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
	headers = {"Authorization": "Bearer %s" % access_token}

	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)

@task
def send_check_account_balance(request,access_token):
	"""
	Task to check accoubt balance asynchronously
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
	headers = {"Authorization": "Bearer %s" % access_token}
	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)

@task
def send_check_transaction_status(request,access_token):
	"""
	Task to check transaction status asynchronously
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
	headers = {"Authorization": "Bearer %s" % access_token}
	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)

@task
def send_transaction_reversal(request,access_token):
	"""
	Task to send create transaction reversal request asynchronously
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
	headers = {"Authorization": "Bearer %s" % access_token}

	response = requests.post(api_url, json=request, headers=headers)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)


@task
def handle_lipa_na_mpesa_callback_task(request,transaction,auth_header):
	"""
		Process the initiate lipa na mpesa callback response
		:param response:
		:return:
		Accepted
		========
		{
		"Body":{
			"stkCallback":{
			"MerchantRequestID":"19465-780693-1",
			"CheckoutRequestID":"ws_CO_27072017154747416",
			"ResultCode":0,
			"ResultDesc":"The service request is processed successfully.",
			"CallbackMetadata":{
			"Item":[
			{
				"Name":"Amount",
				"Value":1
			},
			{
				"Name":"MpesaReceiptNumber",
				"Value":"LGR7OWQX0R"
			},
			{
				"Name":"Balance"
			},
			{
				"Name":"TransactionDate",
				"Value":20170727154800
			},
			{
				"Name":"PhoneNumber",
				"Value":254721566839
			}
			]
			}
			}
		}
		}
		Canceled
		=========
		{
		"Body":{
			"stkCallback":{
			"MerchantRequestID":"8555-67195-1",
			"CheckoutRequestID":"ws_CO_27072017151044001",
			"ResultCode":1032,
			"ResultDesc":"[STK_CB - ]Request cancelled by user"
			}
		}
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

	response = requests.post(api_url, json=request, headers=auth_header)
	
	response_data = response.json()
	# print(response.__dict__)

	if response.status_code ==200:
		merchant_request_id = response_data['MerchantRequestID']
		checkout_request_id = response_data['CheckoutRequestID']
		response_code = response_data['ResponseCode']
		response_description = response_data['ResponseDescription']
		customer_message = response_data['CustomerMessage']
		
		print( {
            "MerchantRequestID":merchant_request_id,
            "CheckoutRequestID":checkout_request_id,
            "ResponseCode":response_code ,
            "ResponseDescription":response_description,
            "CustomerMessage":customer_message
        })
		#Add is successfull boolean 
		TransactionResponse.objects.create(
		transaction=transaction,
		merchant_request_id=merchant_request_id,
		checkout_request_id=checkout_request_id,
		response_code=response_code)
	
	if response.status_code ==400:
		return response.errorCode
		
	



@task
def send_query_lipa_na_mpesa_online_status(request,auth_header):
	"""
	Task to check stk push transaction status
	"""
	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
	# headers = {"Authorization": "Bearer %s" % access_token}

	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
	# headers = {"Authorization": "Bearer %s" % access_token}
	response = requests.post(api_url, json=request, headers=auth_header)
	response_description = response['ResponseDescription']
	originator_conversation_id = response['OriginatorConversationID ']
	conversation_id = response['ConversationID']
	merchant_request_id = response['MerchantRequestID']
	checkout_request_id = response['CheckoutRequestID']
	response_code = response['ResponseCode']
	result_description = response['ResultDesc']
	result_code = response['ResultCode']
	# customer_message = response['CustomerMessage']

	TransactionResponse.objects.create(
	transaction_feedback=response_description,
	transaction=transaction,
	originator_conversation_id=originator_conversation_id,
	conversation_id=conversation_id,
	merchant_request_id=merchant_request_id,
	checkout_request_id=checkout_request_id,
	response_code=response_code,
	result_description=result_description,
	result_code=result_code)




# @shared_task(name='xelpayer.handle_online_checkout_callback')
# def handle_online_checkout_callback_task(response):
#     """
#     Process the callback response
#     :param response:
#     :return:
#      Accepted
#     ========
#     {
#       "Body":{
# 	"stkCallback":{
# 	  "MerchantRequestID":"19465-780693-1",
# 	  "CheckoutRequestID":"ws_CO_27072017154747416",
# 	  "ResultCode":0,
# 	  "ResultDesc":"The service request is processed successfully.",
# 	  "CallbackMetadata":{
# 	    "Item":[
# 	      {
# 		"Name":"Amount",
# 		"Value":1
# 	      },
# 	      {
# 		"Name":"MpesaReceiptNumber",
# 		"Value":"LGR7OWQX0R"
# 	      },
# 	      {
# 		"Name":"Balance"
# 	      },
# 	      {
# 		"Name":"TransactionDate",
# 		"Value":20170727154800
# 	      },
# 	      {
# 		"Name":"PhoneNumber",
# 		"Value":254721566839
# 	      }
# 	    ]
# 	  }
# 	}
#       }
#     }
#     Canceled
#     =========
#     {
#       "Body":{
# 	"stkCallback":{
# 	  "MerchantRequestID":"8555-67195-1",
# 	  "CheckoutRequestID":"ws_CO_27072017151044001",
# 	  "ResultCode":1032,
# 	  "ResultDesc":"[STK_CB - ]Request cancelled by user"
# 	}
#       }
#     """
#     try:
# 	data = response.get('Body', {}).get('stkCallback', {})
# 	update_data = dict()
# 	update_data['result_code'] = data.get('ResultCode', '')
# 	update_data['result_description'] = data.get('ResultDesc', '')
# 	update_data['checkout_request_id'] = data.get('CheckoutRequestID', '')
# 	update_data['merchant_request_id'] = data.get('MerchantRequestID', '')

# 	meta_data = data.get('CallbackMetadata', {}).get('Item', {})
# 	if len(meta_data) > 0:
# 	    # handle the meta data
# 	    for item in meta_data:
# 		if len(item.values()) > 1:
# 		    key, value = item.values()
# 		    if key == 'MpesaReceiptNumber':
# 			update_data['mpesa_receipt_number'] = value
# 		    if key == 'Amount':
# 			update_data['amount'] = Decimal(value)
# 		    if key == 'PhoneNumber':
# 			update_data['phone'] = int(value)
# 		    if key == 'TransactionDate':
# 			date = str(value)
# 			year, month, day, hour, min, sec = date[:4], date[4:-8], date[6:-6], date[8:-4], date[10:-2], date[12:]
# 			update_data['transaction_date'] = '{}-{}-{} {}:{}:{}'.format(year, month, day, hour, min, sec)

# 	# save
# 	OnlineCheckoutResponse.objects.create(**update_data)
# 	logger.info(dict(updated_data=update_data))
#     except Exception as ex:
# 	logger.error(ex)
# raise ValueError(str(ex))