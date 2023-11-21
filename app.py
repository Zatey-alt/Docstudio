from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from werkzeug.utils import secure_filename
from datetime import datetime
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS_DOC = {'pdf', 'doc', 'docx'}
ALLOWED_EXTENSIONS_AUDIO = {'mp3', 'wav'}

def allowed_file(filename, allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
  
        os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def splash():
    return render_template('splash.html')

@app.route('/index')
def index():
    create_upload_folder()
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_info = []

    for file in files:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        date_added = datetime.fromtimestamp(os.path.getctime(file_path))
        file_info.append({'name': file, 'date_added': date_added})


    return render_template('index.html', file_info=file_info)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_DOC.union(ALLOWED_EXTENSIONS_AUDIO)):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index'))

    return redirect(request.url)


@app.route('/search')
def search_files():
    create_upload_folder()
    query = request.args.get('query', '').lower()
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    file_info = []

    for file in files:
        if query in file.lower():
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
            date_added = datetime.fromtimestamp(os.path.getctime(file_path))
            file_info.append({'name': file, 'date_added': date_added})

    return render_template('index.html', file_info=file_info)





@app.route('/open/<filename>')
def open_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(filepath)

@app.route('/delete/<filename>')
def delete_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(filepath):
        os.remove(filepath)
    return redirect(url_for('index'))

# show only documents
@app.route('/show_docs')
def show_docs():
    create_upload_folder()
    doc_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith(('.pdf', '.doc', '.docx'))]
    doc_info = [{'name': file, 'date_added': datetime.fromtimestamp(os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], file)))} for file in doc_files]
    return render_template('docs.html', doc_info=doc_info)

# show only audios
@app.route('/show_audios')
def show_audios():
    create_upload_folder()
    audio_files = [file for file in os.listdir(app.config['UPLOAD_FOLDER']) if file.endswith(('.mp3', '.wav'))]
    audio_info = [{'name': file, 'date_added': datetime.fromtimestamp(os.path.getctime(os.path.join(app.config['UPLOAD_FOLDER'], file)))} for file in audio_files]
    return render_template('audios.html', audio_info=audio_info)



if __name__ == '__main__':
    app.run(debug=True)
