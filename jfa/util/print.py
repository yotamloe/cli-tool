import json
import click


def _print_json(string):
    """Pretty print json string"""
    parsed = json.loads(string)
    click.echo(json.dumps(parsed, indent=2))


def _print_response_error(response):
    error_message = json.loads(response.text)['errors'][0]['message']
    click.echo(f'Error: {error_message}')
