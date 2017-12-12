from noArvore import Node
from calculo import Calculo


class HuffmanAdaptativo:

    raiz = None
    codTemporario = ""
    tabelaSaida = []

    def __init__(self, mensagem, codigoInicial):
        self.codInicial = codigoInicial
        self.calc = Calculo()
        self.mensagem = mensagem
        self.letraNaArvore = []
        self.listaNo = []
        self.saidaProxima = []

        #Inicializando o nó NYT (NEW)
        self.nytNode = Node("NYT", 0)
        self.raiz = self.nytNode
        self.listaNo.append(self.nytNode)

    def codificacao(self):
        # resultado = []
        for letra in self.mensagem:
            temp = letra
            self.tabelaSaida.append(self.gerarCod(letra))
            # self.saidaProxima.append(self.pegarCodProximo(temp))
            self.atualizarArvore(temp)

        return self.tabelaSaida


    '''
    Se o código retornado da árvore for vazio, então não há a letra na árvore.
    Será retornado o código do New (NYT) + o código da tabela passada como parâmetro inicial
    '''
    def gerarCod(self, letra):
        resultado = self.pegarCodArvore(self.raiz, letra, "")
        if(resultado == None):
            codNyt = self.pegarCodArvore(self.raiz, "NYT", "")
            if(codNyt == ""):
                self.tabelaSaida.append(self.codInicial["NYT"])
            else:
                self.tabelaSaida.append(codNyt)
            resultado = self.codInicial[letra]

        return resultado

    '''
    A primeira parte do método verifica se o nó é folha, se for, retorna o código gerado
    Se não for folha, será verificado para qual filho a criação do código seguirá.
    Sendo esquerdo é acrescentado 0 ao código, se for direito é acrescentado 1 ao código,
    chamando novamente o método de forma recursiva
    '''
    def pegarCodArvore(self, node, letra, codigo):
        if(node.filhoEsquerdo == None and node.filhoDireito == None):
            if(node.letra != None and node.letra == letra):
                self.codTemporario = codigo
                return codigo
        else:
            if(node.filhoEsquerdo != None):
                retorno = self.pegarCodArvore(node.filhoEsquerdo, letra, codigo + "0")

            if(node.filhoDireito != None and retorno == None): #Se meu retorno for None neste ponto, é porque não encontrou no lado esquerdo
                retorno = self.pegarCodArvore(node.filhoDireito, letra, codigo + "1")

            if (retorno != None):
                return retorno

    def pegarCodProximo(self, letra):
        resultado = self.pegarCodArvore(self.raiz, letra, "")
        if(resultado == ""):
            resultado = self.pegarCodArvore(self.raiz, "NYT", "") +"'" + letra + "'"

        return resultado

    def atualizarArvore(self, letra):
        self.tornarNoAntigo()

        if(not self.noExiste(letra)):
            noInterno = Node(None, 1)
            novoNo = Node(letra, 1)
            novoNo.ehNovo = True
            noInterno.filhoEsquerdo = self.nytNode
            noInterno.filhoDireito = novoNo
            noInterno.pai = self.nytNode.pai

            if(self.nytNode.pai == None):
                self.raiz = noInterno
            else:
                self.nytNode.pai.filhoEsquerdo = noInterno

            self.nytNode.pai = noInterno
            novoNo.pai = noInterno

            self.listaNo.insert(1, noInterno)
            self.listaNo.insert(1, novoNo)
            self.letraNaArvore.append(letra)

            noParaAtualizar = noInterno.pai

        else:
            noParaAtualizar = self.encontrarNo(letra)
            noParaAtualizar.ehNovo = True

        while(noParaAtualizar != None):
            noComp = self.noParaComparar(noParaAtualizar)



            if(noParaAtualizar != noComp and noParaAtualizar.pai != noComp and noParaAtualizar.pai != None):
                self.trocarNode(noParaAtualizar, noComp)

            noParaAtualizar.frequencia = noParaAtualizar.frequencia + 1
            noParaAtualizar = noParaAtualizar.pai

    def trocarNode(self, node1, node2):
        i1 = self.listaNo.index(node1)
        i2 = self.listaNo.index(node2)

        self.listaNo.remove(node1)
        self.listaNo.remove(node2)

        self.listaNo.insert(i1, node2)
        self.listaNo.insert(i2, node1)

        pai1 = node1.pai
        pai2 = node2.pai

        if(pai1 != pai2):
            if(pai1.filhoEsquerdo == node1): #Erro no código, pai 1 não possui filho, ele é None
                pai1.filhoEsquerdo = node2
            else:
                pai1.filhoDireito = node2

            if(pai2.filhoEsquerdo == node2):
                pai2.filhoEsquerdo = node1
            else:
                pai2.filhoDireito = node1
        else:
            pai1.filhoEsquerdo = node2
            pai1.filhoDireito = node1

        node1.pai = pai2
        node2.pai = pai1


    def noParaComparar(self, noAtualizar):

        #if(noComp == noParaAtualizar.filhoEsquerdo or noComp == noParaAtualizar.filhoDireito)
        # aux = None
        for node in self.listaNo:
            aux = node
            if(node.frequencia == noAtualizar.frequencia and node != noAtualizar.filhoEsquerdo and node != noAtualizar.filhoDireito):
                break

        return aux


    def encontrarNo(self, letra):
        for node in self.listaNo:
            if(node != None and node.letra == letra):
                return node
        return None

    def noExiste(self, letra):
        for i in self.letraNaArvore:
            if(letra == i):
                return True
        return False

    def tornarNoAntigo(self):
        self.tornarNoFalso(self.raiz)

    def tornarNoFalso(self, node):
        if(node != None):
            self.tornarNoFalso(node.filhoEsquerdo)
            if(node.ehNovo):
                node.ehNovo = False
                return

            self.tornarNoFalso(node.filhoDireito)