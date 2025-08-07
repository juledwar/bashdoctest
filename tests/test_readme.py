import doctest
import sys

import pytest


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Python 3.10+ required")
def test_readme():
    errs, _ = doctest.testfile('../README.rst', report=True)
    assert not errs
