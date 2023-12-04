from itertools import product
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors 
import csv

#-- Entrada: apenas os dados como no artigo de referência
#-- Saída: csv com labels 1 e 0 para frequências de k-mers das sequências iniciais

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

# avalia k-mers de tamanho 1 a 7
for k in range(1,8):
    print('Iniciando processamento para k = ' + str(k) + '.')
    # gerar vocabulário de todos os k-mers possíveis para este valor de k
    # vocab será usado para inicializar dicionário das frequências de k-mers com valores 0
    vocab = [''.join(seq) for seq in product(nucleo, repeat=k)]
    # print(*vocab)
    # prepara o dicionário das frequências de k-mers com valores 0
    # o dicionário de frequências de k-mers será reinicializado e reusado ao longo dos laços
    freqDict = {}
    for kmer in vocab:
        freqDict[kmer] = 0.0
    # print(freqDict)
    
    for index in range(0,3):
        print('   Iniciando processamento para dataset de index = ' + str(index) + '.')
        # abre o arquivo de sequências que formam os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'f.txt','r')
        freqList = []
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # zera dicionário de frequências de k-mers
            for kmer in vocab:
                freqDict[kmer] = 0.0
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                freqDict[ls[i:i+k]] += 1.0
            # guarda valores de frequências de k-mers em vetor temporário com label 1 no final
            freqListTemp = []
            for key,value in freqDict.items():
                freqListTemp.append(value)
            freqListTemp = freqListTemp / (np.sum(freqListTemp))
            freqListTemp = np.append(freqListTemp,1)
            # guarda vetor temporário de frequências de k-mers e label 1 em matriz de frequências de k-mers com labels
            freqList.append(freqListTemp)
        file.close()
        
        # abre o arquivo de sequências que inibem os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'i.txt','r')
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # zera dicionário de frequências de k-mers
            for kmer in vocab:
                freqDict[kmer] = 0.0
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                freqDict[ls[i:i+k]] += 1.0
            # guarda valores de frequências de k-mers em vetor temporário
            freqListTemp = []
            for key,value in freqDict.items():
                freqListTemp.append(value)
            freqListTemp = freqListTemp / (np.sum(freqListTemp))
            freqListTemp = np.append(freqListTemp,0)
            # guarda vetor temporário de frequências de k-mers e label 0 em matriz de frequências de k-mers com labels
            freqList.append(freqListTemp)
        file.close()

        print('      Imprimindo frequências de k-mers.')
        # printar frequências de k-mers pra csv com os labels 1 e 0
        freqFile = open(pathDict[index]+'freq-'+str(k)+'-mer.csv','w')
        csv_writer = csv.writer(freqFile)
        for i in range(len(freqList)):
            csv_writer.writerow(freqList[i].tolist())
        freqFile.close()

        print('   Processamento para dataset de index = ' + str(index) + ' finalizado.')
        
    print('Processamento para k = ' + str(k) + ' finalizado.\n##############################')
# após o termino da execução, rodar o outro arquivo de processamento para gerar os vetores word2vec para as sequências em si