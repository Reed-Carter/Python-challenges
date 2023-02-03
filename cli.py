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


# adding a group of cli sub-commands
# this is just a placeholder to add the sub-commands later
@click.group()
def cli():
    """A Program to sleep or dance!"""
    pass


# sleep sub-command with --duration option
@click.command()
@click.option('--duration', type=int, default=1, help='Number of seconds to sleep')
def sleep(duration):
    """sleep for a bit"""
    click.echo(f"sleeping for {duration} seconds")
    time.sleep(duration)


# dance sub-command with --style option
@click.command()
@click.option('--style', default='Cha Cha', help='Type of dance')
def dance(style):
    """dancing the night away!"""
    click.echo(f"dancing {style}")


# now, add the sub-commands to the cli group
cli.add_command(sleep)
cli.add_command(dance)


if __name__ == '__main__':
    cli()