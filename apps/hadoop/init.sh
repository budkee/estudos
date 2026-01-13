# This script sets up a Hadoop environment on a Linux system. DONT RUN IT, THIS SCRIPT ITS FOR EDUCATIONAL PURPOSES ONLY! 

# =========== Installs ===========
# Update system and install Java 11
sudo apt update
sudo apt install openjdk-11-jdk -y
# Install neofetch
sudo apt install neofetch -y

# Download and Install Hadoop
wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
tar -xvzf hadoop-3.3.6.tar.gz
mv hadoop-3.3.6 ~/hadoop

# =========== Set environment variables  in .bashrc ===========
echo "export HADOOP_HOME=~/hadoop" >> ~/.bashrc
echo "export PATH=\$PATH:\$HADOOP_HOME/bin:\$HADOOP_HOME/sbin" >> ~/.bashrc
echo "export HADOOP_CONF_DIR=\$HADOOP_HOME/etc/hadoop" >> ~/.bashrc
echo "export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64" >> ~/.bashrc
# Check if JAVA_HOME is set correctly
cat ~/.bashrc

# Update .bashrc
source ~/.bashrc

# =========== Create a SSH Key Pair ===========
# Create a SSH key pair for Hadoop
ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
# Add the public key to authorized_keys
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
# Set permissions for the SSH key files
chmod 600 ~/.ssh/authorized_keys
# Test SSH connection
ssh localhost


# =========== Configure Hadoop ===========
# configure core-site.xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://localhost:9000</value>
  </property>
</configuration>

# configure hdfs-site.xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>1</value>
  </property>
</configuration>

# configure mapred-site.xml
<configuration>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
  <property>
    <name>yarn.app.mapreduce.am.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ubuntu/hadoop</value>
  </property>

  <property>
    <name>mapreduce.map.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ubuntu/hadoop</value>
  </property>

  <property>
    <name>mapreduce.reduce.env</name>
    <value>HADOOP_MAPRED_HOME=/home/ubuntu/hadoop</value>
  </property>
</configuration>

# configure yarn-site.xml
<configuration>
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
<configuration>

# =========== Initialize HDFS ===========
# Format the HDFS filesystem
hdfs namenode -format
# >> In case of error, run the following command and update the JAVA_HOME path in ~/.bashrc:
update-alternatives --config java

# =========== Start Hadoop Services ===========
start-dfs.sh
start-yarn.sh

# =========== Stop Hadoop Services ===========
stop-dfs.sh
stop-yarn.sh
# Remove the ResourceManager PID file
# rm -f /tmp/hadoop-ubuntu-resourcemanager.pid
rm -f /tmp/hadoop-ubuntu-*.pid

# =========== Check Hadoop Status ===========
ubuntu@hadoop-log-analysis:~$ jps
7619 Jps
7283 DataNode
7495 SecondaryNameNode
7112 NameNode
ubuntu@hadoop-log-analysis:~$ start-yarn.sh
Starting resourcemanager
Starting nodemanagers
ubuntu@hadoop-log-analysis:~$ jps
8243 Jps
7283 DataNode
8069 NodeManager
7495 SecondaryNameNode
7112 NameNode
7722 ResourceManager

# =========== Create the project directory structure ===========
mkdir -p ~/hadoop-log-analysis/input
cd ~/hadoop-log-analysis

# Log ficticious data for testing
echo '127.0.0.1 - - [25/Jun/2025:10:05:23 -0300] "GET /index.html HTTP/1.1" 200 2326' > input/access_log.txt

# Create python files for MapReduce
vi mapper.py
vi reducer.py
# Give permission to the python files
chmod +x mapper.py reducer.py

# =========== Run the MapReduce job ===========
./run.sh
