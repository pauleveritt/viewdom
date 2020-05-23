from os.path import abspath, dirname, join
from time import strftime, localtime

from examples.usage.csr.bottle import route, run, static_file
from viewdom import html

STATIC_DIR = abspath(join(dirname(__file__), 'static'))


def Todos():
    return html('''
<ul>
  <li>First Item <input type="checkbox"/></li>
</ul>
    ''')


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_DIR)


@route('/todos')
def todos():
    now = strftime('%H:%M:%S', localtime())
    response = html('''
<h1 id="hello">Hello World at <em>{now}</em></h1>
<{Todos}/>
''')
    return dict(response=str(response))


@route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="static/bulma.css">
    <link rel="shortcut icon" href="https://developer.mozilla.org/static/img/favicon32.7f3da72dcea1.png">
  </head>
  <body>
  <section class="section">
    <div class="container">
      <h1 class="title">
        Hello World
      </h1>
      <p class="subtitle">
        My first website with <strong>Bulma</strong>!
      </p>
      <p><button id="update">Update</button></p>
      <div id="todos"></div>
    </div>
  </section>
  <script src="static/app.js" type="module"></script>
  </body>
</html>
    '''


if __name__ == '__main__':
    run(host='localhost', port=8089, reloader=True, fast=True)
