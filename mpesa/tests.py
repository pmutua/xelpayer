import datetime
from django.test import TestCase
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from .utils import *
# C
from django.conf import settings

from rest_framework.test import APIClient
from .models import *

consumer_key = settings.CONSUMER_KEY
consumer_secret = settings.CONSUMER_SECRET


access_token = Authenticate.access_token()

# print(access_token)

auth_header = Authenticate.auth_header(access_token)

print(auth_header)


class SetUpMd(APITestCase):

    @classmethod
    def setUp(cls):

        cls.occassion = Occassion.objects.create(name="Occassion")

        cls.command_id = CommandID.objects.create(name="CustomerPayBillOnline")
        # Add Business Code
        cls.bussiness_short_code = BusinessShortCodeOrNumber.objects.create(
            number=174379)

        cls.customer_phone = PhoneNumber.objects.create(number=254722212132)

        cls.transaction_type = TransactionType.objects.create(name="CustomerPayBillOnline")

        cls.timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')

        cls.command_id = CommandID.objects.create(name="CustomerPayBillOnline")

        cls.initiator_name = InitiatorName.objects.create(name="apitest361")

        cls.client = APIClient()

    def test_can_initiate_lipa_na_mpesa_transaction(self):
        # print(self.bussiness_short_code.id)
        # print(self.customer_phone.id)
        # BODY OR PAYLOAD
        payload = {
            "business_short_code": self.bussiness_short_code.id,
            "initiator_name": self.initiator_name.name,
            "transaction_type": self.transaction_type.id,
            "TransactionType": "CustomerPayBillOnline",
            "command_id": self.command_id.id,
            "amount": 100.00,
            "remarks": "174379",
            "customer_phone_number": self.customer_phone.id
        }

        # print(payload)
        # url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #C2B URL

        url = reverse('mpesa:initiate_lipa_na_mpesa_online_transaction')

        res = self.client.post(url, json=payload, format='json')

        print(res.data["customer_phone_number"])

