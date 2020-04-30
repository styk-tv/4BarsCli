import requests
from urllib.parse import urlencode
from collections import OrderedDict
from fourbars.api.connect import Connect
import json


class Asset(object):
    connect = None

    def __init__(self):
        self.connect = Connect()
        if not self.connect.login():
            print("Login Failed")
            return

    # TODO: change to PUT (new) for CRUD consistency
    def post(self, in_schema_asset):
        headers = {
            'Authorization': '{0}'.format(self.connect.get_auth_header()),
            'content-type': 'application/json'
        }
        response = requests.post(self.connect.settings.api + 'mc/asset/',
                                 json=json.dumps(in_schema_asset.as_json()),
                                 headers=headers
                                 )

        print()
        print(response.status_code, response.text)
        pass

    def get_md5_quick(self, in_md5):
        path = 'mc/asset/md5/quick/{}'.format(in_md5)
        headers = {
            'Authorization': '{0}'.format(self.connect.get_auth_header()),
            'content-type': 'application/json'
        }
        response = requests.get(self.connect.settings.fourbars.api+'{0}'.format(path),
                                headers=headers
                                )

        if response.status_code == 200:
            return response.text.replace('\n','').replace('"', '')
        else:
            return None
