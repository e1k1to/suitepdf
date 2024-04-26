#Antes de executar, fazer os builds dos dockers e instalar as dependencias de python

pip install flask

docker build -t ghs ghs/

docker build -t ptt ptt/
