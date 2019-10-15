from tabuleiro import Tabuleiro
# Quebra Cabeça 8 peças
class Puzzle:
    def __init__(self, posicoes, objetivo):
        self.posicoes = posicoes
        self.objetivo = objetivo
        self.tabuleiro = Tabuleiro(posicoes, self.objetivo)
        print("tabuleiro inicial")
        self.tabuleiro.printTabuleiro()
        self.algoritimoA()
        print("tabuleiro final")
        self.tabuleiro.printTabuleiro()

    def algoritimoA(self):
        visitados = []
        paraVisitar = []
        paraVisitar.append(self.tabuleiro)
        while paraVisitar[0].corretos != 9:

            print("no atual: ")
            paraVisitar[0].printTabuleiro()
            print("Qtd corretos: " + str(paraVisitar[0].corretos))

            folhas = paraVisitar[0].mover()
            for folha in folhas:
                if folha not in map(self.arrTabuleiro, visitados) and folha not in map(self.arrTabuleiro, paraVisitar):
                    paraVisitar.append(Tabuleiro(folha, self.objetivo))

            visitados.append(paraVisitar[0])
            paraVisitar.remove(paraVisitar[0])
            paraVisitar.sort(key = self.getCorretos, reverse = True)
        
        self.tabuleiro = paraVisitar[0]

    def getCorretos(self, e):
        return e.corretos
    def arrTabuleiro(self, e):
        return e.tabuleiro

def main():
    # Inicializa e resolve o quebra cabeça
    Puzzle([[5, 1, 2], [3, 4, 0], [6, 7, 8]], [[0, 1, 2], [3, 4, 5], [6, 7, 8]])

if __name__ == "__main__":
    # execute only if run as a script
    main()