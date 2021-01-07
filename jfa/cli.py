import os

import click


class ComplexCLI(click.MultiCommand):
    def list_commands(self, ctx):
        """All command python files are under jfa/commands/ folder, other classes and functions are under jfa/util/
        folder """
        commands = []
        commands_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
        for filename in os.listdir(commands_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                commands.append(filename.replace("cmd_", "").replace(".py", ""))

        commands.sort()
        return commands

    def get_command(self, ctx, name):
        try:
            mod = __import__(f"jfa.commands.cmd_{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI)
def cli():
    """Welcome to JFA - CLI tool for jfrog artifactory made by Yotam loewenabch
    """
    pass