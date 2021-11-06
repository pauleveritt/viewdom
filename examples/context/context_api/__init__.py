"""Use the Context API to avoid passing values down a long tree."""
from viewdom import html
from viewdom import render


def NavHeading(title):
    """A navigation heading component."""
    return html("<h1>{title}</h1>")


def Nav(site):
    """A navigation component."""
    return html('<nav><{NavHeading} title={site["title"]}/></nav>')


def PageHeading(title):
    """Title block for a page."""
    return html("<h2>{title}</h2>")


def Main(page):
    """Full page layout."""
    return html('<{PageHeading} title={page["title"]}/>')


def App(site, page):
    """An app for a site."""
    return html(
        """
        <{Nav} site={site}/>
        <{Main} page={page}/>
    """
    )


def main() -> str:
    """Main entry point."""
    site = dict(title="My Site")
    page = dict(title="My Page")

    return render(
        html(
            """
        <{App} site={site} page={page} />
"""
        )
    )
