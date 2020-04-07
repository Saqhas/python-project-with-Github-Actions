from app import index
import sys

sys.path.insert(0, '../src')
def test_index():
    assert index() == "Hello, World!"
