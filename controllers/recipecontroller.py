from flask import (Flask, render_template, session)
import connexion

app = connexion.App(__name__, specification_dir='../openapi/')
app.add_api('swagger.yml')

#app.secret_key = '?\x91\xa7\x11\x0b\xb9.\x1e\x05n\x05\xa8\xb4\xab\xee6\xa2\x1e?\x96\xae\xe1\xedB'
version = "0.0.1"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ingredients')
def ingredients():
    return render_template('ingredients.html')


@app.route('/nouvelleRecette')
def new_recipe():
    return render_template('ajoutRecette.html')


@app.route('/recette/<id_recipe>')
def page_recipe(id_recipe):
    print(id_recipe)
    return render_template('pageRecipe.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
