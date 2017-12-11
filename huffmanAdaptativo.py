from calculo import Calculo

class HuffmanAdaptativo:

    def __init__(self, palavra, codigoInicial):
        self.calc = Calculo()
        self.palavra = palavra
        frequencias = self.definirFrequencias()
        self.dicionarioCodigos = {}
        self.compressao(frequencias)
        self.imprimirCompressao(self.definirFrequencias())

