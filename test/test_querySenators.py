import pytest
from src.querySenators import SenatorInfo
def test_getName():
    testObj = SenatorInfo("TX")
    assert testObj.getName(0) == "Ted Cruz"
    assert testObj.getName(1) == "John Cornyn"
    
    with pytest.raises(Exception):
        testObj.getName(2)

def test_getTwitter():
    testObj = SenatorInfo("TX") 
    assert testObj.getTwitter(0) == "SenTedCruz"