# TCC

Este repositório contém os arquivos, datasets e resultados dos experimentos realizados no meu TCC. Todos os arquivos secundários foram deletados, porque eram muitos e ocupavam muito espaço.

Para realizar os experimentos das frequências de k-mers:
pre-processamento-freq.py -> classificador-svm-freq.py

Para realizar os experimentos da representação oneHot:
pre-processamento-one.py -> classificador-svm-one.py

Para realizar os experimentos dos word embeddings do Word2Vec:
pre-processamento-word.py -> pre-processamento-word-embed.py -> classificador-svm-word.py

Para realizar os experimentos dos word embeddings do FastText:
pre-processamento-fast.py -> pre-processamento-fast-embed.py -> classificador-svm-fast.py

Para arredondar os resultados com cinco casas decimais uma vez que todos os arquivos de resultado tenham sido gerados:
arredonda-resultados.py

Para gerar os gráficos uma vez que todos os arquivos de resultado arredondados tenham sido gerados:
gera-graficos.py

Observações:
- Não deletar arquivos secundários (que são vários) durante um dos fluxos de execução, apenas depois
- Ajustar manualmente os tamanhos de janela e de vetor nos arquivos pre-processamento-word-embed.py, classificador-svm-word.py, pre-processamento-fast-embed.py e classificador-svm-fast.py, caso queira todos os resultados
