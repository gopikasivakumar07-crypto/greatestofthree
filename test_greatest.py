from greatest import greatest

def test_greatest():
    assert greatest(10, 20, 30) == 30
    assert greatest(50, 20, 10) == 50
    assert greatest(10, 40, 20) == 40
    assert greatest(10, 10, 5) == 10