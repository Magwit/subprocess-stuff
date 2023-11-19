import click

# https://www.youtube.com/watch?v=vJIXr4Kx5oo
VERSION = "0.0.1"


@click.command()
@click.version_option(VERSION)
@click.argument("names", nargs=2)
@click.option("-a", "--age", type=int, default=0)
# @click.option("-s", "--shout", is_flag=True)
@click.option("--shout/--no-shout")
def profile(names, age, shout):
    output = f"My name is {names}, and I am {age} years."
    if shout:
        output = output.upper()

    print(output)


if __name__ == "__main__":
    profile()
