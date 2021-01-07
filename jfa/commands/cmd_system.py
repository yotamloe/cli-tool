import click
import requests
from jfa.util.auth import Credentials, BearerAuth
from jfa.util.print import _print_response_error


class Context:
    def __init__(self):
        self.credentials = Credentials()


@click.group()
@click.pass_context
def cli(ctx):
    """Jfrog artifactory system information"""
    ctx.obj = Context()


@cli.command()
@click.pass_context
def version(ctx):
    """Returns system version"""
    try:
        response = requests.get(f'{ctx.obj.credentials.base_api_url}system',
                            auth=BearerAuth(ctx.obj.credentials.access_token))
        if response.ok:
            info = response.text
            lines = info.split('\n')
            for line in lines:
                if 'artifactory.version ' in line:
                    click.echo(line.replace(' ', ''))
        else:
            _print_response_error(response)
    except (TypeError, AttributeError):
        click.echo("Error: You are not logged in. Try to use `jfa login`")


@cli.command()
@click.pass_context
def ping(ctx):
    """System Ping"""
    try:
        response = requests.get(f'{ctx.obj.credentials.base_api_url}system/ping',
                            auth=BearerAuth(ctx.obj.credentials.access_token))
        if response.ok:
            click.echo(response.text)
        else:
            _print_response_error(response)
    except (TypeError, AttributeError):
        click.echo("Error: You are not logged in. Try to use `jfa login`")
