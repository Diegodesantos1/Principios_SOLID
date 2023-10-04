from matriz import Matriz
class Transpuesta:
    def __init__(self, matriz: Matriz):
        self.matriz = matriz
    
    def calcular_transpuesta(self):
        return Matriz([[fila[i] for fila in self.matriz.elementos] for i in range(len(self.matriz.elementos[0]))])