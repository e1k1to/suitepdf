#!/bin/bash

usage (){
    echo Função necessita de 1 argumentos, você usou $#
    echo "uso: $0 input.pdf"
    exit 1
}


if [ $# -ne 1 ]; then
    usage
fi

pdftotext $1

resposta=$?

if [ $resposta -ne 0 ]; then
    echo Erro, código de saída: $resposta
fi

envio="$(date +'%d-%m-%Y %H-%M-%S'); PDFtoTXT; $resposta"

echo $envio

echo -n "$envio" | nc -q 0 log 12345

return $resposta


