from mypythonlib import myfunctions
def test_haversine():
    assert myfunctions.haversine(52.370216, 4.895168, 52.520008, 13.404954) == 946.3876221719835
    #946.3876221719836