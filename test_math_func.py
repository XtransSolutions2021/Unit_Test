from math_func import studentDB
#import pytest

def setup_module(module):
    print("----Setup-----")
    global db
    db = studentDB()
    db.connect('data.json')

def teardown_module(module):
    print("----teardown-----")
    db.close()

def test_scott_data():
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'



def test_mark_data():
    scott_data = db.get_data('Mark')
    assert scott_data['id'] == 2
    assert scott_data['name'] == 'Mark'
    assert scott_data['result'] == 'fail'

def test_krishan_data():
    scott_data = db.get_data('Krishan')
    assert scott_data['id'] == 3
    assert scott_data['name'] == 'Krishan'
    assert scott_data['result'] == 'pass'