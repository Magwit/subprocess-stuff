import click
import random

# https://www.youtube.com/watch?v=gLCfLOaIHoQ


@click.group()
def main():
    pass


@main.command()
@click.argument("text")
def reverse(text):
    """Reverse a string"""
    click.echo(text[::-1])


@main.command()
@click.argument("text")
def shuffle(text):
    """Shuffle a string"""
    click.echo(" ".join(random.sample(text, len(text))))


if __name__ == "__main__":
    main()
