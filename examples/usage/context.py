"""
Use the Context API to avoid passing values down a long tree.
"""

from viewdom import html, render


def NavHeading(title):
    return html('<h1>{title}</h1>')


def Nav(site):
    return html('<nav><{NavHeading} title={site["title"]}/></nav>')


def PageHeading(title):
    return html('<h2>{title}</h2>')


def Main(page):
    return html('<{PageHeading} title={page["title"]}/>')


def App(site, page):
    return html(
        '''
        <{Nav} site={site}/>
        <{Main} page={page}/>
    '''
    )


def main():
    site = dict(title='My Site')
    page = dict(title='My Page')

    return render(
        html(
            '''
        <{App} site={site} page={page} />
'''
        )
    )


result = main()
expected = '<nav><h1>My Site</h1></nav><h2>My Page</h2>'


def test():
    return expected, result
