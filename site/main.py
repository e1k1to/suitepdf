import subprocess
import os
from hashlib import sha256 
from flask import Flask, render_template, request, redirect, url_for, send_from_directory


def reduce(nome, nomered, res):
    current_directory = os.getcwd()
    
    docker_command = [
            "docker", "run", "--rm", "-v",
            f"{current_directory}:/app", "--net", "teste", "--name", "ghs",
            "ghs", nome, nomered, res
        ]
    subprocess.run(docker_command, check=True)

def totext(nome):
    current_directory = os.getcwd()
    docker_command = [
            "docker", "run", "--rm", "-v",
            f"{current_directory}:/app", "--net", "teste", "--name", "ptt",
            "ptt", nome
        ]
    subprocess.run(docker_command, check=True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdftotxt')
def pdftotxt():
    return render_template('totext.html')

@app.route('/reduzirpdf')
def reduzpdf():
    return render_template('reduzir.html')

@app.route('/upload_gh', methods=['POST'])
def upload_file_gh():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado!'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Nenhum arquivo selecionado!'
    
    nomeArqSalvar = (sha256(file.filename.encode('utf-8')).hexdigest())[:8] + "-in.pdf"
    nomeArqDevolv = (sha256(file.filename.encode('utf-8')).hexdigest())[:8] + "-out.pdf"

    file.save(nomeArqSalvar)

    reso = request.form.get('res','')

    reduce(nomeArqSalvar, nomeArqDevolv,reso)

    return redirect(url_for('download_file_gh',filename=nomeArqDevolv))


@app.route('/upload_ptt', methods=['POST'])
def upload_file_ptt():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado!'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'Nenhum arquivo selecionado!'
    
    nomeArqSalvar = (sha256(file.filename.encode('utf-8')).hexdigest())[:8] + ".pdf"

    # Aqui você pode salvar o arquivo, processá-lo, etc.
    # Por exemplo, salvar o arquivo na pasta de uploads do Flask
    file.save(nomeArqSalvar)
    
    totext(nomeArqSalvar)
    nomeArqDevolv = (sha256(file.filename.encode('utf-8')).hexdigest())[:8] + ".txt"

    return redirect(url_for('download_file_ptt',filename=nomeArqDevolv))

@app.route('/<filename>')
def download_file_ptt(filename):
    return send_from_directory('', filename, as_attachment=True)

@app.route('/<filename>')
def download_file_gh(filename):
    return send_from_directory('', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
