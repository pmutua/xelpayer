# xelpayer
API Payment GateWay 


## Requirements

- Python >=3.5

## Installing Instructions

Follow the following steps:

1. Clone the project to your workspace

   `git clone https://github.com/xelphahealth/xelpayer.git`

2. Navigate to the cloned project

   `cd xelpayer`

3. In the project create a folder for the virtual environment and install python3.

   `mkdir env && virtualenv -p python3 env`

4. Activate environment

   `source env/bin/activate`

5. Install dependencies required to run the application.

   `pip install -r requirements.txt`

6. Before running the app make `manage.py` executable (Optional)

   `sudo chmod +x manage.py`

7. Run application

   `./manage.py runserver`

### Common Fixes

Updating Django - error: 'No module named migration'</p>

**syntax**
`pip install --upgrade --force-reinstall package`

`pip install --upgrade --force-reinstall Django==1.11`

## Postgres setup

Login as PostgreSQL Superuser postgres via psql Client

`sudo -u postgres psql`

### Instructions

```sql
CREATE DATABASE xelpayer;
CREATE USER aphya WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE xelpayer TO aphya;
```



# Lipa Na Mpesa Online Payment
Lipa na M-Pesa Online Payment API is used to initiate a M-Pesa transaction on behalf of a customer using STK Push. This is the same technique mySafaricom App uses whenever the app is used to make payments.

**Lipa na M-Pesa Online Payment - Resource URL**

POST https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest


# C2B API

This API enables Paybill and Buy Goods merchants to integrate to M-Pesa and receive real time payments notifications.

**C2B Register URL - Resource URL**

POST https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl


# B2B API

This API enables Business to Business (B2B) transactions between a business and another business. Use of this API requires a valid and verified B2B M-Pesa short code for the business initiating the transaction and the both businesses involved in the transaction.

**B2B - Resource URL**

POST https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest

# B2C API 

This API enables Business to Customer (B2C) transactions between a company and customers who are the end-users of its products or services. Use of this API requires a valid and verified B2C M-Pesa Short code

**B2C Resource URL**

POST https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest

# Account Balance API 

The Account Balance API requests for the account balance of a shortcode.

**Account Balance - Resource URL**

POST https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query

## Types of Command IDs one would probably use

| Parameter  |  Description                                  |  B2C                           |B2B                                         |C2B  
| -----------|-----------------------------------------------|--------------------------------|--------------------------------------------|----------------------------------:|
| CommandId  |  Unique command for each transaction type     | SalaryPayment, BusinessPayment,| BusinessPayBill, MerchantToMerchantTransfer| CustomerPayBillOnline             |
|            |                                               | PromotionPayment               | MerchantTransferFromMerchantToWorking,     |                                   |
|            |                                               |                                | MerchantServicesMMFAccountTransfer,        |                                   |
|            |                                               |                                | AgencyFloatAdvance Amount                  |                                   |                                                        

## B2C Query Parameters 

| Parameter         |  Description                                                                                                                                     |  
| ------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| IntiatorName      | This is the credentials/username used to authenticate the transaction request.                                                                   |
| SecurityCredential| Base64 encoded string of the Security Credential, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.|
| CommandID         | Unique command for each transaction type e.g. SalaryPayment, BusinessPayment, PromotionPayment.                                                  |
| Amount            | The amount being transacted.                                                                                                                     |
| PartyA            | Organization’s shortcode initiating the transaction.                                                                                             |
| PartyB            | Phone number receiving the transaction.                                                                                                          |  
| Remarks           | Comments that are sent along with the transaction.                                                                                               |  
| QueueTimeOutURL   | The timeout end-point that receives a timeout response.                                                                                          |  
| ResultURL         | The end-point that receives the response of the transaction                                                                                      |  
| Occasion          | Optional                                                                                                                                         |


## B2B Request Parameters

| Parameter         |  Description                                                                                                                                     |  
| ------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Intiator          | This is the credentials/username used to authenticate the transaction request.                                                                   |
| SecurityCredential| Base64 encoded string of the Security Credential, which is encrypted using M-Pesa public key and validates the transaction on M-Pesa Core system.|
| CommandID         | Unique command for each transaction type, possible values are: BusinessPayBill, MerchantToMerchantTransfer, MerchantTransferFromMerchantToWorking|
|                   | MerchantServicesMMFAccountTransfer, AgencyFloatAdvance.                                                                                          |
|                   |                                                                                                                                                  |
| Amount            | The amount being transacted.                                                                                                                     |
| PartyA            | Organization’s shortcode initiating the transaction.                                                                                             |
| PartyB            | Organization’s short code receiving the funds being transacted.                                                                                  |         | Sender Identifier | Type of organization sending the transaction.                                                                                                    |  
| Remarks           | Comments that are sent along with the transaction.                                                                                               |  
| QueueTimeOutURL   | The path that stores information of time out transactions it should be properly validated to make sure that it contains the port, URI and domain |
|                   | name or publicly available IP.                                                                                                                   |  
| ResultURL         |The path that receives results from M-Pesa it should be properly validated to make sure that it contains the port, URI and domain name or publicly|
|                   |available IP.                                                                                                                                     |  
| AccountReference  | Account Reference mandatory for “BusinessPaybill” CommandID.                                                                                     |                                                                                                                                        

## B2B Response Parameters

| Parameter               |  Description                                                                      |  
| ------------------------|-----------------------------------------------------------------------------------|
| ConversationID          | A unique numeric code generated by the M-Pesa system of the response to a request.|
| OriginatorConversationID| A unique numeric code generated by the M-Pesa system of the request.              |
| ResponseDescription     | A response message from the M-Pesa system accompanying the response to a request. |


## C2B Register URL - Request Parameters

| Parameter         |  Description                      |  
| ------------------|-----------------------------------|
| ValidationURL     | Validation URL for the client.    |
| ConfirmationURL   | Confirmation URL for the client.  |
| ResponseType      | Default response type for timeout.|
| ShortCode         |The short code of the organization.|



## C2B Register URL - Response Parameters

| Parameter               |  Description                                                                        |  
| ------------------------|-------------------------------------------------------------------------------------|
| ConversationID          | A unique numeric code generated by the M-Pesa system of the response to a request.  |
| OriginatorConversationID| A unique numeric code generated by the M-Pesa system of the request.                |
| ResponseDescription     | A response message from the M-Pesa system accompanying the response to a request.   |


## C2B Simulate Transaction
C2B Simulate Transaction - Resource URL

POST https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate


## C2B Simulate Transaction - Request Parameters

| Parameter               |  Description                                                                                      |  
| ------------------------|---------------------------------------------------------------------------------------------------|
| CommandID               | Unique command for each transaction type.                                                         |
| Amount                  | The amount been transacted.                                                                       |
| MSISDN                  | MSISDN (phone number) sending the transaction, start with country code without the plus(+) sign.  |
| BillRefNumber           | Bill Reference Number (Optional).                                                                 |
| ShortCode               | 6 digit M-Pesa Till Number or PayBill Number                                                      |


## C2B Simulate Transaction - Response Parameters

| Parameter               |  Description                                                                                      |  
| ------------------------|---------------------------------------------------------------------------------------------------|
| ConversationID          | A unique numeric code generated by the M-Pesa system of the response to a request.                |
| OriginatorConversationID| A unique numeric code generated by the M-Pesa system of the request.                              |
| ResponseDescription     | A response message from the M-Pesa system accompanying the response to a request.                 |



## Lipa na M-Pesa Online Payment - Request Parameters

| Parameter               |  Description                                                                                                          |  
| ------------------------|-----------------------------------------------------------------------------------------------------------------------|
| BusinessShortCode       | The organization shortcode used to receive the transaction.                                                           |
| Password                | The password for encrypting the request. This is generated by base64 encoding BusinessShortcode, Passkey and Timestamp|
| Timestamp               | The timestamp of the transaction in the format yyyymmddhhiiss.                                                        |
| TransactionType         | The transaction type to be used for this request. Only CustomerPayBillOnline is supported.                            |
| Amount                  | The amount to be transacted.                                                                                          |
| PartyA                  | The MSISDN sending the funds.                                                                                         |
| PartyB                  | The organization shortcode receiving the funds.                                                                       |
| PhoneNumber             | The MSISDN sending the funds.                                                                                         |
| CallBackURL             | The url to where responses from M-Pesa will be sent to.                                                               |
| AccountReference        | Used with M-Pesa PayBills.                                                                                            |
| TransactionDesc         | A description of the transaction.                                                                                     |


## Lipa na M-Pesa Online Payment - Response Parameters

| Parameter              |  Description                                                                                                          |  
| -----------------------|-----------------------------------------------------------------------------------------------------------------------|
| MerchantRequestID      | Merchant Request ID                                                                                                   |
| CheckoutRequestID      | Check out Request ID                                                                                                  |
| ResponseCode           | Response Code                                                                                                         |
| ResultDesc             | Result Desc                                                                                                           |
| ResponseDescription    | Response Description message                                                                                          |
| ResultCode             | Result Code                                                                                                           |


Lipa na M-Pesa Online Query Request

## Lipa na M-Pesa Online Query Request - Resource URL

POST https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query


## Lipa Na M_Pesa Online Query Request - Request Parameters 

| Parameter              |  Description                                                                                                          |  
| -----------------------|-----------------------------------------------------------------------------------------------------------------------|
| BusinessShortCode      | Business Short Code                                                                                                   |
| Password               | Password                                                                                                              |
| Timestamp              | Timestamp                                                                                                             |
| CheckoutRequestID      | Checkout RequestID                                                                                                    |    


## Lipa na M-Pesa Online Query Request - Response Parameters

| Parameter              |  Description                                                                                                          |  
| -----------------------|-----------------------------------------------------------------------------------------------------------------------|
| MerchantRequestID      | Merchant Request ID                                                                                                   |
| CheckoutRequestID      | Check out Request ID                                                                                                  |
| ResponseCode           | Response Code                                                                                                         |
| ResultDesc             | Result Desc                                                                                                           |  
| ResponseDescription    | Response Description message                                                                                          |  
| ResultCode             | Result Code                                                                                                           |  



# Creating a HTTP Server Listener

M-Pesa APIs are asynchronous. When a valid M-Pesa API request is received by the API Gateway, it is sent to M-Pesa where it is added to a queue. M-Pesa then processes the requests in the queue and sends a response to the API Gateway which then forwards the response to the URL registered in the CallBackURL or ResultURL request parameter. Whenever M-Pesa receives more requests than the queue can handle, M-Pesa responds by rejecting any more requests and the API Gateway sends a queue timeout response to the URL registered in the QueueTimeOutURL request parameter.

To receive responses, either M-Pesa results or queue timeouts, an HTTP listener will be needed. The listener should be deployed to a server that can receive traffic over the internet. On local host, use an http tunnelling client like ngrok or localtunnel to get a public IP that will enable your local host to receive traffic over the internet. Sample json responses that are received on callback urls or queue timeout urls are provided in the ‘Json Response’ tab on the top right corner for each API. Sample http listeners are also provided on the right in Python, NodeJS, PHP and Java.

The API Gateway does not cache responses from M-Pesa, should the server running the HTTP listener be unavailable or inaccessible,the API Gateway will log a 503 error and discard the M-Pesa results.

The HTTP listner should deploy POST methods for receiving M-Pesa responses on CallBackURL or ResultURL and for receiving queue timeouts on QueueTimeOutURL.

