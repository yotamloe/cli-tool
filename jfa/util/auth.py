import os
import requests
import json


class BearerAuth(requests.auth.AuthBase):
    """Custom auth class to impalement bearer token authentication easily"""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer {}".format(self.token)
        return r


class Credentials:
    """Class to store credentials and related session info"""

    def __init__(self):
        try:
            self.access_token, self.password, self.server, self.user = _get_credentials_from_config()
            self.base_api_url = 'http://{}.jfrog.io/artifactory/api/'.format(self.server)
        except (TypeError, json.decoder.JSONDecodeError):
            pass


def _write_to_config(access_token, username, password, server):
    """Writes credentials to config.json file for future use"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/config.json".format(dir_path), "r+") as config_file:
        new_json = {
            'user': username,
            'password': password,
            'access_token': access_token,
            'server': server
        }
        json.dump(new_json, config_file)
        config_file.truncate()
        config_file.close()


def _get_credentials_from_config():
    """Reads credentials from config.json"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/config.json".format(dir_path), "r+") as config_file:
        config_json = json.load(config_file)
        config_file.truncate()
        config_file.close()
        try:
            return config_json['access_token'], config_json['password'], config_json['server'], config_json['user']
        except (TypeError, json.decoder.JSONDecodeError):
            pass
