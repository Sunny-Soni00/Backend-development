# # part 1: Basic Authentication
# from flask import Flask, request

# app = Flask(__name__)

# # Homepage
# @app.route('/home', methods=['GET'])
# def home():
#     return "Welcome to the homepage"

# # Define valid credentials
# VALID_USERNAME = "user"
# VALID_PASSWORD = "password"

# @app.route('/basic-auth', methods=['GET'])
# def basic_auth():
#     auth = request.authorization
#     if auth and auth.username == VALID_USERNAME and auth.password == VALID_PASSWORD:
#         message = "Welcome"
#         return (message,200)
#     else:
#         message = "Unauthorized access"
#         return (message, 401)

# # part 2: Bearer Token Authentication
# VALID_TOKEN = "Token"

# @app.route('/bearer-auth', methods=['GET'])
# def bearer_auth():
#     auth_header = request.headers.get('Authorization')
#     if auth_header and auth_header.startswith('Bearer '):
#         token = auth_header.split(' ')[1]
#         if token == VALID_TOKEN:
#             message = "Access granted"
#             return message, 200
#     message = "Unauthorized access"
#     return message, 401

# if __name__ == '__main__':
#     app.run(debug=True)

# part 3: OAuth 2.0 Authentication

import os
from flask import Flask, redirect, url_for, session, request
from requests_oauthlib import OAuth2Session

# Disable HTTPS requirement for OAuthlib (for development purposes only)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# GitHub OAuth configuration
CLIENT_ID = 'Ov23liK54s5jfTtWXekq'
CLIENT_SECRET = '112fb908f8d4f91caf39529cd2169f5c010024cc'
AUTHORIZATION_BASE_URL = "https://github.com/login/oauth/authorize"
TOKEN_URL = "https://github.com/login/oauth/access_token"
API_BASE_URL = "https://api.github.com/user"

@app.route('/')
def home():
    user_info = session.get('user_info')
    if user_info:
        return f'Hello, {user_info["login"]}! <a href="/logout">Logout</a>'
    return '<a href="/login">Login with GitHub</a>'

@app.route('/login')
def login():
    github = OAuth2Session(CLIENT_ID)
    authorization_url, state = github.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    github = OAuth2Session(CLIENT_ID, state=session['oauth_state'])
    token = github.fetch_token(TOKEN_URL, client_secret=CLIENT_SECRET, authorization_response=request.url)
    session['oauth_token'] = token

    user_info = github.get(API_BASE_URL).json()
    session['user_info'] = user_info
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user_info', None)
    session.pop('oauth_token', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)