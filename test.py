def test():
    try:
        1 / 0
    except ZeroDivisionError:
        pass  # be carefull with that!
    print("test")


test()
