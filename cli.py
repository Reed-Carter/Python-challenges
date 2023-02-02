# You have 15 minutes. 
# Building CLIs

# Read the “Nesting Commands” section of click’s quickstart doc:
# https://click.palletsprojects.com/en/8.1.x/quickstart/

# Create a CLI that:
# Takes two sub-commands for  sleep  and  dance
# sleep has a  --duration  option for # of secs to sleep
# dance has a  --style   option for the dance style

# Calling the script should have the following behavior:

# > python cli.py sleep --duration=2
# sleeping for 2 seconds

# > python cli.py dance --style="tango"
# dancing tango

import click
import time

@click.group()
def cli():
    pass

@click.command()
@click.option('--style', default='tango', help='dance style')
def dance(style):
    """tells dance style"""
    click.echo(f"Dancing {style}!")

@click.command()
@click.option('--sleep', default=1, help='seconds to sleep')
def sleeps(duration):
    """tells sleep time"""
    click.echo(f"sleeping for {duration}!")

cli.add_command(dance)
cli.add_command(sleeps)

if __name__ == '__main__':
    cli()
