# Data Lake & Data Lakehouse
## Data Lake (Lago de Dados)
- É um repositório de dados **brutos**. Ele aceita **qualquer** tipo de dado:
    - `Estruturado`;
    - `Semi-estruturado`;
    - `Não estruturados`.
    Por exemplo: *logs, JSON, CSV, imagens, vídeos, etc...*
    - Escalável, geralmente em S3, HDFS, ADLS (são serviços de armazenamento para guardar todos esses dados).

### Dados Estruturados, Semi-Estruturados e Não Estruturados
- **Estruturados**: Dados organizados em tabelas com colunas e tipos fixos (por exemplo: SQL, planilhas);
- **Semi-Estruturados**: Dados com alguma organização, mas sem `esquema` fixo (por exemplo: JSON, XML, CSV);
- **Não Estruturados**: Dados sem organização definida (por exemplo: textos, imagens, vídeos, áudios.)

### Schemas
- **Schema (esquema)** é a estrutura definida para organizar os dados, define bem nomes das colunas, tipos de dados (inteiro, texto, data, etc).

## Data LakeHouse
É uma **evolução** do Data Lake. Ele combina o melhor do **Data Lake** (aceita qualquer tipo de dado) com o melhor do **Data Warehouse** (ótimo com dados estruturados para realização de consultas rápidas mas pouco flexivel, só aceita dados tabulares).
- Mantém os **dados brutos** do Data Lake;
- Permite consultas SQL estruturadas de forma eficiente;
- Suporta transações `ACID`, versionamento de dados e controle de schema;
- Ferramentas: **DataBricks**, **Snowflake**, **Iceberg**, **Apache Delta Lake**, **S3 + Athena**;
- Permite `ETL (extração, transformação e carregamento (Extract, Transform Load))` + **Analytics** na mesma camada, sem precisar mover dados para um `warehouse` separado

### Em Resumo
**Data LakeHouse** é um **Data Lake** *arrumado*, onde você tem a flexibilidade de armazenar **qualquer** tipo de dado, mas consegue trabalhar com eles de forma eficiente, como se fosse um banco de dados tradicional.
#### Analogia
- **Data Lake**: Depósito de dados *bagunçado*;
- **Data LakeHouse**: Depósito de dados bem *organizado* (você pode consultar).