from dlg_py.functs import get_total

def test_get_total_1():
    ls = [1,2,3,4]

    assert get_total(ls) == 10

def test_get_total_2():
    ls = list(range(101))

    assert get_total(ls) == 5050
