from matriz import Matriz
class Imprimir:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
    
    def imprimir(self):
        for fila in self.matriz.elementos:
            print(fila)