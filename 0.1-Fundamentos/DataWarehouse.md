# 🗄️Data Warehouse
- É um sistema de armazenamento de dados projetado para análises de relat´roios, não para operações do dia a dia (`OLAP - Online Analytical Processing`);
- O Data Warehouse não lida com cada operação individual do dia a dia, mas sim com *resumos e análises* de todas as operações;
- É voltado para decisão estratégica, não para processar cada venda individual.
    <div style="background-color: #d4edda; color: #155724; padding: 10px; border-left: 5px solid #28a745; border-radius: 3px; margin: 10px 0;">
        <strong>💡 Analogia:</strong><br>
        Se o Data Lake é como peças de 🧱LEGO soltas, o 🏰Data Warehouse é como a construção já pronta, organizada e fácil de consultar.
    </div>
- Principais ferramentas: Snowflake, Amazon Redshift, Google BigQuery, Microsoft Synapse analytics, Teradata;
- Dados já estruturados e limpos, prontos para análise;
- **Otimizado** para consultas complexas e agregações em grandes volumes de daddos;
- Precisa de **CPU (poder computacional) e RAM (memória)** para consultas rápidas;
- Na maior parde das vezes o Data Warehouse recebe dados de Data Lakes após os pipelines ETL/ELT;