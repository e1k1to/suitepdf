#Antes de executar, fazer os builds dos dockers e instalar as dependencias de python

sudo apt install python3-flask

docker build -t ghs ghs/

docker build -t ptt ptt/

docker build -t log log/

docker network create teste

mkdir log/logs/

docker run --rm -v $(pwd)/log/logs:/app -d --net teste --name log log
