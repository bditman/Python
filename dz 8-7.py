class Complex_num:
    def __init__(self, data):
        self.real = int(data.real)
        self.imag = int(data.imag)

    def __add__(self, other):
        return f"Результат солжения: {complex(self.real + other.real, self.imag + other.imag)}"

    def __mul__(self, other):
        return f"Результат умножения: " \
               f"{complex(((self.real * other.real) - (self.imag * other.imag)) + ((self.imag * other.real) + (self.real * other.imag)))}"


x = Complex_num(2 + 4j)
y = Complex_num(3 - 1j)
print(x + y)
print(x * y)

