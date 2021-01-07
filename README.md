# Jfa a CLI tool by Yotam loewenbach
## Built with:
1. Python 3.7
2. [Click](https://click.palletsprojects.com/en/7.x/) 7.1.2
3. [Requests](https://pypi.org/project/requests/) 2.25.1
## How to use:
* Install the package using pip (you will need credentials):
``` shell
pip install jfa -i http://yotamloewenbach.jfrog.io/artifactory/api/pypi/Jfrog_instance_cli/simple --trusted-host yotamloewenbach.jfrog.io
```
* Login to your instance (admin users only):
``` shell
jfa login
```
Or
```shell
jfa login --username <username> --password <password> --server <server>
```
You will need to provide:
1. `username` - your artifactory username
2. `password` - your artifactory password
3. `server` - your jfrog.io subdomain (for example if your instance url is `http://myinstance.jfrog.io` enter `myinstance`)
* Run `jfa --help` to list all commands:
```shell
Usage: jfa [OPTIONS] COMMAND [ARGS]...

  Welcome to JFA - CLI tool for jfrog artifactory made by Yotam loewenabch

Options:
  --help  Show this message and exit.

Commands:
  login    Login to your Jfrog artifactory instance
  storage  Jfrog artifactory storage information
  system   Jfrog artifactory system information
  user     User administration for your Jfrog artifactory instance
```
* Play around, have fun 🚀