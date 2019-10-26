from tabuleiro import Tabuleiro
import random
import datetime
import os
# Quebra Cabeça 8 peças
class Puzzle:
    def __init__(self, posicoes, objetivo):
        self.posicoes = posicoes
        self.objetivo = objetivo
        self.tabuleiro = Tabuleiro(posicoes, self.objetivo)
        self.visitados = []
        self.paraVisitar = []
        self.tabuleiroFinal = self.algoritimoA()

    def printBacktrack(self):
        tAnterior = self.tabuleiroFinal.copy()
        caminho = ""
        quebraLinha = 0
        while tAnterior.ponteiro != "":
            posicaoZero = tAnterior.getPosicaoZero()
            mv = []
            caminho += tAnterior.ponteiro
            if quebraLinha == 10:
                caminho += "\n"
                quebraLinha = 0
            else:
                caminho += " "
                quebraLinha += 1
            if tAnterior.ponteiro == "↓":
                mv = [posicaoZero[0] - 1, posicaoZero[1]]
            elif tAnterior.ponteiro == "↑":
                mv = [posicaoZero[0] + 1, posicaoZero[1]]
            elif tAnterior.ponteiro == "←":
                mv = [posicaoZero[0], posicaoZero[1] + 1]
            elif tAnterior.ponteiro == "→":
                mv = [posicaoZero[0], posicaoZero[1] - 1]
            aux = tAnterior.troca(posicaoZero, mv)
            for visitado in self.visitados:
                if visitado.tabuleiro == aux:
                    tAnterior = visitado.copy()
        print(caminho[::-1])

    def algoritimoA(self):
        visitados = self.visitados
        paraVisitar = self.paraVisitar
        paraVisitar.append(self.tabuleiro)
        while paraVisitar[0].corretos != 9:

            print("nó atual: ")
            paraVisitar[0].printTabuleiro()
            print("Qtd corretos: " + str(paraVisitar[0].corretos))
            os.system('cls' if os.name == 'nt' else 'clear')

            folhas = paraVisitar[0].mover()
            for folha in folhas:
                if folha.tabuleiro not in map(lambda e: e.tabuleiro, visitados) and folha not in map(lambda e: e.tabuleiro, paraVisitar):
                    paraVisitar.append(folha)

            visitados.append(paraVisitar[0])
            paraVisitar.remove(paraVisitar[0])
            paraVisitar.sort(key = lambda e: e.corretos, reverse = True)
        
        self.visitados = visitados
        self.paraVisitar = paraVisitar
        return paraVisitar[0]

def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(x)
    padraoBr = "%d/%m/%Y %H:%M:%S"
    horainicio = datetime.datetime.now()
    puzzle = Puzzle([x[0:3], x[3:6], x[6:9]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    horaFinal = datetime.datetime.now()
    print("Tabuleiro inicial: ")
    puzzle.tabuleiro.printTabuleiro()
    print("Caminho: ")
    puzzle.printBacktrack()
    print("Tabuleiro final: ")
    puzzle.tabuleiroFinal.printTabuleiro()
    print("Tempo de inicio: " + str(horainicio.strftime(padraoBr)))
    print("Tempo de conclusão: " + str(horaFinal.strftime(padraoBr)))
    print("Tempo de conclusão: " + str(horaFinal - horainicio))
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
