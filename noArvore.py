
class Node(object):
    pai = None
    filhoEsquerdo = None
    filhoDireito = None
    letra = None
    frequencia = None
    ehNovo = None
    '''
    Definição do construtor do nó
    '''
    def __init__(self, letra, frequencia):
        self.letra = letra
        self.frequencia = frequencia

    def setPai(self, pai):
        self.pai = None

    def ehFolha(self):
        if(self.filhoEsquerdo == None and self.filhoDireito == None):
            return True

        return False

    '''
    Método responsável por retornar o nó a ser mostrado na tela
    '''
    def toString(self):
        return ("Nó[ letra = {0} | frequência = {1} ]".format(self.letra, self.frequencia))
