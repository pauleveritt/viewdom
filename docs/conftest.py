import sys
from os import getcwd, chdir
from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp

from sybil import Sybil
from sybil.parsers.codeblock import CodeBlockParser
from sybil.parsers.doctest import DocTestParser


def sybil_setup(namespace):
    import viewdomx

    t = Path(viewdom.__file__).parents[1] / 'docs'
    sys.path.append(str(t))
    namespace['path'] = path = mkdtemp()
    namespace['cwd'] = getcwd()
    chdir(path)


def sybil_teardown(namespace):
    chdir(namespace['cwd'])
    rmtree(namespace['path'])


# load_tests = Sybil(
#     parsers=[
#         DocTestParser(),
#         CodeBlockParser(future_imports=['print_function']),
#     ],
#     path='../docs/',
#     pattern='*.rst',
#     setup=sybil_setup, teardown=sybil_teardown
# ).unittest()

pytest_collect_file = Sybil(
    parsers=[
        DocTestParser(),
        CodeBlockParser(future_imports=['print_function']),
    ],
    # setup=sybil_setup,
    # teardown=sybil_teardown,
    pattern='*.rst',
).pytest()
