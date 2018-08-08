from collections import deque


class Fila:
    def __init__(self, n):
        self.numeros = deque()
        self.insert(n)

    def insert(self, n):
        if isinstance(n, int):
            self.numeros.append(n)
        elif isinstance(n, list):
            self.numeros.extend(n)
        else:
            raise ValueError

    def pop(self):
        return self.numeros.popleft()

    def min(self):
        return min(self.numeros)

    def max(self):
        return max(self.numeros)

    def __repr__(self):
        return f'{self.numeros}'