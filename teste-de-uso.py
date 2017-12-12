from calculo import Calculo
from shannonFano import ShannonFano
from huffmanAdaptativo import HuffmanAdaptativo

calc = Calculo()

# palavra = input('Informe a palavra a ser comprimida!')

# sf = ShannonFano(palavra)

codInicial = {
    "NYT" : "0",
    "A" : "000",
    "B" : "001",
    "C" : "010"
}

ha = HuffmanAdaptativo("AABBBACC", codInicial)



print(ha.codificacao())

# print("Testando a taxa de compressão")
# a = calc.taxaDeCompressao('100000011111111111010101', '1111111111110')
# print("Taxa de compressão = %.2f" % a)
#
# print("Testando a probabilidade")
# a = {
#     'A' : 0.4,
#     'B' : 0.3,
#     'C' : 0.2,
#     'D' : 0.1
# }
#
# print('%.2f' % calc.probabilidade(a))
#
# print('Entropia')
# print('%.2f' % calc.entropia(a))
#
# print('Comprimento médio')
# print('%.2f' % calc.comprimentoMedio(a, 'AAAABBAACCD'))
#
# print('Eficiencia')
# eficiencia = calc.eficiencia(calc.entropia(a), calc.comprimentoMedio(a, 'AAAABBAACCD'))
# print('%.2f' % eficiencia)
#
# print('redundancia')
# print('%.2f' % calc.redundancia(eficiencia))