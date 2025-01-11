import os
from lib.peep_repository import PeepRepository
from lib.peep import Peep
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
repository = PeepRepository()

@app.route('/Chitter', methods = ['GET'])
def get_peeps():
    peeps = repository.all()
    return render_template('index.html', peeps=peeps)

@app.route('/Chitter', methods = ['POST'])
def create_peep():
    content = request.form['content']
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
    repository.create(content, date_time)
    # peeps = repository.all()
    # return render_template('index.html', peeps=peeps)
    return redirect(url_for('get_peeps'))



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))