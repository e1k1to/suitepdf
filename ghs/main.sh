#!/bin/bash

TOKEN="lhama"

usage (){
    echo Função necessita de 3 argumentos, você usou $#
    echo "Opções de resolução: (screen, ebook, printer, prepress, default)"
    echo "uso: $0 input.pdf output.pdf resolução"
    exit 1
}


if [ $# -ne 3 ]; then
    usage
fi

ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$3 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$2 $1

resposta=$?

if [ $resposta -ne 0 ]; then
    echo Erro, código de saída: $resposta
fi

envio="$TOKEN; $(date +'%d-%m-%Y %H-%M-%S'); GhostScript; $resposta"

echo $envio

echo -n "$envio" | nc -q 0 log 12345

return $resposta
