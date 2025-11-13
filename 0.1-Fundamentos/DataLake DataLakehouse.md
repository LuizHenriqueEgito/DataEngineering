# Data Lake & Data Lakehouse
## 🏞️Data Lake (Lago de Dados):
- É um repositório de dados **brutos**. Ele aceita **qualquer** tipo de dado:
    - `Estruturado`;
    - `Semi-estruturado`;
    - `Não estruturados`.
    Por exemplo: *logs, JSON, CSV, imagens, vídeos, etc...*
    - Escalável, geralmente em S3, HDFS, ADLS (são serviços de armazenamento para guardar todos esses dados).

    <div style="background-color: #f4f4f4; color: #333; padding: 10px; border-left: 5px solid #3498db; border-radius: 3px; margin: 10px 0;">

    **🎲 Tipos de Dados:**
    O que são dados **Estruturados**, **Semi-Estruturados** e **Não estruturados**?

    - **Estruturados**: Dados organizados em tabelas com colunas e tipos fixos (por exemplo: SQL, planilhas);
    - **Semi-Estruturados**: Dados com alguma organização, mas sem `esquema` fixo (por exemplo: JSON, XML, CSV);
    - **Não Estruturados**: Dados sem organização definida (por exemplo: textos, imagens, vídeos, áudios.)
    </div>

    <div style="background-color: #f4f4f4; color: #333; padding: 10px; border-left: 5px solid #3498db; border-radius: 3px; margin: 10px 0;">

    **🗂️ Schema (Esquema):**
    **Schema (esquema)** é a estrutura definida para organizar os dados, define bem nomes das colunas, tipos de dados (inteiro, texto, data, etc)

    <div style="background-color: #d4edda; color: #155724; padding: 10px; border-left: 5px solid #28a745; border-radius: 3px; margin: 10px 0;">
        <strong>💡 Analogia:</strong><br>
        O esquema é como um formulário que você preenche: define quais campos existem e que tipo de informação cada campo aceita.  
        Dados estruturados seguem o formulário à risca, semi-estruturados têm alguma organização, e dados não estruturados são como mensagens ou fotos sem modelo definido.
    </div>
    </div>

## 🏞️🏡Data Lakehouse 
- É uma **evolução** do Data Lake. Ele combina o melhor do **Data Lake** com o melhor do `Data Warehouse`.
    - Mantém os **dados brutos** do Data Lake;
    - Permite consultas SQL estruturadas de forma eficiente;
    - Suporta transações `ACID`, versionamento de dados e controle de schema;
    - Ferramentas: **DataBricks**, **Snowflake**, **Iceberg**, **Apache Delta Lake**;
    - Permite `ETL (extração, transformação e carregamento (Extract, Transform Load))` + **Analytics** na mesma camada, sem precisar mover dados para um `warehouse` separado

    <div style="background-color: #f4f4f4; color: #333; padding: 10px; border-left: 5px solid #3498db; border-radius: 3px; margin: 10px 0;">

    **🗄️ Data Warehouse (Armazem de Dados)**
    Repositório Central de dados coletados de diversas fontes, projetado especificamente para **análise e relatórios**. Ele é o alicerce do BI (Business Intelligence). Se com o **Data Lake** nós temos os dados de diversas formas possiveis, no Data Warehouse tudo bem transformado e normalizado para serem consumidos, agrupados e visualizados.
    
    </div>
---
<div style="background-color: #fdd8b9ff; color: #000000; padding: 10px; border-left: 5px solid #ee6237ff; border-radius: 3px; margin: 10px 0;">
  <strong>📌 Resumo:</strong><br>
  Data Lakehouse é um Data Lake "arrumado", onde você tem a flexibilidade de armazenar qualquer tipo de dado, mas consegue trabalhar com eles de forma eficiente, como se fosse um banco de dados tradicional.

  <div style="background-color: #d4edda; color: #155724; padding: 10px; border-left: 5px solid #28a745; border-radius: 3px; margin: 10px 10px 0 0;">
    <strong>💡 Analogia:</strong><br>
    <strong>Data Lake:</strong> Depósito de dados "bagunçado";<br>
    <strong>Data Lakehouse:</strong> Depósito de dados bem organizado.
  </div>
</div>

