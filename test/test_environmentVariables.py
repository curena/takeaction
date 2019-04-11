import pytest
import os

def test_APIKey():
    assert os.environ.get("SECRET_KEY") != None
    assert os.environ.get("SECRUT_KEY") == None