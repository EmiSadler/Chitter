import os
from lib.peep_repository import PeepRepository
from lib.database_connection import get_flask_database_connection
from lib.peep import Peep
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/Chitter', methods = ['GET'])
def get_peeps():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    return render_template('index.html', peeps=peeps)

@app.route('/Chitter', methods = ['POST'])
def create_peep():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    content = request.form['content']
    repository.create(content)
    # peeps = repository.all()
    # return render_template('index.html', peeps=peeps)
    return redirect(url_for('get_peeps'))

@app.route('/Chitter/<int:peep_id>', methods = ['POST'])
def delete_peep(peep_id):
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    repository.delete(peep_id)
    return redirect(url_for('get_peeps'))

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

