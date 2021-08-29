"""
Components can be any kind of callable.
"""

from dataclasses import dataclass

from viewdom import html, render


@dataclass
class Greeting:
    name: str

    def __call__(self):
        return f'Hello {self.name}'


greeting = Greeting(name='viewdom')
result = render(html('<div><{greeting} /></div>'))
expected = '<div>Hello viewdom</div>'


def test():
    return expected, result
