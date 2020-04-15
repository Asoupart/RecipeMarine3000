import connexion
import os
from flask import (render_template, request, jsonify)
from werkzeug.utils import secure_filename

app = connexion.App(__name__, specification_dir='../openapi/')
UPLOAD_FOLDER = 'E:/Code/RecipeMarine3000/controllers/images/'
app.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.add_api('swagger.yml')

# app.secret_key = '?\x91\xa7\x11\x0b\xb9.\x1e\x05n\x05\xa8\xb4\xab\xee6\xa2\x1e?\x96\xae\xe1\xedB'
version = "0.0.1"

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#@app.route('/')
#def home():
#    return render_template('home.html')


#@app.route('/ingredients')
#def ingredients():
#    return render_template('gestion.html')


#@app.route('/nouvelleRecette')
#def new_recipe():
#    return render_template('ajoutRecette.html')


#@app.route('/recette/<id_recipe>')
#def page_recipe(id_recipe):
#    return render_template('pageRecipe.html')


@app.route('/ajout/python-flask-files-upload', methods=['POST'])
def upload_file():
    if 'files[]' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp

    files = request.files.getlist('files[]')
    errors = {}
    success = False

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.app.config['UPLOAD_FOLDER'], filename))
            success = True
        else:
            errors[file.filename] = 'File type not allowed'

    if success and errors:
        errors['message'] = 'File successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 206
        return resp
    if success:
        resp = jsonify({'message': 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
