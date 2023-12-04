from itertools import product
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors 
import csv

#-- Entrada: apenas os dados como no artigo de referência
#-- Saída: csv com labels 1 e 0 para representação oneHot das sequências iniciais

# prepara array com nucleotídeos para formar dicionário de frequências de k-mers no futuro
nucleo = ['A','C','G','T']

# prepara o dicionário de path dos dados
pathDict = {}
pathDict[0] = 'data/C. elegans/'
pathDict[1] = 'data/D. melanogaster/'
pathDict[2] = 'data/H. sapiens/'
# prepara o dicionário de path dos arquivos acessados
fileDict = {}
fileDict[0] = 'C. elegans n-'
fileDict[1] = 'D.m n-'
fileDict[2] = 'human n-'

# avalia k-mers de tamanho 1 a 5
for k in range(1,6):
    print('Iniciando processamento para k = ' + str(k) + '.')
    # gerar vocabulário de todos os k-mers possíveis para este valor de k
    # vocab será usado para inicializar dicionário das frequências de k-mers com valores 0
    vocab = [''.join(seq) for seq in product(nucleo, repeat=k)]
    # print(*vocab)
    
    for index in range(0,3):
        print('   Iniciando processamento para dataset de index = ' + str(index) + '.')

        # abre o arquivo no qual escreve as sequências de vetores
        oneHotFile = open(pathDict[index]+'one-'+str(k)+'-mer.csv','w')
        csv_writer = csv.writer(oneHotFile)
        
        # abre o arquivo de sequências que formam os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'f.txt','r')
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # zera lista de oneHot
            oneHotList = []
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                # zera a representação oneHot
                oneHot = np.zeros(len(vocab))
                oneHot[vocab.index(ls[i:i+k])] = 1.0
                oneHotList.extend(oneHot)
            # guarda vetor oneHot em matriz de oneHot com label 1 no final
            oneHotList.append(1)
            csv_writer.writerow(oneHotList)
        file.close()
        
        # abre o arquivo de sequências que inibem os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'i.txt','r')
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # zera lista de oneHot
            oneHotList = []
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                # zera a representação oneHot
                oneHot = np.zeros(len(vocab))
                oneHot[vocab.index(ls[i:i+k])] = 1.0
                oneHotList.extend(oneHot)
            # guarda vetor oneHot em matriz de oneHot com label 0 no final
            oneHotList.append(0)
            csv_writer.writerow(oneHotList)
        file.close()

        oneHotFile.close()

        print('   Processamento para dataset de index = ' + str(index) + ' finalizado.')
        
    print('Processamento para k = ' + str(k) + ' finalizado.\n##############################')
# após o termino da execução, rodar o outro arquivo de processamento para gerar os vetores word2vec para as sequências em si