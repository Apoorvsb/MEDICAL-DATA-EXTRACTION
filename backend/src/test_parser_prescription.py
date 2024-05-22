from backend.src.parser_prescription import PrescriptionParser
import pytest
@pytest.fixture()
def testcases():
    doc1='''
    Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks -
    Lialda - take 2 pill everyday for 1 month
    Refill: 3 times
    '''

    return PrescriptionParser(doc1)
def test_name(testcases):
    assert testcases.get_field("patient_name")=="Marta Sharapova"
