class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative!")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self._capacity or n > (self._size + n):
            raise ValueError("Out of capacity!")
        self.deposit = n
        self._size += self.deposit

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Out of size!")
        self.withdraw = n
        self._size -= self.withdraw

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(3)
    print(jar.capacity)
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.withdraw(1)
    print(jar)

if __name__=="__main__":
    main()

