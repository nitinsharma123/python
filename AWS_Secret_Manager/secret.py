import base64
import boto3
import json
import os
import sys
from botocore.exceptions import ClientError
filename = 'data.json'
kms_id = sys.argv[1]
secret_name = sys.argv[2]
secret_json = sys.argv[3]
secret_data={}
secretdata = json.loads(secret_json)
client = boto3.client('secretsmanager')
response = client.get_secret_value(
    SecretId=secret_name,
)
if 'SecretString' in response:
    secret=response['SecretString']
for k,v in secretdata.items():
    encrypt_string = os.popen(("aws kms encrypt --key-id %s --plaintext '%s' --query CiphertextBlob --output text" % (kms_id, v))).read()
    secret_data[k] = encrypt_string
json_data = json.dumps(secret_data)
with open(filename,'w') as f:	    
    f.write(json_data)
with open('data.json', 'r') as content_file:
    secret_content = content_file.read()
dic1 = eval(secret_content)
dic2 = eval(secret)
dic3 = {**dic1, **dic2}
secret_content1 = json.dumps(dic3)
print (secret_content1)
client = boto3.client('secretsmanager')
response = client.put_secret_value(
    SecretId=secret_name,
    SecretString=secret_content1,
)