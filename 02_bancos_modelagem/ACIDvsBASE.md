# ACID x BASE
## ACID
**ACID**: Conjunto de propriedades que garantem `transações confiaveis` em bancos de dados.
- **A**: Atomicity (Atomicidade), ou uma transação acontece no banco de dados ou ela não acontece, se algo falhar o banco desfaz tudo;
- **C**: Consistency (Consistência), após uma transação o banco continua em um estado válido, nenhuma regra do banco deve ser quebrada (por exemplo o saldo de uma pessoa ser sempre maior ou igual a zero mas nunca menor que zero);
- **I**: Isolation (Isolamento), se várias transações acontecem ao mesmo tempo , elas não se interferem;
- **D**: Durability (Durabilidade), depois que a transação foi confirmada (commit) o dado nunca será perdido, mesmo que o servidor caia.
**ACID** prioriza, correção, segurança e consistência.

## BASE
**BASE** surgiu em bancos de dados distribudos e NoSQL.
- **BA**: Basically Available, sistema sempre responde mesmo se alguns dados estiverem inconsistentes;
- **S**: Soft State, o estado do sistema pode mudar ao longo do tempo, mesmo sem novas operações, os dados podem estar sendo replicados ou o sistema pode estar sincronizando.
- **E**: Eventually Consistent, os dados podem ficar temporariamente inconsistentes, mas eventualmente convergem.
Ele abre mão de consistência imediata para ganhar em escalabilidade