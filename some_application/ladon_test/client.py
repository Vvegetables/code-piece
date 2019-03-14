#encoding:utf-8

'''
pip install suds-jurko
'''

from suds.client import Client

url = "http://webservice.cingta.com/Calculator/soap11/description/"
headers = {
    "Content-Type": 'application/soap+xml; charset="UTF-8"'
}
client2 = Client(url, headers=headers, faults=False, timeout=15)

result = client2.service.extract_remote_addr()
print(result)