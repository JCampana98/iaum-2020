import requests
from requests.auth import HTTPBasicAuth

"""
    Basic Auth API ACCESS
"""
response = requests.get('https://14a90caa038d.ngrok.io/alumnos', auth=HTTPBasicAuth('elusuario', 'laclave'))
print("Status code:", response.status_code)
print("Json content: \n", response.json())

"""
    JWT API ACCESS
"""

response = requests.post('https://44ba9afc8128.ngrok.io/users/authenticate', json='{"username":"elusuario", '
                                                                                 '"password":"laclave"}')
print("Status code:", response.status_code)
print("Json content: \n", response.json())
