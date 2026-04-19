# 1º Instale o Java
```bash
# Atualize os repositórios
sudo apt update

# Instale o OpenJDK 8 ou 11
sudo apt install openjdk-11-jdk -y

# Verifique a instalação
java -version
```

# 2º Crie o usuário para o Hadoop
``` bash
sudo adduser hadoop
sudo usermod -aG sudo hadoop
su - hadoop
```

# 3º Configure o SSH
``` bash
# Instale o SSH
sudo apt install openssh-server openssh-client -y

# Gere as chaves SSH
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa

# Adicione a chave pública ao authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 640 ~/.ssh/authorized_keys

# Teste a conexão SSH
ssh localhost
# Digite 'yes' e depois saia com 'exit'
```

# 4º Instale o Hadoop
``` bash
# Baixe o Hadoop (versão 3.3.6 - mais recente estável)
cd ~
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz

# Extraia o arquivo
tar -xzvf hadoop-3.3.6.tar.gz

# Mova para /usr/local
sudo mv hadoop-3.3.6 /usr/local/hadoop

# Dê permissões ao usuário
sudo chown -R $USER:$USER /usr/local/hadoop
```

# 5º Configure as variáveis de ambiente
``` bash
vim ~/.bashrc

# adicione
# Hadoop Environment Variables
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

# Java Environment
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

# saia do arquivo de edição :wq
source ~/.bashrc
```
Vá para o arquivo `hadoop-env.sh`:
```bash
vim $HADOOP_HOME/etc/hadoop/hadoop-env.sh
# adicione
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
export HADOOP_HEAPSIZE=512  # Reduzido para máquinas com pouca memória
```
Vá para o arquivo `core-site.xml`:
```bash
vim $HADOOP_HOME/etc/hadoop/core-site.xml
```
Adicione:
```xml
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/home/hadoop/hadoopdata</value>
    </property>
</configuration>
```
Vá para o arquivo `hdfs-site.xml`:
```bash
vim $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```
Adicione:
```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/hadoop/hadoopdata/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/hadoop/hadoopdata/datanode</value>
    </property>
    <property>
        <name>dfs.blocksize</name>
        <value>67108864</value> <!-- 64MB ao invés de 128MB padrão -->
    </property>
</configuration>
```
Vá para o arquivo `mapred-site.xml`:
``` bash
vim $HADOOP_HOME/etc/hadoop/mapred-site.xml
```
Adicione
```xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
    <property>
        <name>mapreduce.application.classpath</name>
        <value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    </property>
    <!-- Configurações para máquinas com poucos recursos -->
    <property>
        <name>mapreduce.map.memory.mb</name>
        <value>512</value>
    </property>
    <property>
        <name>mapreduce.reduce.memory.mb</name>
        <value>512</value>
    </property>
    <property>
        <name>mapreduce.map.java.opts</name>
        <value>-Xmx400m</value>
    </property>
    <property>
        <name>mapreduce.reduce.java.opts</name>
        <value>-Xmx400m</value>
    </property>
</configuration>
```
Vá para `yarn-site.xml`:
```bash
vim $HADOOP_HOME/etc/hadoop/yarn-site.xml
```
Adicione:
```xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
        <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>localhost</value>
    </property>
    <!-- Configurações para máquinas com poucos recursos -->
    <property>
        <name>yarn.nodemanager.resource.memory-mb</name>
        <value>2048</value> <!-- Ajuste conforme sua RAM disponível -->
    </property>
    <property>
        <name>yarn.scheduler.minimum-allocation-mb</name>
        <value>256</value>
    </property>
    <property>
        <name>yarn.scheduler.maximum-allocation-mb</name>
        <value>2048</value>
    </property>
    <property>
        <name>yarn.nodemanager.resource.cpu-vcores</name>
        <value>2</value> <!-- Ajuste conforme seus cores disponíveis -->
    </property>
</configuration>
```

# 7º Crie os diretórios (namenode & datanode)
```bash
mkdir -p ~/hadoopdata/namenode
mkdir -p ~/hadoopdata/datanode
```

# 8º Formate o NameNode
```bash
hdfs namenode -format
```

# 9º Inicie o Hadoop
```bash
# Inicie o HDFS
start-dfs.sh

# Inicie o YARN
start-yarn.sh

# Verifique os processos em execução
jps
```

# 10º Testando o MapReduce:
```bash
# Copiar um arquivo de exemplo do Hadoop para HDFS
hdfs dfs -mkdir /input
hdfs dfs -put $HADOOP_HOME/etc/hadoop/*.xml /input

# Rodar o exemplo WordCount
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /input /output_wc
```
Veja os resultados:
```bash
hdfs dfs -ls /output_wc
hdfs dfs -cat /output_wc/part-r-00000
```

# 11º Testando com seu próprio Scrip (mapper.py & reducer.py)
Crie uma pasta para seu script:
```bash
mkdir map_reducer
cd map_reducer
```
Crie os arquivos:
`mapper.py`
``` python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(f"{word}\t1")
```
`reducer.py`:
```python
#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

if current_word:
    print(f"{current_word}\t{current_count}")
```
Dê o acesso aos `scripts` criados:
```bash
chmod +x mapper.py reducer.py
```
Crie o seu próprio texto:
```bash
echo -e "Esse é um ato de rebeldia contra esse mundo CRUEL" > input.txt
```
Adicione na pasta de input do `HDFS`:
```bash
hdfs dfs -put -f input.txt /input/
```
Confira o conteúdo no `HDFS`:
```bash
hdfs dfs -ls /input
hdfs dfs -cat /input/input.txt
```
Para rodar na sua pasta `map_reducer` rode:
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input /input -output /output -file mapper.py -file reducer.py -mapper "python3 mapper.py" -reducer "python3 reducer.py"
```
Pegue o resultado:
```bash
hdfs dfs -cat /output/part-00000
```
Apague o resultado para fazer novamente
``` bash
hdfs dfs -rm -r /output
```