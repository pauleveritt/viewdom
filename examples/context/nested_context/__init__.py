from viewdom import Context  # noqa
from viewdom import html
from viewdom import render
from viewdom import use_context


def NavHeading():
    """A navigation heading component."""
    site = use_context("site")
    title = site["title"]
    return html("<h1>{title}</h1>")


def Nav():
    """A navigation component."""
    return html("<nav><{NavHeading}/></nav>")


def PageHeading(title):
    """Title block for a page."""
    return html("<h2>{title}</h2>")


def Main(page):
    """Full page layout."""
    return html('<{PageHeading} title={page["title"]}/>')


def App(page):
    """An app for a site."""
    return html(
        """
        <{Nav}/>
        <{Main} page={page}/>
    """
    )


def main():
    """Main entry point."""
    site = dict(title="My Site")
    page = dict(title="My Page")

    return render(
        html(
            """
        <{Context} site={site}>
            <{App} page={page} />
        <//>
"""
        )
    )
