"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """ViewDOM."""


if __name__ == "__main__":
    main(prog_name="viewdom")  # pragma: no cover
