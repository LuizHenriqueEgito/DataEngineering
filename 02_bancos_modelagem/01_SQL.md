# SQL
É uma linguagem `declarativa` você fala o que quer, e não como fazer pois o como fazer o sistema vai encontrar a melhor forma para você. O `Postgre` é um programa **SGBD (Sistema Gerenciador de Banco de Dados)**, escrito principalmente em *C* e *C++*, ganhando controle de memória, alta performance e baixo nível (I/O).

## Onde os Dados Ficam:
Os dados ficam separados assim:
    - Cada Banco de Dados: uma pasta
    - Cada tabela: um arquivo binário
    - Indices: ficam em arquivos separados

## Como os dados são armazenados:
Uma tabela possui vários arquivos divididos em páginas (8KB) cada

## Como uma query funciona:
Uma `query` é um **pedido estruturado** para um banco de dados. O banco de dados faz uma série de verificações na sua query antes de continuar. Para a query ser concluida o banco de dados passa por três etapas:
### 1º Parser
O banco verifica:
- Sintaxe correta?
- Tabela existe?
- Colunas existem?

### 2º Planner
O banco planeja qual a melhor forma de retornar o que lhe foi pedido, chamamos isso de `query plan`.
- Devo usar indice?
- Faço scan completo da tabela?
- Qual ordem devo seguir das operações?

### Executor
Depois do `Parser` e do `Planner` agora ele tem um plano de ações e já validou a lógica da `query` então ele pode seguir para fazer o que lhe foi pedido.