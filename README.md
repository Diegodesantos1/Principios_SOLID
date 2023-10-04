<h1 align="center">Principios SOLID</h1>

En este [repositorio](https://github.com/Diegodesantos1/Principios_SOLID) quedan resuelta la práctica de los principios SOLID.

<h2 align="center">Matriz Transpuesta</h2>

El código empleado para resolverlo es el siguiente:

```python
class Matriz:
    def __init__(self, elementos: list):
        self.elementos = elementos

class Transpuesta:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
    
    def calcular_transpuesta(self):
        return Matriz([[fila[i] for fila in self.matriz.elementos] for i in range(len(self.matriz.elementos[0]))])

class Imprimir:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
    
    def imprimir(self):
        for fila in self.matriz.elementos:
            print(fila)

class Lanzador:
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)
        self.transpuesta = Transpuesta(self.matriz)
        self.imprimir = Imprimir(self.matriz)

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Ingrese el elemento {i+1},{j+1}: ")))
            self.elementos.append(fila)

    def lanzar(self):
        print("La matriz es: ")
        self.imprimir.imprimir()
        print("La matriz transpuesta es: ")
        transpuesta_result = self.transpuesta.calcular_transpuesta()
        imprimir_transpuesta = Imprimir(transpuesta_result)
        imprimir_transpuesta.imprimir()

if __name__ == "__main__":
    lanzador = Lanzador()
    lanzador.lanzar()
```
