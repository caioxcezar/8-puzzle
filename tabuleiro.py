class Tabuleiro:
    def __init__(self, tabuleiro, objetivo):
        self.tabuleiro = tabuleiro
        self.checkTabuleiro()
        self.corretos = self.checarCorretos(objetivo)

    def checkTabuleiro(self):
        tabuleiro = []

        qtdLinhas = 0
        qtdElementos = 0
        for linhas in self.tabuleiro:
            qtdLinhas += 1
            qtdElementos += len(linhas)

        if qtdLinhas != 3 and qtdElementos != 9:
            raise Exception("insira as 9 posicoes corretamente")
        elif self.checarRepetidos():
            raise Exception("numero de casas reperido")
        elif self.checarZero() == False:
            raise Exception("informe a casa vazia com um zero")
        return tabuleiro

    # True para numeros repetidos
    def checarRepetidos(self):
        tabAux = []
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento in tabAux:
                    return True
                tabAux.append(tabAux)
        return False
    
    # True quando encontra um unico zero
    def checarZero(self):
        qtdZeros = 0
        for linha in self.tabuleiro:
            qtdZeros += linha.count(0)
        if qtdZeros == 1:
            return True
        return False

    def printTabuleiro(self):
        output = " ------ \n"
        for linha in self.tabuleiro:
            output += "|"
            for campo in linha:
                output += str(campo) + " "
            output += "|\n"
        print(output + " ------ ")

    def mover(self):
        estados = []
        posicaoZero = self.getPosicaoZero()
        cima = [posicaoZero[0] - 1, posicaoZero[1]]
        baixo = [posicaoZero[0] + 1, posicaoZero[1]]
        direita = [posicaoZero[0], posicaoZero[1] + 1]
        esquerda = [posicaoZero[0], posicaoZero[1] - 1]
        if cima[0] >= 0:
            estados.append(self.troca(posicaoZero, cima))
        if baixo[0] <= 2:
            estados.append(self.troca(posicaoZero, baixo))
        if direita[1] <= 2:
            estados.append(self.troca(posicaoZero, direita))
        if esquerda[1] >= 0:
            estados.append(self.troca(posicaoZero, esquerda))
        return estados

    def getPosicaoZero(self):
        for lin in range(len(self.tabuleiro)):
            for col in range(len(self.tabuleiro[lin])):
                if self.tabuleiro[lin][col] == 0:
                    return [lin, col]
        raise Exception("zero não encontrado")

    def troca(self, pos1, pos2):
        arrTabuleiro = []
        for linha in self.tabuleiro:
            arrTabuleiro.append(linha.copy())

        valor1 = arrTabuleiro[pos1[0]][pos1[1]]
        valor2 = arrTabuleiro[pos2[0]][pos2[1]]

        arrTabuleiro[pos1[0]][pos1[1]] = valor2
        arrTabuleiro[pos2[0]][pos2[1]] = valor1

        return arrTabuleiro

    def checarCorretos(self, objetivo):
        posicoesCorreta = 0

        for lin in range(len(objetivo)):
            for col in range(len(objetivo[lin])):
                if objetivo[lin][col] == self.tabuleiro[lin][col]:
                    posicoesCorreta += 1

        return posicoesCorreta