import math

class Calculo(object):

    '''
    Calculo referente a taxa de compressão
    '''
    def taxaDeCompressao(self, entrada, saida):
        self.taxa = len(entrada) / len(saida)
        return self.taxa

    '''
    Calculo referente a probabilidade das letras na palavra que será
    codificada
    '''
    def probabilidade(self, dicionario):
        probMaxima = 0.0
        for i in dicionario:
            probMaxima += dicionario[i]

        return probMaxima

    '''
    Calculo referente a entropia
    '''
    def entropia(self, dicionario):
        soma = 0.0
        for i in dicionario:
            prob = dicionario[i]
            soma += prob * math.log(prob, 2)
        soma *= -1
        return soma

    '''
    Calculo referente ao comprimento médio
    '''
    def comprimentoMedio(self, dicCodigos, dicProb):
        soma = 0.0
        for i in dicProb:
            soma += len(dicCodigos[i]) * dicProb[i]
        return soma

    '''
    Calculo referente a eficiência
    '''
    def eficiencia(self, entropia, comprimento):
        return entropia/comprimento

    '''
    Calculo referente a redundância
    '''
    def redundancia(self, eficiencia):
        return 1 - eficiencia
