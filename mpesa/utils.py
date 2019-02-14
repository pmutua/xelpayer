from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from base64 import b64encode
import requests
import datetime
import base64
# To authenticate your app and get an OAuth access token, use this code.
# An access token expires in 3600 seconds or 1 hour


from requests.auth import HTTPBasicAuth


from django.conf import settings 


consumer_key = settings.CONSUMER_KEY 
consumer_secret = settings.CONSUMER_SECRET

passkey = settings.LIPA_NA_MPESA_ONLINE_PASSKEY 




class Authenticate:
    @staticmethod
    def access_token():
        """Generates access token."""

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))
      
        data = r.json()
    
        access_token = "Bearer" + ' ' + data['access_token']

        return access_token
    
    @staticmethod 
    def password(passkey,business_short_code):
        """Get password."""
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        data = str(business_short_code) +passkey+ timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')
        return password

    @staticmethod 
    def auth_header(access_token):
        return  {"Authorization": access_token,
                "Content-Type": "application/json"
                }




INITIATOR_PASS = "YOUR_PASSWORD"
CERTIFICATE_FILE = "PATH_TO_CERTIFICATE_FILE"

# Base64 encoded string of the Security Credential, which is encrypted
# using M-Pesa public key and validates the transaction on M-Pesa Core
# system.

# When obtaining a certificate from a certificate authority (CA), the usual flow is:
# In our case safaricom

# 1.You generate a private/public key pair.
# 2.You create a request for a certificate, which is signed by your key (to prove that you own that key).
# 3.You give your CSR to a CA (but not the private key).
# 4.The CA validates that you own the resource (e.g. domain) you want a certificate for.
# 5.The CA gives you a certificate, signed by them, which identifies your public key, and the resource you are authenticated for.
# 6.You configure your server to use that certificate, combined with your
# private key, to server traffic.


def Password(code_b=None, time=None):
    cipher = (
        INITIATOR_PASS, code_b, time)
    return b64encode(cipher)


def encryptInitiatorPassword():
    cert_file = open(CERTIFICATE_FILE, 'r')
    cert_data = cert_file.read()  # read certificate file
    cert_file.close()

    cert = X509.load_cert_string(cert_data)
    pub_key = X509.load_cert_string(cert_data)
    pub_key = cert.get_pubkey()
    rsa_key = pub_key.get_rsa()
    cipher = rsa_key.public_encrypt(INITIATOR_PASS, rsa.pkcs1_padding)
    return b64encode(cipher)