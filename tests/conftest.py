"""Test configuration."""
import os
import sys

import pytest


@pytest.fixture(scope="session", autouse=True)
def examples_path():
    """Automatically add the root of the repo to path."""
    ep = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.insert(0, ep)
