class Test(object):
    def __init__(self):
        pass

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


a = Test()
with a:
    print(a)
