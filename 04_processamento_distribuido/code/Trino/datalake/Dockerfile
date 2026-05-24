FROM eclipse-temurin:8-jre

WORKDIR /opt

ENV HADOOP_VERSION=3.2.0
ENV METASTORE_VERSION=3.0.0

RUN apt-get update && apt-get install -y netcat-openbsd curl

COPY deps/ /tmp/deps/

ENV HADOOP_HOME=/opt/hadoop-${HADOOP_VERSION}
ENV HIVE_HOME=/opt/apache-hive-metastore-${METASTORE_VERSION}-bin

RUN cd /opt && \
    tar -xzf /tmp/deps/hive-standalone-metastore-3.0.0-bin.tar.gz && \
    tar -xzf /tmp/deps/hadoop-3.2.0.tar.gz && \
    tar -xzf /tmp/deps/mysql-connector-java-8.0.19.tar.gz && \
    cp /tmp/deps/postgresql-42.4.0.jar ${HIVE_HOME}/lib/ && \
    cp /tmp/deps/hive-exec-3.0.0.jar ${HIVE_HOME}/lib/ && \
    cp mysql-connector-java-8.0.19/mysql-connector-java-8.0.19.jar ${HIVE_HOME}/lib/ && \
    rm -rf /tmp/deps

COPY scripts/entrypoint.sh /entrypoint.sh
# COPY ./hive-exec-3.0.0.jar ${HIVE_HOME}/lib/


RUN groupadd -r hive --gid=1001 && \
    useradd -r -g hive --uid=1001 -d ${HIVE_HOME} hive && \
    chown hive:hive -R ${HIVE_HOME} && \
    chown hive:hive /entrypoint.sh && \
    chmod +x /entrypoint.sh        # ← garante execute explicitamente

USER hive
EXPOSE 9083

ENTRYPOINT ["/entrypoint.sh"]