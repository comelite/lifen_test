"""
main file for running the app
"""
from pathlib import Path

import typer

from core import app

app_typer = typer.Typer()


@app_typer.command()
def main(
    path_load: str = typer.Option("data/docs.json", help="Path to json file"),
    path_save: str = typer.Option("data/docs_save.json", help="Path to json file"),
):
    """
    Run the app
    Args:
        path_load (str): Path to json file
        path_save (str): Path to json file
    """
    app_name = app.App()
    app_name.run(path_load=Path(path_load), path_save=Path(path_save))


if __name__ == "__main__":
    app_typer()
