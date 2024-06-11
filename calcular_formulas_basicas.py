import math

# def formula_perimetro_cuadrado():
#     lado = input("Lado: ")
#     perimetro = lado*4
#     return f"Perimetro: {perimetro}"

# def formula_perimetro_rectangulo():
#     ancho = input("Ancho: ")
#     largo = input("Largo: ")
#     perimetro = 2*(ancho+largo)
#     return f"Perimetro: {perimetro}"

# def formula_perimetro_triangulo():
#     lado1 = input("Lado1: ")
#     lado2 = input("Lado2: ")
#     lado3 = input("Lado3: ")
#     perimetro = lado1 + lado2 + lado3
#     return f"Perimetro: {perimetro}"

# def formula_area_cuadrado():
#     lado = input("Lado: ")
#     area = lado**2
#     return f"Area: {area}"

# def formula_area_rectangulo():
#     base = input("Base: ")
#     altura = input("Altura: ")
#     area = base*altura
#     return f"Area {area}"

# def formula_area_cuadrado():
#     lado = input("Lado: ")
#     area = lado**2
#     return f"Area {area}"

# def formula_circuferencia():
#     radio = float(input("Radio: "))
#     area =  2 * math.pi * radio
#     return f"Area {area}"

# def formula_area_circulo():
#     radio = float(input("Radio: "))
#     area =  math.pi * radio*2
#     return f"Area {area}"



# class Cuadrado():
#     def __init__(self,lado):
#         self.lado = lado
# class Rectangulo():
#     def __init__(self,longitud,anchura):
#         self.longitud = longitud
#         self.anchura = anchura
# class Triangulo():
#     def __init__(self,lado1,lado2,lado3,base,altura):
#         self.lado = lado
#         self.base = base
#         self.altura = altura
# class Circuferencia():
#     def __init__(self,radio):
#         self.radio = radio
# class Paralelogramo():
#     def __init__(self,lado1,lado2,base,altura):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.base = base
#         self.altura = altura
# class Trapecio():
#     def __init__(self,lado,base_mayor,base_menor,altura):
#         self.lado = lado
#         self.base_mayor = base_mayor
#         self.base_menor = base_menor
#         self.altura = altura
# class Rombo():
#     def __init__(self,lado,diagonal_mayor,diagonal_menor):
#         self.lado = lado
#         self.diagonal_mayor = diagonal_mayor
#         self.diagonal_menor = diagonal_menor
# class Romboide():
#     def __init__(self,lado1,lado2,base,altura):
#         self.lado1 = lado1
#         self.lado2 = lado2
#         self.base = base
#         self.altura = altura
# class PentagonoRegular():
#     def __init__(self,lado):
#         self.lado = lado
# class HexagonoRegular():
#     def __init__(self,lado):
#         self.lado = lado
# class Cubo():
#     def __init__(self,lado):
#         self.lado = lado
# class PrismaRectangular():
#     def __init__(self,longitud,anchura,altura):
#         self.longitud = longitud
#         self.anchura = anchura
#         self.altura = altura
# class Esfera():
#     def __init__(self,radio):
#         self.radio = radio
# class Cilindro():
#     def __init__(self,radio_base,altura):
#         self.radio_base = radio_base
#         self.altura = altura
# class Cono():
#     def __init__(self,radio_base,altura):
#         self.radio_base = radio_base
#         self.altura = altura
# class Piramide():
#     def __init__(self,area_base,perimetro_base,longitud_apotema,altura):
#         self.area_base = area_base
#         self.perimetro_base = perimetro_base
#         self.longitud_apotema = longitud_apotema
#         self.altura = altura



# lado = int(input("Lado: "))
# base = int(input("Base: "))
# altura = int(input("Altura: "))
# radio = int(input("Radio: "))

# perimetro_cuadrado = Cuadrado(lado*4)
# area_cuadrado = Cuadrado(lado**2)


# print(f"Perimetro: {perimetro_cuadrado.lado}")





class Cuadrado():
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2
    def perimetro(self):
        return 4 * self.lado

def perimetro_area_cuadrado():
    while True:
        lado = float(input("Lado: "))
        # if lado.is_integer():
        #     lado = int(lado)
        try:
            if lado >= 0:
                break
        except ValueError:
            continue
    cuadrado = Cuadrado(lado)
    area_cuadrado = cuadrado.area()
    if area_cuadrado.is_integer():
        area_cuadrado = int(area_cuadrado)
    perimetro_cuadrado = cuadrado.perimetro()
    if perimetro_cuadrado.is_integer():
        perimetro_cuadrado = int(perimetro_cuadrado)
    return f"El perímetro del cuadrado es de {perimetro_cuadrado} unidades y su área es de {area_cuadrado} unidades cuadradas"

print(perimetro_area_cuadrado())



class Rectangulo():
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura
    def area(self):
        return self.longitud * self.anchura
    def perimetro(self):
        return 2 * (self.longitud + self.anchura)

class Triangulo():
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Circunferencia():
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)
    def perimetro(self):
        return 2 * math.pi * self.radio

class Paralelogramo():
    def __init__(self, lado1, lado2, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.lado1 + self.lado2)

class Trapecio():
    def __init__(self, lado, base_mayor, base_menor, altura):
        self.lado = lado
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
    def area(self):
        return ((self.base_mayor + self.base_menor) / 2) * self.altura
    def perimetro(self):
        return self.lado * 2 + self.base_mayor + self.base_menor

class Rombo():
    def __init__(self, lado, diagonal_mayor, diagonal_menor):
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    def perimetro(self):
        return 4 * self.lado

class Romboide():
    def __init__(self, lado1, lado2, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.lado1 + self.lado2)

class PentagonoRegular():
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        apotema = self.lado / (2 * math.tan(math.pi / 5))
        return (5 * self.lado * apotema) / 2
    def perimetro(self):
        return 5 * self.lado

class HexagonoRegular():
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return ((3 * math.sqrt(3)) / 2) * (self.lado ** 2)
    def perimetro(self):
        return 6 * self.lado

class Cubo():
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return 6 * (self.lado ** 2)
    def volumen(self):
        return self.lado ** 3

class PrismaRectangular():
    def __init__(self, longitud, anchura, altura):
        self.longitud = longitud
        self.anchura = anchura
        self.altura = altura
    def area(self):
        return 2 * (self.longitud * self.anchura + self.longitud * self.altura + self.anchura * self.altura)
    def volumen(self):
        return self.longitud * self.anchura * self.altura

class Esfera():
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 4 * math.pi * (self.radio ** 2)
    def volumen(self):
        return (4 / 3) * math.pi * (self.radio ** 3)

class Cilindro():
    def __init__(self, radio_base, altura):
        self.radio_base = radio_base
        self.altura = altura
    def area(self):
        return 2 * math.pi * self.radio_base * (self.radio_base + self.altura)
    def volumen(self):
        return math.pi * (self.radio_base ** 2) * self.altura

class Cono():
    def __init__(self, radio_base, altura):
        self.radio_base = radio_base
        self.altura = altura
    def area(self):
        return math.pi * self.radio_base * (self.radio_base + math.sqrt(self.altura ** 2 + self.radio_base ** 2))
    def volumen(self):
        return (1 / 3) * math.pi * (self.radio_base ** 2) * self.altura

class Piramide():
    def __init__(self, area_base, perimetro_base, longitud_apotema, altura):
        self.area_base = area_base
        self.perimetro_base = perimetro_base
        self.longitud_apotema = longitud_apotema
        self.altura = altura
    def area(self):
        return self.area_base + (self.perimetro_base * self.longitud_apotema) / 2
    def volumen(self):
        return (1 / 3) * self.area_base * self.altura
