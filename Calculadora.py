def sumar (a: float, b: float) -> float:
    return a + b

def restar (a: float, b: float) -> float:
    return a - b

def multiplicar (a: float, b: float) -> float:
    return a * b

def dividir (a: float, b: float) -> float:
    return a / b

def potencia (a: float, b: float) -> float:
    return a ** b

def elevar (a: float) -> float:
    return a ** 3

if __name__ == "__main__":
    print(sumar(2,5))
    print(restar(8,3))
    print(multiplicar(9,4))
    print(dividir(12,6))
    print(potencia(3,3))
    print(elevar(5))
