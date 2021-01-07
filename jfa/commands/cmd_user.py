import click
import requests
from jfa.util.auth import Credentials, BearerAuth
from jfa.util.print import _print_response_error
from jfa.util.user import ArtiifactoryUser


class Context:
    def __init__(self):
        self.credentials = Credentials()


@click.group()
@click.pass_context
def cli(ctx):
    """User administration for your Jfrog artifactory instance"""
    ctx.obj = Context()


@cli.command()
@click.option('--name', '-n', required=True, type=str, help="Username for the new user")
@click.option('--password', '-p', required=True, type=str, help="Password for the new user")
@click.option('--email', '-em', required=True, type=str, help="Email of the new user")
@click.option('--admin', '-a', required=False, type=bool, default=False, show_default=True, help="Enter true for user "
                                                                                                 "admin creation")
@click.option('--group', '-g', required=False, multiple=True, type=str, help="Add new users to a group, you can "
                                                                             "use this option multiple times")
@click.option('--profileupdatable', '-pu', required=False, type=bool, default=True, show_default=True)
@click.option('--disableuiccess', '-dui', required=False, type=bool, default=True, show_default=True)
@click.option('--internalpassworddisabled', '-ipd', required=False, type=bool, default=False, show_default=True)
@click.option('--watchmanager', '-wm', required=False, type=bool, default=False, show_default=True)
@click.option('--policymanager', '-pm', required=False, type=bool, default=False, show_default=True)
@click.pass_context
def create(ctx, name, password, email, admin, group, profileupdatable, disableuiccess, internalpassworddisabled,
           watchmanager, policymanager):
    """Create new artifactory user"""
    new_user = ArtiifactoryUser(name=name, password=password, email=email, admin=admin, groups=group,
                                profileupdatable=profileupdatable, disableuiccess=disableuiccess,
                                internalpassworddisabled=internalpassworddisabled, watchmanager=watchmanager,
                                policymanager=policymanager)
    try:
        response = requests.put(f'{ctx.obj.credentials.base_api_url}security/users/{new_user.name}',
                                auth=BearerAuth(ctx.obj.credentials.access_token), data=new_user.to_json())
        if response.ok:
            click.echo(f'User with name: `{new_user.name}` was created successfully')
        else:
            _print_response_error(response)
    except (TypeError, AttributeError):
        click.echo("Error: You are not logged in. Try to use `jfa login`")


@cli.command()
@click.option('--name', '-n', required=True, type=str, help="Username to delete")
@click.pass_context
def delete(ctx, name):
    """Deletes artifactory user"""
    try:
        response = requests.delete(f'{ctx.obj.credentials.base_api_url}security/users/{name}',
                                   auth=BearerAuth(ctx.obj.credentials.access_token))
        if response.ok:
            click.echo(f'User with name: `{name}` was deleted successfully')
        else:
            _print_response_error(response)
    except (TypeError, AttributeError):
        click.echo("Error: You are not logged in. Try to use `jfa login`")
