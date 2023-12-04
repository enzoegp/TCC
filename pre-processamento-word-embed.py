from itertools import product
import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors 
import csv

#-- Entrada: txt de label 1 para sequências de k-mers das sequências iniciais
	  # txt de label 0 para sequências de k-mers das sequências iniciais
      # modelos do word2vec para serem usados na obtenção dos vetores junto com os arquivos txt
#-- Saída: csv de labels 0 e 1 com as sequências representadas por word embeddings e o label

# prepara array com nucleotídeos para formar dicionário de frequências de k-mers no futuro
nucleo = ['A','C','G','T']

# prepara o dicionário de path dos dados
pathDict = {}
pathDict[0] = 'data/C. elegans/'
pathDict[1] = 'data/D. melanogaster/'
pathDict[2] = 'data/H. sapiens/'

windowSize = 7
vectorSize = 100

# avalia k-mers de tamanho 1 a 7
for k in range(1,8):
    print('Iniciando processamento para k = ' + str(k) + '.')
    
    for index in range(0,3):
        print('   Iniciando processamento para dataset de index = ' + str(index) + '.')

        # carrega o modelo de word2vec já treinado
        model = Word2Vec.load(pathDict[index]+"model-word-"+str(k)+"-mer-"+str(windowSize)+"-win-"+str(vectorSize)+"-size.model")

        # abre o arquivo no qual escreve as sequências de vetores
        vectorFile = open(pathDict[index]+"word-"+str(k)+"-mer-"+str(windowSize)+"-win-"+str(vectorSize)+"-size.csv",'w')
        csv_writer = csv.writer(vectorFile)
        
        # abre o arquivo de sequências que formam os nucleosomos
        file = open(pathDict[index]+'seq-'+str(k)+'-mer-forming.txt','r')
        corpus1 = []
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            # obtém os k-mers da sequência em ordem
            corpus1 = ls.split(" ")
            listValues = []
            for subseq in corpus1:
                vector = model.wv.get_vector(subseq, norm=True)
                listValues.extend(vector.tolist())
            listValues.append(1)
            # printar linha com label 1
            csv_writer.writerow(listValues)
            corpus1 = []
        file.close()
        
        # abre o arquivo de sequências que inibem os nucleosomos
        file = open(pathDict[index]+'seq-'+str(k)+'-mer-inhibiting.txt','r')
        corpus2 = []
        # lê as linhas do arquivo
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            # obtém os k-mers da sequência em ordem
            corpus2 = ls.split(" ")
            listValues = []
            for subseq in corpus2:
                vector = model.wv.get_vector(subseq, norm=True)
                listValues.extend(vector.tolist())
            listValues.append(0)
            # printar linha com label 1
            csv_writer.writerow(listValues)
            corpus2 = []
        file.close()

        vectorFile.close()

        print('   Processamento para dataset de index = ' + str(index) + ' finalizado.')
        
    print('Processamento para k = ' + str(k) + ' finalizado.\n##############################')