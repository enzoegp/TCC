#-- Entrada: todos os arquivos txt com resultados
#-- Saída: todos os arquivos txt com resultados arredondados

# prepara o dicionário de path dos dados
pathDict = {}
pathDict[0] = 'data/C. elegans/'
pathDict[1] = 'data/D. melanogaster/'
pathDict[2] = 'data/H. sapiens/'

for pathIndex in range(0,3):
    fileIn = open(pathDict[pathIndex]+'freq-results.txt','r')
    fileOut = open(pathDict[pathIndex]+'rounded-freq-results.txt','w')
    for lines in fileIn:
        # trata a formatação para pegar a sequência
        ls = lines.strip('\n')
        list = ls.split(" ")
        roundedList = []
        for item in list:
            roundedList.append(str(round(float(item),5)))
        result = ' & '.join(roundedList)
        print(result, file=fileOut)
    fileIn.close()
    fileOut.close()
    fileIn = open(pathDict[pathIndex]+'one-results.txt','r')
    fileOut = open(pathDict[pathIndex]+'rounded-one-results.txt','w')
    for lines in fileIn:
        # trata a formatação para pegar a sequência
        ls = lines.strip('\n')
        list = ls.split(" ")
        roundedList = []
        for item in list:
            roundedList.append(str(round(float(item),5)))
        result = ' & '.join(roundedList)
        print(result, file=fileOut)
    fileIn.close()
    fileOut.close()
    for windowSize in range(3,8,2):
        for vectorSize in range(50,151,50):
            fileIn = open(pathDict[pathIndex] + 'word-' + str(windowSize) + '-win-' + str(vectorSize) + '-siz-results.txt','r')
            fileOut = open(pathDict[pathIndex] + 'rounded-word-' + str(windowSize) + '-win-' + str(vectorSize) + '-siz-results.txt','w')
            for lines in fileIn:
                # trata a formatação para pegar a sequência
                ls = lines.strip('\n')
                list = ls.split(" ")
                roundedList = []
                for item in list:
                    roundedList.append(str(round(float(item),5)))
                result = ' & '.join(roundedList)
                print(result, file=fileOut)
            fileIn.close()
            fileOut.close()
    for windowSize in range(3,8,2):
        for vectorSize in range(50,151,50):
            fileIn = open(pathDict[pathIndex] + 'fast-' + str(windowSize) + '-win-' + str(vectorSize) + '-siz-results.txt','r')
            fileOut = open(pathDict[pathIndex] + 'rounded-fast-' + str(windowSize) + '-win-' + str(vectorSize) + '-siz-results.txt','w')
            for lines in fileIn:
                # trata a formatação para pegar a sequência
                ls = lines.strip('\n')
                list = ls.split(" ")
                roundedList = []
                for item in list:
                    roundedList.append(str(round(float(item),5)))
                result = ' & '.join(roundedList)
                print(result, file=fileOut)
            fileIn.close()
            fileOut.close()