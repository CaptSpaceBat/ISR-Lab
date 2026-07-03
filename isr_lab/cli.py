import typer

app = typer.Typer(
    help="ISR-Lab - Quantitative Horse Racing Research Platform"
)


@app.command()
def version() -> None:
    """Display the application version."""
    print("ISR-Lab v0.1.0")


@app.command()
def init() -> None:
    """Initialise the ISR-Lab database."""
    print("Initialising database...")


@app.command()
def verify() -> None:
    """Verify configuration and API connectivity."""
    print("Verifying configuration...")


@app.command()
def status() -> None:
    """Display database status."""
    print("Database status...")


if __name__ == "__main__":
    app()