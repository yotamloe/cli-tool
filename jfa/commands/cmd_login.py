from json import JSONDecodeError
import click
import requests
import json
from requests.auth import HTTPBasicAuth
from jfa.util.auth import _write_to_config


@click.command()
@click.option('--username', prompt=True, help='Your Jfrog artifactory username')
@click.option('--server', prompt=True,
              help='Your Jfrog artifactory server name aka jfrog.io subdomain name -> http://<<server name>>.jfrog.io')
@click.password_option(help='Your Jfrog artifactory password')
# The login method requires authentication with admin user username and password, the cli() function creates an
# access token and stores it in `jfk/util/config.json` file. Other auth related resources can be found in
# `jfa/util/auth.py`

def cli(username, server, password):
    """Login to your Jfrog artifactory instance"""
    token_url = 'http://{}.jfrog.io/artifactory/api/security/token'.format(server)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    params = {'username': username, 'scope': 'api:* member-of-groups:*', 'expires_in': 0}
    try:
        access_token = \
            json.loads(
                requests.post(token_url, auth=HTTPBasicAuth(username, password), headers=headers, params=params).text)[
                'access_token']
        _write_to_config(access_token, username, password, server)
        click.echo("Login successful :)")
    except (KeyError, JSONDecodeError):
        click.echo('Error: Bad credentials. Note that this tool is built only for admin users only. '
                   'Please try again, and Make sure your user have sufficient permissions')
