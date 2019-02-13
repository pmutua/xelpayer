from django.test import TestCase
from rest_framework.test import APITestCase

from .utils import *
# Create your tests here.

class SetUpMd(APITestCase):

    @classmethod
    def setUp(cls):
        consumer_key = "eiuhniNnw9S6Z0jBqqWASA1ZZDfxhbtW "
        consumer_secret = "zIjFKFzJsgJLaYzb "


        access_token = authenticate(consumer_key,consumer_secret)
        
        print(access_token)
        