from itertools import product
import numpy as np
from gensim.models import FastText
from gensim.models import KeyedVectors 
import csv

#-- Entrada: apenas os dados como no artigo de referência
#-- Saída: txt de label 1 para sequências de k-mers das sequências iniciais
	  # txt de label 0 para sequências de k-mers das sequências iniciais
      # modelos do fasttext para serem usados na obtenção dos vetores junto com os arquivos txt

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
    
    # corpus é usado para treinar o fasttext
    corpus = []
    for index in range(0,3):
        print('   Iniciando processamento para dataset de index = ' + str(index) + '.')
        # abre o arquivo de sequências que formam os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'f.txt','r')
        lineList = []
        corpusTemp = []
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                lineList.append(ls[i:i+k])
            corpus.append(lineList)
            corpusTemp.append(lineList)
            lineList = []
        file.close()
        # printar sequências de k-mers pra txt de label 1
        seqFile = open(pathDict[index]+'seq-'+str(k)+'-mer-forming.txt','w')
        for i in range(len(corpusTemp)):
            print(*corpusTemp[i], file=seqFile)
        seqFile.close()
        
        # abre o arquivo de sequências que inibem os nucleosomos
        file = open(pathDict[index]+fileDict[index]+'i.txt','r')
        lineList = []
        corpusTemp = []
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls[1:]
            # obtém os k-mers da sequência em ordem
            for i in range(0,len(ls)-k+1):
                lineList.append(ls[i:i+k])
            corpus.append(lineList)
            corpusTemp.append(lineList)
            lineList = []
        file.close()
        # printar sequências de k-mers pra txt de label 0
        seqFile = open(pathDict[index]+'seq-'+str(k)+'-mer-inhibiting.txt','w')
        for i in range(len(corpusTemp)):
            print(*corpusTemp[i], file=seqFile)
        seqFile.close()

        # usar corpus pra treinar fasttext
        # itera por tamanhos de janela 3, 5 e 7
        for windowSize in range(3,8,2):
            print('      Iniciando processamento para janela de tamanho = ' + str(windowSize) + '.')
            # itera por tamanhos de embeddings de 50, 100 e 150
            for vectorSize in range(50,151,50):
                print('         Iniciando processamento para vetor de tamanho = ' + str(vectorSize) + '.')
                # usar corpus para treinar fasttext e salva o modelo
                model = FastText(sentences=corpus,min_count=1,vector_size=vectorSize,sg=1,hs=1,window=windowSize)
                model.save(pathDict[index]+"model-fast-"+str(k)+"-mer-"+str(windowSize)+"-win-"+str(vectorSize)+"-size.model")
                
                print('      Processamento para vetor de tamanho = ' + str(vectorSize) + ' finalizado.')
            print('      Processamento para janela de tamanho = ' + str(windowSize) + ' finalizado.')
        
        # zera o corpus para próxima iteração
        corpus = []

        print('   Processamento para dataset de index = ' + str(index) + ' finalizado.')
        
    print('Processamento para k = ' + str(k) + ' finalizado.\n##############################')
# após o termino da execução, rodar o outro arquivo de processamento para gerar os vetores fasttext para as sequências em si