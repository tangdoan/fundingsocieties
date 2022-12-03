def test_1():
    a = 1
    b = 2
    assert a != b

def test_2():
    name ="Selenium"
    title = "Selenium is for web automation"
    assert name in title

def test_3():
    name = "jenkins"
    title = "Jenkins is CI server"
    assert name is title, "Title does not match"
