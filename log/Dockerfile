# Use uma imagem base, por exemplo, Python
FROM python:3.9-slim

# Copie o script de recebimento de mensagem para dentro do contêiner
COPY receiver.py /receiver.py 

# Especifica o comando para executar o script de recebimento de mensagem
CMD ["python", "-u", "/receiver.py"]
