import matplotlib.pyplot as plt
import numpy as np 

#-- Entrada: todos os arquivos txt com resultados arredondados
#-- Saída: gráficos da curva AUC para todos os arquivos

# prepara o dicionário de path dos dados
pathDict = {}
pathDict[0] = 'data/C. elegans/'
pathDict[1] = 'data/D. melanogaster/'
pathDict[2] = 'data/H. sapiens/'

barWidth = 0.25

for pathIndex in range(0,3):
    # trata as frequências de k-mers
    file = open(pathDict[pathIndex]+'rounded-freq-results.txt','r')
    listAuc = []
    for lines in file:
        # trata a formatação para pegar a sequência
        ls = lines.strip('\n')
        ls = ls.replace(" ","")
        list = ls.split("&")
        listAuc.append(float(list[4]))
    fig = plt.figure(figsize = (10, 5))
    plt.bar(range(1,8), listAuc, color ='red', width = 0.4)
    ax = plt.gca()
    ax.set_ylim([0.6, 1.0])
    plt.xlabel("k")
    plt.ylabel("AUC")
    plt.title("Frequências de k-mers - AUC(k)")
    plt.savefig(pathDict[pathIndex]+"rounded-freq-results.jpg")
    plt.close(fig)
    file.close()
    # trata a representação one-hot
    file = open(pathDict[pathIndex]+'rounded-one-results.txt','r')
    listAuc = []
    for lines in file:
        # trata a formatação para pegar a sequência
        ls = lines.strip('\n')
        ls = ls.replace(" ","")
        list = ls.split("&")
        listAuc.append(float(list[4]))
    fig = plt.figure(figsize = (10, 5))
    plt.bar(range(1,6), listAuc, color ='red', width = 0.4)
    ax = plt.gca()
    ax.set_ylim([0.6, 1.0])
    plt.xlabel("k")
    plt.ylabel("AUC")
    plt.title("Representação one-hot - AUC(k)")
    plt.savefig(pathDict[pathIndex]+"rounded-one-results.jpg")
    plt.close(fig)
    file.close()
    # trata a representação por word2vec
    for windowSize in range(3,8,2):
        file = open(pathDict[pathIndex] + 'rounded-word-' + str(windowSize) + '-win-50-siz-results.txt','r')
        listAuc1 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc1.append(float(list[4]))
        file.close()
        file = open(pathDict[pathIndex] + 'rounded-word-' + str(windowSize) + '-win-100-siz-results.txt','r')
        listAuc2 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc2.append(float(list[4]))
        file.close()
        file = open(pathDict[pathIndex] + 'rounded-word-' + str(windowSize) + '-win-150-siz-results.txt','r')
        listAuc3 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc3.append(float(list[4]))
        file.close()
        fig = plt.figure(figsize = (10, 5))
        br1 = np.arange(len(listAuc1)) 
        br2 = [x + barWidth for x in br1] 
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, listAuc1, color ='r', width = barWidth, edgecolor ='grey', label ='50')
        plt.bar(br2, listAuc2, color ='g', width = barWidth, edgecolor ='grey', label ='100')
        plt.bar(br3, listAuc3, color ='b', width = barWidth, edgecolor ='grey', label ='150')
        ax = plt.gca()
        ax.set_ylim([0.6, 1.0])
        plt.xlabel('k', fontweight ='bold', fontsize = 15) 
        plt.ylabel('AUC', fontweight ='bold', fontsize = 15) 
        plt.xticks([r + barWidth for r in range(len(listAuc1))], range(1,8))
        plt.legend()
        plt.title("Representação por Word2Vec com janela = " + str(windowSize) + " - AUC(k)")
        plt.savefig(pathDict[pathIndex]+"rounded-word-" + str(windowSize) + "-win-results.jpg")
        plt.close(fig)
    # trata a representação por fasttext
    for windowSize in range(3,8,2):
        file = open(pathDict[pathIndex] + 'rounded-fast-' + str(windowSize) + '-win-50-siz-results.txt','r')
        listAuc1 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc1.append(float(list[4]))
        file.close()
        file = open(pathDict[pathIndex] + 'rounded-fast-' + str(windowSize) + '-win-100-siz-results.txt','r')
        listAuc2 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc2.append(float(list[4]))
        file.close()
        file = open(pathDict[pathIndex] + 'rounded-fast-' + str(windowSize) + '-win-150-siz-results.txt','r')
        listAuc3 = []
        for lines in file:
            # trata a formatação para pegar a sequência
            ls = lines.strip('\n')
            ls = ls.replace(" ","")
            list = ls.split("&")
            listAuc3.append(float(list[4]))
        file.close()
        fig = plt.figure(figsize = (10, 5))
        br1 = np.arange(len(listAuc1)) 
        br2 = [x + barWidth for x in br1] 
        br3 = [x + barWidth for x in br2]
        plt.bar(br1, listAuc1, color ='r', width = barWidth, edgecolor ='grey', label ='50')
        plt.bar(br2, listAuc2, color ='g', width = barWidth, edgecolor ='grey', label ='100')
        plt.bar(br3, listAuc3, color ='b', width = barWidth, edgecolor ='grey', label ='150')
        ax = plt.gca()
        ax.set_ylim([0.6, 1.0])
        plt.xlabel('k', fontweight ='bold', fontsize = 15)
        plt.ylabel('AUC', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(listAuc1))], range(1,8))
        plt.legend()
        plt.title("Representação por FastText com janela = " + str(windowSize) + " - AUC(k)")
        plt.savefig(pathDict[pathIndex]+"rounded-fast-" + str(windowSize) + "-win-results.jpg")
        plt.close(fig)