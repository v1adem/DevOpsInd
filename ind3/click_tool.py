import click

@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", required=True, help="Ім'я для виводу.")
def say(name):
    """Друкує ім’я, якщо воно не починається з p/P."""
    if name.lower().startswith("p"):
        print("Ім’я не підходить")
    else:
        print(name)


if __name__ == "__main__":
    cli()
