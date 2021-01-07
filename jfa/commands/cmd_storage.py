import click
import requests
from jfa.util.auth import Credentials, BearerAuth
from jfa.util.print import _print_json


class Context:
    def __init__(self):
        self.credentials = Credentials()


@click.group()
@click.pass_context
def cli(ctx):
    """Jfrog artifactory storage information"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def info(ctx):
    """Get Storage Info"""
    try:
        info = requests.get(f'{ctx.obj.credentials.base_api_url}storageinfo',
                            auth=BearerAuth(ctx.obj.credentials.access_token)).text
        _print_json(info)
    except (TypeError, AttributeError):
        click.echo("Error: You are not logged in. Try to use `jfa login`")

