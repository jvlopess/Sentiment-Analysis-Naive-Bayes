# Classificação de Sentimentos em Tweets

## Autores
- Alberto Guevara de Araujo Franca, Centro de Informática, Universidade Federal de Pernambuco, Recife, Brasil. agaf2@cin.ufpe.br
- Felipe Torres de Macedo, Centro de Informática, Universidade Federal de Pernambuco, Recife, Brasil. ftm2@cin.ufpe.br
- João Marcelo de Souza Ferreira, Centro de Informática, Universidade Federal de Pernambuco, Recife, Brasil. jmsf3@cin.ufpe.br
- João Victor Cardoso Lopes, Centro de Informática, Universidade Federal de Pernambuco, Recife, Brasil. jvcl@cin.ufpe.br
- Victor Pessoa Diniz, Centro de Informática, Universidade Federal de Pernambuco, Recife, Brasil. vpd@cin.ufpe.br

## Resumo
Apresentamos uma proposta de projeto para a disciplina de Estatística e Probabilidade para Computação do Centro de Informática (CIn) da Universidade Federal de Pernambuco (UFPE). Nosso objetivo é explorar a aplicação do modelo Naive Bayes na análise de sentimentos em mensagens curtas, especificamente em tweets. A justificativa para essa abordagem reside na crescente relevância das redes sociais como fonte de informações e opiniões. Nossa metodologia envolve a coleta de dados de tweets, pré-processamento textual, treinamento do modelo Naive Bayes e avaliação de sua eficácia na classificação de sentimentos. O cronograma detalhado inclui etapas como aquisição de dados, implementação do modelo e redação do relatório final. As referências utilizadas abrangem trabalhos relacionados a processamento de linguagem natural, classificação de sentimentos e o próprio método Naive Bayes.

## Objetivos
Neste projeto, nosso foco principal é explorar a aplicação do modelo Naive Bayes na análise de sentimentos em tweets. Para atingir esse objetivo, delineamos as seguintes etapas:
1. Investigar detalhadamente o funcionamento e os princípios subjacentes ao modelo Naive Bayes.
2. Realizar o pré-processamento dos tweets coletados do dataset Sentiment140.
3. Treinar o modelo Naive Bayes com os dados processados.
4. Avaliar a eficácia do modelo utilizando métricas de desempenho como acurácia, precisão e recall.
5. Analisar os resultados obtidos após a aplicação do modelo para identificar padrões e tendências nos sentimentos expressos pelos usuários.

## Justificativa
A análise de sentimentos em redes sociais, como o Twitter, tornou-se essencial em um cenário em que a comunicação digital desempenha um papel central na disseminação de informações e opiniões. Compreender os sentimentos expressos pelos usuários é fundamental para empresas, pesquisadores e tomadores de decisão. Ao aplicar o modelo Naive Bayes a essa tarefa, buscamos obter resultados valiosos sobre as emoções presentes nos tweets, contribuindo para uma melhor compreensão do comportamento online e possibilitando ações mais informadas.

## Metodologia
### Coleta de Dados
A etapa inicial consiste na coleta de dados contendo tweets previamente rotulados como positivos, negativos ou neutros. Utilizaremos conjuntos de dados disponíveis publicamente, como o Sentiment140.

### Anotação de Dados
Os tweets coletados passarão por um processo de anotação, que pode ser realizado manualmente ou com base em conjuntos de dados previamente rotulados. As categorias de anotação adotadas serão: Positivo, Neutro e Negativo.

### Pré-processamento de Dados
1. Remoção de stop words
2. Tokenização
3. Normalização
4. Remoção de pontuação e links
5. Stemming e lemmatização

### Treinamento do Modelo Naive Bayes
O modelo Naive Bayes será treinado utilizando a biblioteca scikit-learn. A abordagem Multinomial Naive Bayes é geralmente adequada para dados textuais.

### Avaliação do Modelo
Para determinar o desempenho do classificador, utilizaremos métricas como acurácia, precisão, recall e F1-Score.

## Resultados Esperados
Esperamos que o modelo Naive Bayes apresente resultados promissores na classificação de sentimentos em tweets. A análise de sentimentos pode ser aplicada em diversos contextos, como monitoramento da percepção pública de marcas, eventos esportivos, eleições e crises de saúde pública.
