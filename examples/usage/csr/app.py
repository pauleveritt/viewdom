from datetime import datetime
import json
from os.path import abspath, dirname, join

from examples.usage.csr.bottle import route, run, static_file, template

STATIC_DIR = abspath(join(dirname(__file__), 'static'))


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=STATIC_DIR)


@route('/todos')
def todos():
    now = str(datetime.now())
    child1 = ['em', {}, ['Hello',]]
    response = ['h1', dict(id='hello'), ['Some Text', child1]]
    return dict(response=response)
    # child = dict(
    #     type='em',
    #     props=dict(),
    #     children='XXXXX'
    # )
    # return dict(
    #     type='h1',
    #     props=dict(id='hello'),
    #     children=[f'Hello World at {now}', child]
    # )


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
      <p id="message"></p>
    </div>
  </section>
  <script src="static/app.js" type="module"></script>
  </body>
</html>
    '''


if __name__ == '__main__':
    run(host='localhost', port=8089, reloader=True)
