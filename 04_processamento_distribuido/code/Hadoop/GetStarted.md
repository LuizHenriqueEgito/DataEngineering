# Hadoop
Escrito em Java
- `HDFS`: Sistema de arquivos;
- `YARN`: Gerenciador de recursos;
- `MapReduce`

link: [Instalação](https://medium.com/@charan.n_22122016/installing-hadoop-on-ubuntu-a-step-by-step-guide-a2f43dfdc4ac)
```bash
# para entrar no hadoop entre no seu usuario
su hadoop  # coloque a senha (seu usuario é o hadoop)
cd hadoop  # entre na pasta hadoop
```

## Inicia (mas inicia o que?)
```bash
start-dfs.sh
```

## Criando uma pasta no HDFS
```bash
hdfs dfs -mkdir /sua_pasta
```

## Verificando as pastas existentes
```bash
hdfs dfs -ls /
```

## Passa um arquivo para o HDFS
```bash
hdfs dfs -put seu_arquivo_que_vai_para_o_hdfs /sua_pasta_criada_no_hdfs/
```

## Sai do safemode
Quando o Hadoop inicia, o NameNode entra em safe mode, que é um estado de apenas leitura. Ele faz isso para garantir que uma porcentagem mínima de blocos de dados esteja disponível nos DataNodes antes de permitir operações de escrita.
Enquanto estiver em safe mode:

Não é possível criar diretórios ou enviar arquivos (-put)

Comandos como -cat também podem falhar se o arquivo ainda não existia
```bash
hdfs dfsadmin -safemode leave  # sai do safemode

hdfs dfsadmin -report  # olha o estado
```

## Comando para entender o que estão fazendo
```bash
hdfs namenode -format

jps
```
O que é um datanodes e o namenodes

NameNode          → Gerencia o sistema de arquivos HDFS
DataNode          → Armazena fisicamente os blocos dos arquivos
SecondaryNameNode → Faz checkpoints do NameNode
Jps               → Apenas mostra os processos Java em execução  
ResourceManager   → Gerencia recursos e decide onde rodar tarefas
NodeManager       → Executa tarefas e monitora recursos locais

O hadoop aceita mesmo arquivos .py?

## Rodando o map reduce
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /logs/sample_logs.txt \
    -output /logs/output \
    -mapper ./mapper.py \
    -reducer ./reducer.py
```

## Apaga uma pasta
```bash
hdfs dfs -rm -r /sua_pasta/seu_arquivo  # hdfs dfs -rm -r /logs/output
```

core-site.xml contém as seguintes informações:
Número da porta usada para instância do Hadoop
Memória alocada para o sistema de arquivos
Limite de memória para armazenar os dados
Tamanho dos buffers de leitura/gravação
```xml
<configuration>
   <property>
      <name>fs.default.name</name>
      <value>hdfs://localhost:9000 </value>
   </property>
</configuration>
```

hdfs-site.xml contém as seguintes informações:
Valor dos dados de replicação
O caminho do namenode
O caminho do datanode dos seus sistemas de arquivos locais (o local onde você deseja armazenar a infra do Hadoop)
```xml
<configuration>

   <property>
      <name>dfs.replication</name>
      <value>1</value>
   </property>
   
   <property>
      <name>dfs.name.dir</name>
      <value>file:///home/hadoop/hadoopinfra/hdfs/namenode</value>
   </property>
   
   <property>
      <name>dfs.data.dir</name>
      <value>file:///home/hadoop/hadoopinfra/hdfs/datanode </value>
   </property>
   
</configuration>
```

yarn-site.xml
Este arquivo é usado para configurar o Yarn no Hadoop. Abra o arquivo Yarn-site.xml e adicione 
as seguintes propriedades entre as tags <configuration> e </configuration>
```xml
<configuration>
   <property>
      <name>yarn.nodemanager.aux-services</name>
      <value>mapreduce_shuffle</value>
   </property>
</configuration>
```

hdfs dfs -ls /output_streaming
-rw-r--r--   1 hadoop hadoop        567 2025-10-06 01:06 /output_streaming/_SUCCESS
_SUCCESS é um arquivo vazio que indica que o job terminou sem erros.

## Pega o resultado
``` bash
hdfs dfs -cat /sua_pasta_output/part-00000
```