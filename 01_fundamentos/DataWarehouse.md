# 🗄️Data Warehouse (OLAP)
- É um sistema de armazenamento de dados projetado para **análises de relatórios**, não para operações do dia a dia (`OLAP - Online Analytical Processing`);
- O Data Warehouse não lida com cada operação individual do dia a dia, mas sim com *resumos e análises* de todas as operações;
- É voltado para decisão estratégica, não para processar cada venda individual (usado em analytics).
- Se o Data Lake é como peças de LEGO soltas, o Data Warehouse é como a construção já pronta, organizada e fácil de consultar.
- Principais ferramentas: Snowflake, Amazon Redshift, Google BigQuery, Microsoft Synapse analytics, Teradata;
- Dados já estruturados e limpos, prontos para análise;
- **Otimizado** para consultas complexas e agregações em grandes volumes de daddos;
- Precisa de **CPU (poder computacional) e RAM (memória)** para consultas rápidas;
- Na maior parde das vezes o **Data Warehouse** recebe dados de Data Lakes após os pipelines ETL/ELT;

### Em Resumo
Repositório Central de dados coletados de diversas fontes, projetado especificamente para **análise e relatórios**. Ele é o alicerce do BI (Business Intelligence). Se com o **Data Lake** nós temos os dados de diversas formas possiveis, no **Data Warehouse** tudo bem transformado e normalizado para serem consumidos, agrupados e visualizados.
