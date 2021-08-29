from viewdom import html, render


def DefaultHeading():  # pragma: nocover
    return html('<h1>Default Heading</h1>')


def OtherHeading():
    return html('<h1>Other Heading</h1>')


def Body(heading=None):
    return html('<body>{heading if heading else DefaultHeading}</body>')


result = render(html('<{Body} heading={OtherHeading}/>'))
expected = '<body><h1>Other Heading</h1></body>'


def test():
    return expected, result
