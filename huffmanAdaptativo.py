from noArvore import Node
from calculo import Calculo


class HuffmanAdaptativo:

    def __init__(self, mensagem, codigoInicial):
        self.raiz = None
        self.tabelaLetra = []
        self.tabelaSaida = []
        self.codInicial = codigoInicial
        self.calc = Calculo()
        self.mensagem = mensagem
        self.letraNaArvore = []
        self.listaNo = []
        self.msgCodificada = ""

        #Inicializando o nó NYT (NEW)
        self.nytNode = Node("NYT", 0)
        self.raiz = self.nytNode
        self.listaNo.append(self.nytNode)

    def codificacao(self):
        for letra in self.mensagem:
            temp = letra
            resultado = self.gerarCod(letra)
            self.msgCodificada += resultado
            self.tabelaSaida.append(resultado)
            self.tabelaLetra.append(letra)
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
                self.msgCodificada += self.codInicial["NYT"]
                self.tabelaSaida.append(self.codInicial["NYT"])
                self.tabelaLetra.append("NEW")
            else:
                self.msgCodificada += codNyt
                self.tabelaSaida.append(codNyt)
                self.tabelaLetra.append("NEW")
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
                return codigo
        else:
            if(node.filhoEsquerdo != None):
                retorno = self.pegarCodArvore(node.filhoEsquerdo, letra, codigo + "0")

            if(node.filhoDireito != None and retorno == None): #Se meu retorno for None neste ponto, é porque não encontrou no lado esquerdo
                retorno = self.pegarCodArvore(node.filhoDireito, letra, codigo + "1")

            if (retorno != None):
                return retorno

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
            noParaAtualizar.frequencia = noParaAtualizar.frequencia + 1
            noParaAtualizar = noParaAtualizar.pai
            self.verificaTroca()

    def verificaTroca(self):
        if(self.letraNaArvore.__len__() < 2):
            return

        # Primeira verificação: troca das folhas
        for i in range(1, self.listaNo.__len__()-1):
            atual = self.listaNo[i]
            j = i + 1
            proximo = self.listaNo[j]
            while not(atual.ehFolha() and proximo.ehFolha()):
                if not(atual.ehFolha()):
                    atual = self.listaNo[i+1]

                if not(proximo.ehFolha()):
                    if ((j+1) > (self.listaNo.__len__()-1)):
                        break

                    proximo = self.listaNo[j+1]

            if(atual.frequencia > proximo.frequencia):
                self.trocarNode(atual, proximo)

        # Erro ao utilizar o código de verificação horizontal
        # self.verificaTrocaHorizontal()
        # Segunda verificação: troca dos nós internos com as folhas
        # for node in self.listaNo:
        #     if not(node.ehFolha()):
        #         filhoEsquerdo = node.filhoEsquerdo
        #         filhoDireito = node.filhoDireito
        #         if(filhoEsquerdo.frequencia > filhoDireito.frequencia):
        #             self.trocarNode(filhoEsquerdo, filhoDireito)


        return

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
        self.refatorarArvore()

    def verificaTrocaHorizontal(self):
        self.percursoPosOrdemTroca(self.raiz)

    def percursoPosOrdemTroca(self, node):
        if (node != None):
            valor1 = self.percursoPosOrdemTroca(node.filhoEsquerdo)
            valor2 = self.percursoPosOrdemTroca(node.filhoDireito)
            if(valor1 != None and valor2 != None):
                if (valor1 > valor2):
                    self.trocarNode(node.filhoEsquerdo, node.filhoDireito)
            return self.visit(node)


    def refatorarArvore(self):
        self.percursoPosOrdemRefatorar(self.raiz)

    def percursoPosOrdemRefatorar(self, node):
        if (node != None):
            valor1 = self.percursoPosOrdemRefatorar(node.filhoEsquerdo)
            valor2 = self.percursoPosOrdemRefatorar(node.filhoDireito)
            if (valor1 != None and valor2 != None):
                node.frequencia = valor1 + valor2
            return self.visit(node)

    def visit(self, node):
        return node.frequencia


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

    def imprimirCompressao(self):
        print('Simbolo \t Código')
        for k, v in self.tabelaSaida, self.tabelaLetra:
            print('   %s \t\t    %s' % (k, v))

        print('\nMensagem: %s' % self.mensagem)
        print('Compressão: '.format(self.msgCodificada))

        bits = self.codInicial.items()
        txComp = self.calc.taxaDeCompressao(self.mensagem, len(bits[1][0]), self.msgCodificada)
        print('Taxa de compressão: %.2f' % txComp)
