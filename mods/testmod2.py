def init():
    print("testmodul 2 ist da")

if __name__ == "__main__":
    print("please import me")
    raise Exception
else:
    print("imported " + str(__name__))
