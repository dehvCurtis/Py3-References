from nose.tools import *

import NAME

def setup():
    print(f'Setup!')

def teardown():
    print(f'TEAR DOWN!')

def test_basic():
    print(f'I RAN!')
