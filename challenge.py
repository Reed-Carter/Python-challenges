# You have 15 minutes. 
# Building your own cli

# Research using a library called click. This library allows your python code to run like a cli like:
# gcloud projects list --region us-central1


# Build a python cli that:
# takes two parameters for --name and --count
# You must specify the --count option 
# The program should prompt for name (if not provided)
# The program should print the name for N number of count

# You can run the program as such:
# python main.py --count 3 --name DSA

# Your name: John
# Hello Joh

import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
