# OLTP vs OLAP
## OLTP (Online Transaction Processing)
- Usado para transações do dia a dia (banco de dados de vendas em tempo real);
- Focado na operação: registrar, atualizar, processar agrupamentos;
- inserts/updates/deletes rápidos na tabela

## OLAP (Online Analytical Processing)
- Usado para análise de dados e decisões estratégicas;
- Focado em analítico: relatórios, dashboards, análise de tendências;
- Características:
    - Consultas complexas (joins, agregações)
    - Dados históricos e resumidos
    - Menos atualizações, mais leiturea intensiva
- Por exemplo: Calcular o total de vendas por região nos útlimos 12 meses, gerar ranking de produtos mais vendidos;

### 🛒 OLTP: A loja funcionando no dia a dia
- Cada cliente chegando, comprando produtos, pagando no caixa.
- Tudo precisa ser rápido e confiável.
- Você não está pensando em gráficos ou relatórios, só em registrar cada operação corretamente.

### 📊 OLAP: O escritório de análise da loja
- Analistas revisam os registros de todas as vendas.
- Criam relatórios de tendências, gráficos de vendas mensais, ranking de produtos mais vendidos.
- Voltado para decisões estratégicas, não para processar cada venda individual

#### 💡 Resumo da analogia:
- OLTP = motor do dia a dia (ações rápidas e detalhadas).
- OLAP = escritório de análise (resumos, históricos e decisões estratégicas)./