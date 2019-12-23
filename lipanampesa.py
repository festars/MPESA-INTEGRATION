import base64
import requests
from requests.auth import HTTPBasicAuth
import keys
from datetime import datetime


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formatted_time
data_to_encode = data_to_encode.encode('utf-8') #changing string to bytes
encoded_string = base64.b64encode(data_to_encode)
# decoded_string = base64.b64decode(encoded_string)
decoded_string = encoded_string.decode('utf-8')
Password = decoded_string
# print(Password)


  
  
consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
  
r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
  
json_response = r.json() #{'access_token': '9ifzdu3t3yuAm2nwB23JRxnxe3Kv', 'expires_in': '3599'}

my_access_token = json_response['access_token']


def lipana_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    request = {
    "BusinessShortCode": keys.business_shortcode,
    "Password": Password,
    "Timestamp": formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "5",
    "PartyA": keys.phone_number,
    "PartyB": keys.business_shortcode,
    "PhoneNumber": keys.phone_number,
    "CallBackURL": "https://agottech.com",
    "AccountReference": "1245",
    "TransactionDesc": "Download"
    }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

lipana_mpesa()