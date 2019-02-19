import base64
import json
from datetime import datetime
import datetime
from django.conf import settings

from mpesa.models import AuthToken
from mpesa.utilities.http import post


def process_online_checkout(msisdn, amount, account_reference, transaction_desc):
    """
    Handle the online checkout ie lipa na mpesa online.
    :param msisdn:
    :param amount:
    :param account_reference:
    :param transaction_desc:
    :return:
    """
    url = settings.LIPA_NA_MPESA_ONLINE_CHECKOUT_URL 
    headers = {"Content-Type": 'application/json',
               'Authorization': 'Bearer {}'.format(AuthToken.objects.get_token('lipanampesa'))}
    timestamp = datetime.datetime.today.strftime('%Y%m%d%H%M%S')
    #TODO Test with convert_time = time.strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(bytes('{}{}{}'.format(settings.LIPA_NA_MPESA_ONLINE_SHORT_CODE, settings.LIPA_NA_MPESA_ONLINE_PASSKEY,
                                                      timestamp), 'utf-8')).decode('utf-8')
    body = dict(
        BusinessShortCode=settings.LIPA_NA_MPESA_ONLINE_SHORT_CODE,
        Password=password,
        Timestamp=timestamp,
        TransactionType=settings.LIPA_NA_MPESA_ONLINE_TRANSACTION_TYPE,
        Amount=str(amount),
        PartyA=str(msisdn),
        PartyB=settings.LIPA_NA_MPESA_ONLINE_SHORT_CODE,
        PhoneNumber=str(msisdn),
        CallBackURL=settings.LIPA_NA_MPESA_ONLINE_CHECKOUT_CALLBACK_URL,
        AccountReference=account_reference,
        TransactionDesc=transaction_desc
    )
    response = post(url=url, headers=headers, data=json.dumps(body))
    return response.json()
