# Normalização
É o processo de organizar os dados para eliminar redundância e inconsistência. Evita repetir informações.
## Formas Normais
- **1NF**: Dados atomicos, cada celula tem apenas um valor, uma coluna não deve guardar dois valores nela mesma;
- **2NF**: Tabela deve estar em **1NF** e todos os atributos não chave devem depender da chave inteira, não apenas de parte dela.
- **3NF**: Colunas não podem depender de outras colunas, remove dependência transitiva, se A → B e B → C então A → C, dessa forma C depende de B indiretamente, a tabela deve estar em **2NF** e atributos não chave não podem depender de outros atributos não chave.

# Desnormalização
`JOINS` podem ser caros, em sistema `OLAP` usualmente **desnormalizamos** para ganhar performance, mesmo duplicando dados.

### Em Resumo
- **OLTP**: Normalização;
- **OLAP**: Desnormalização