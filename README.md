# LoLStats-ETL: Um Pipeline de Dados End-to-End da Riot API para Visualização Analítica na AWS
## Visão Geral
LoLStats-Insight é um projeto de dados abrangente que encapsula todo o pipeline de dados, desde a obtenção de dados da [Riot Games API](https://developer.riotgames.com/apis) até a visualização analítica por meio de um painel. O uso de vários serviços da AWS estabelece um fluxo de trabalho de dados de ponta a ponta que é escalável e adaptável a casos de uso semelhantes. Este projeto fornece uma abordagem prática para entender e implementar processos ETL, armazenamento de dados, transformação de dados e visualização em um ambiente em nuvem.

## Arquitetura
- **Coleta de Dados:** Obter dados da Riot Games API.
- **Armazenamento de Dados:** Armazenar dados JSON brutos em Buckets da AWS S3.
- **Catalogação e Transformação de Dados:** Utilizar o AWS Glue para rastrear, catalogar e transformar dados em um formato otimizado para consultas.
- **Consulta de Dados:** Utilizar o AWS Athena para consultar e realizar análises.
- **Visualização de Dados:** Visualizar dados e KPIs em um painel usando o Metabase.

### Diagrama do Pipeline de Dados
Abaixo está um diagrama que ilustra o fluxo de dados no pipeline:

<p align="center">
<img src= "https://cdn.discordapp.com/attachments/712894029284769832/1159153735633739838/Pipeline.png?ex=651ed98a&is=651d880a&hm=764571b521bf1c8b3e944aecbaed094f8317782696b68194125018e82472acc4&" alt="Diagrama do Pipeline de Dados">
</p>

## Pré-requisitos
- Python 3.x
- Conta AWS
- Docker (para configuração local do Metabase)
## Etapas e Componentes
**1. Coleta de Dados com Python**
Um script em Python utiliza requests para buscar dados relacionados aos jogos ranqueados de League of Legends, envolvendo divisões e dados de jogadores, da Riot API. Esses dados, armazenados em formato JSON, são então enviados para os Buckets S3 de maneira hierárquica estruturada para recuperação de dados organizada(Particionamento por Tier e Rank).

**2. AWS Glue para ETL**
O Crawler do AWS Glue é empregado para inferir esquemas e criar tabelas de metadados no Catálogo de Dados do AWS Glue, que se torna consultável via Athena. Além disso, um trabalho de ETL no Glue transforma os dados brutos em um formato otimizado (Parquet) para eficiência de consulta.

**3. Análise de Dados com AWS Athena**
Athena é usado para realizar consultas tipo SQL nos dados transformados, facilitando a análise e geração de insights diretamente dos dados armazenados no S3, sem a necessidade de um banco de dados tradicional.

**4. Visualização com Metabase**
O Metabase, executado localmente usando Docker, é conectado ao Athena, permitindo a criação de painéis para interpretar visualmente os dados e mostrar análises perspicazes.

**Primeiros Passos**
1. **Coleta de Dados:** Utilize ou modifique o script Python fornecido para buscar e armazenar dados da Riot API no S3.
2. **Crawler do Glue:** Configure um Crawler do Glue para criar tabelas de metadados a partir de dados brutos no S3.
3. **Trabalho de ETL do Glue:** Crie um trabalho para transformar os dados brutos em um formato otimizado.
4. **Consulta Athena:** Configure o Athena para consultar dados para análise.
5. **Configuração do Metabase:** Execute o Metabase usando o Docker e conecte-o ao Athena para visualização.
## Executando o Metabase com Docker
Certifique-se de que o Docker está em execução e execute o seguinte:

`docker run -d -p 3000:3000 --name metabase metabase/metabase`

Acesse localhost:3000 no seu navegador para acessar o Metabase.

## Conclusão & Aprendizados
- Adquiri muito conhecimento prático na construção de um pipeline de dados utilizando vários serviços AWS.
- Entendi melhor o processo de gerenciamento e transformação de dados adequados para análise.
- Ganhei insights sobre o manuseio de dados da API, lidando com problemas potenciais, como limitação de taxa e formatação de dados.
- Aprendi sobre otimização de consulta por meio de transformação de dados e como ela impacta os tempos e custos de recuperação de dados.
- Explorei a visualização de dados e a criação de painéis para representar análises de dados de maneira amigável ao usuário.
## Nota
Certifique-se de limpar os serviços AWS (parar trabalhos Glue, excluir dados do S3, etc.) após o uso para gerenciar custos e utilizar eficazmente o Free Tier da AWS.
