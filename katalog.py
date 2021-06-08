import click
from lib.db import load_db, save_db
from lib.fetch_lang import fetch_lang


@click.group()
def cli():
    pass


@cli.command()
def list():
    """List known katas"""
    db = load_db()
    if db:
        print("Known katas:")
        for kata in db:
            print(kata)
    else:
        print("No known katas.")


@cli.command()
@click.argument("kataid")
def show(kataid):
    """Show information about kata"""
    db = load_db()
    kata = db.get(kataid, None)
    if kata:
        print(f"Kata ID:   {kataid}")
        print(f"Kata URL:  {kata['url']}")
        print(f"Languages: {', '.join(kata['lang'])}")
    else:
        print(f"'{kataid}' not found!")


@cli.command()
@click.argument("url")
def add(url):
    """Add a kata to katalog"""
    kataid = input("Kata ID: ")
    print("Fetching languages...")
    lang = fetch_lang(url)
    db = load_db()
    db[kataid] = {"url": url, "lang": lang}
    save_db(db)


@cli.command()
@click.argument("kataid")
def refresh(kataid):
    """Re-check languages for kata"""
    kataid = input("Kata ID: ")
    print("Fetching languages...")
    lang = "C C++ JavaScript".split()
    db = load_db()
    db[kataid] = {"url": url, "lang": lang}
    save_db(db)


if __name__ == "__main__":
    cli()
