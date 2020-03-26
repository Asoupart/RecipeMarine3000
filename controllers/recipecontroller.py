from flask import (Flask, render_template)
import connexion

app = connexion.App(__name__, specification_dir='../openapi/')
app.add_api('swagger.yml')

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
