import os
from lib.peep_repository import PeepRepository
from lib.database_connection import get_flask_database_connection
from lib.peep import Peep
from lib.login import Login
from lib.login_repository import LoginRepository
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
    if not content:
        return 'Content is required', 400
    repository.create(content)
    # peeps = repository.all()
    # return render_template('index.html', peeps=peeps)
    return redirect(url_for('get_peeps'))

# @app.route('/Chitter/<int:peep_id>', methods = ['POST'])
# def delete_peep(peep_id):
#     connection = get_flask_database_connection(app)
#     repository = PeepRepository(connection)
#     repository.delete(peep_id)
#     return redirect(url_for('get_peeps'))

@app.route('/Chitter/login', methods = ['GET'])
def login_page():
    return render_template('login.html')

# @app.route('/Chitter/login', methods = ['POST'])
# def login():
#     connection = get_flask_database_connection(app)
#     repository = LoginRepository(connection)
#     find_email = repository.find_user(request.form['email'])
#     if find_email == False:
#         return redirect(f'/Chitter/create_account')
#     else:
#         return redirect(f"/Chitter")
    
# @app.route('/Chitter/login', methods=['GET'])
# def login_page():
#     return render_template('login.html')

@app.route('/Chitter/login', methods=['POST'])
def login():
    # Get email and password from the form
    email = request.form['email']
    # password = request.form.get('password')  # You might also want to check the password in your logic
    
    connection = get_flask_database_connection(app)
    repository = LoginRepository(connection)
    
    # Use the email from the form to check the user's existence
    find_email = repository.find_user(email)
    
    if find_email:
        return redirect('/Chitter/login_success')  # Redirect to the main page after successful login
    else:
        return redirect('/Chitter/create_account') # Redirect to create account page if email not found

@app.route('/Chitter/create_account', methods = ['GET'])
def create_account_page():
    return render_template('create_account.html')

@app.route('/Chitter/login_success', methods = ['GET'])
def login_success():
    return render_template('login_success.html')

@app.route('/Chitter/create_account', methods = ['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = LoginRepository(connection)
    new_user = Login(None, request.form['username'], request.form['email'], request.form['password'])
    if not new_user.is_valid():
        return render_template('create_account.html', new_user=new_user, errors=new_user.generate_errors()), 400
    repository.create_user(new_user.username, new_user.email, new_user.password)
    return redirect(url_for('login_page'))



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

