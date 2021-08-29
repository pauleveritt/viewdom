from viewdom import html, render, use_context, Context


def NavHeading():
    site = use_context('site')
    title = site['title']
    return html('<h1>{title}</h1>')


def Nav():
    return html('<nav><{NavHeading}/></nav>')


def PageHeading(title):
    return html('<h2>{title}</h2>')


def Main(page):
    return html('<{PageHeading} title={page["title"]}/>')


def App(page):
    return html(
        '''
        <{Nav}/>
        <{Main} page={page}/>
    '''
    )


def main():
    site = dict(title='My Site')
    page = dict(title='My Page')

    return render(
        html(
            '''
        <{Context} site={site}>
            <{App} page={page} />
        <//>
'''
        )
    )


result = main()
expected = '<nav><h1>My Site</h1></nav><h2>My Page</h2>'


def test():
    return expected, result
