import os
from lib.peep_repository import PeepRepository
from lib.database_connection import get_flask_database_connection
from lib.peep import Peep
from lib.login import Login
from lib.login_repository import LoginRepository
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)


# @app.route('/Chitter', methods = ['GET'])
# def get_peeps():
#     if 'user_id' not in session:
#         return redirect(url_for('login_page'))
#     connection = get_flask_database_connection(app)
#     repository = PeepRepository(connection)
#     peeps = repository.all()
#     current_user = LoginRepository.get_username(email) # This is a placeholder for the current user
#     return render_template('index.html', peeps=peeps, current_user=current_user)

def start_session():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    repository = LoginRepository(connection)
    user_as_dict = repository.find_user(email)
    user_as_object = Login(user_as_dict['id'], user_as_dict['username'], user_as_dict['email'], user_as_dict['password'])
    session['users_id'] = user_as_object.id
    session['username'] = user_as_object.username



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
@app.route('/Chitter', methods = ['GET'])
def get_peeps():
    user_id = session.get('users_id') 
    if not user_id:
        return redirect(url_for('login_page'))
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    login_repository = LoginRepository(connection)
    current_user = login_repository.get_username(user_id)
    # This is a placeholder for the current user
    # return render_template('index.html', peeps=peeps, current_user=current_user)
    return render_template('index.html', peeps=peeps, current_user=current_user)


@app.route('/Chitter/login', methods=['POST'])
def login():
    # Get email and password from the form
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form.get('password')  # You might also want to check the password in your logic
    repository = LoginRepository(connection)
    if repository.check_password(email, password):
        # user_as_dict = repository.find_user(email)
        # user_as_object = Login(user_as_dict['id'], user_as_dict['username'], user_as_dict['email'], user_as_dict['password'])
        # session['users_id'] = user_as_object.id
        # session['username'] = user_as_object.username
        start_session()
        return redirect(url_for('get_peeps'))
        # return redirect('/Chitter/login_success')  # Redirect to the main page after successful login
    else:
        return redirect('/Chitter/create_account') # Redirect to create account page if email not found

@app.route('/Chitter/create_account', methods = ['GET'])
def create_account_page():
    return render_template('create_account.html')

# @app.route('/Chitter/login_success', methods = ['GET'])
# def login_success():
#     return render_template('login_success.html')

@app.route('/Chitter/create_account', methods = ['POST'])
def create_new_user():
    connection = get_flask_database_connection(app)
    repository = LoginRepository(connection)
    new_user = Login(None, request.form['username'], request.form['email'], request.form['password'])
    if not new_user.is_valid():
        return render_template('create_account.html', new_user=new_user, errors=new_user.generate_errors()), 400
    repository.create_user(new_user.username, new_user.email, new_user.password)
    return redirect(url_for('login_page'))

@app.route('/Chitter/the_nest', methods = ['GET'])
def get_nest():
    user_id = session.get('user_id') 
    if not user_id:
        # No user id in the session so the user is not logged in.
        return redirect(url_for('login_page'))
    connection = get_flask_database_connection(app)
    repository = LoginRepository(connection)
    user_data = repository.get_user_by_id(user_id)
    # The user is logged in, display their account page.
    return render_template('the_nest.html', current_user=user_data)


@app.route('/Chitter', methods = ['POST'])
def create_peep():
    users_id = session.get('users_id') 
    if not users_id:
        return redirect(url_for('login_page'))
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    content = request.form['content']
    if not content:
        return 'Content is required', 400
    username = session.get('username')
    repository.create(username, content, users_id)
    return redirect(url_for('get_peeps'))

@app.route('/Chitter/logout', methods=['GET'])
def logout():
    session.clear()  # Clears all session data
    return render_template('logout.html') # Redirect to the login page or homepage


# @app.route('/Chitter/the_nest', methods = ['GET'])
# def the_nest():
#     return render_template('the_nest.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

