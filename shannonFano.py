from calculo import Calculo

class ShannonFano:

    '''
    Método construtor que recebe a palavra para ser comprimida
    '''
    def __init__(self, palavra):
        self.calc = Calculo()
        self.palavra = palavra

        frequencias = self.definirFrequencias()
        self.dicionarioCodigos = {}
        self.compressao(frequencias)
        self.imprimirCompressao(self.definirFrequencias())


    '''
    Método responsável por comprimir a palavra recebida, que foi transformada em um dicionário
    '''
    def compressao(self, dicionario):
        if(dicionario.__len__() > 1):
            subConjDir = {}

            probabilidade = 0.0
            maxProb = self.calc.probabilidade(dicionario)
            meio = maxProb/2
            while(probabilidade < meio):
                menorChave = min(dicionario, key=dicionario.get)
                if(maxProb > (dicionario[menorChave] + probabilidade)):
                    subConjDir[menorChave] = dicionario.pop(menorChave)
                    probabilidade += subConjDir[menorChave]
                else:
                    probabilidade += dicionario[menorChave]


            for i in dicionario:
                if(self.dicionarioCodigos.__contains__(i)):
                    self.dicionarioCodigos[i] += "0"
                else:
                    self.dicionarioCodigos[i] = "0"


            for i in subConjDir:
                if (self.dicionarioCodigos.__contains__(i)):
                    self.dicionarioCodigos[i] += "1"
                else:
                    self.dicionarioCodigos[i] = "1"

            self.compressao(dicionario)
            self.compressao(subConjDir)

    '''
    Método responsável por verificar a frequência de cada letra
    '''
    def definirFrequencias(self):
        tamPalavra = len(self.palavra)
        dicionario = {}

        for i in self.palavra:
            if(dicionario.__contains__(i)):
                dicionario[i] += 1
            else:
                dicionario[i] = 1

        for i in dicionario:
            dicionario[i] = float(dicionario[i]/tamPalavra)

        return dicionario

    def imprimirCompressao(self, dicionario):
        print('Simbolo \t Probabilidade \t Código')
        for k, v in dicionario.items():
            print('   %s \t\t    %.3f \t\t  %s' % (k, v, self.dicionarioCodigos[k]))

        print('\nPalavra: %s' % self.palavra)
        print('Compressão', end=': ')
        for i in self.palavra:
            print(self.dicionarioCodigos[i], end='')

        entropia = self.calc.entropia(dicionario)
        comprimento = self.calc.comprimentoMedio(self.dicionarioCodigos, dicionario)
        eficiencia = self.calc.eficiencia(entropia, comprimento)
        redundancia = self.calc.redundancia(eficiencia)
        print('\nEntropia: %.2f' % entropia)
        print('Comprimento da palavra: %.2f' % comprimento)
        print('Eficiência: %.2f' % eficiencia)
        print('Redundância: %.2f' % redundancia)
