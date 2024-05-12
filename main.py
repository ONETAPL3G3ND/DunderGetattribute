class Base:
    def __getattribute__(self, item):
        print(f"getting: {item}")
        return super().__getattribute__(item)

class Stock(Base):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass

if __name__ == '__main__':
    a = Stock(10)
    print(a.x)