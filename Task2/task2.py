# part 1: Basic Authentication
from flask import Flask, request

app = Flask(__name__)

# Homepage
@app.route('/home', methods=['GET'])
def home():
    return "Welcome to the homepage"

# Define valid credentials
VALID_USERNAME = "user"
VALID_PASSWORD = "password"

@app.route('/basic-auth', methods=['GET'])
def basic_auth():
    auth = request.authorization
    if auth and auth.username == VALID_USERNAME and auth.password == VALID_PASSWORD:
        message = "Welcome"
        return (message,200)
    else:
        message = "Unauthorized access"
        return (message, 401)

# part 2: Bearer Token Authentication
VALID_TOKEN = "Token"

@app.route('/bearer-auth', methods=['GET'])
def bearer_auth():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        if token == VALID_TOKEN:
            message = "Access granted"
            return message, 200
    message = "Unauthorized access"
    return message, 401

if __name__ == '__main__':
    app.run(debug=True)

# part 3: OAuth 2.0 Authentication

from flask import Flask, request, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'random_secret_key'  # Replace with a secure secret key
oauth = OAuth(app)

# GitHub OAuth configuration
github = oauth.remote_app(
    'github',
    consumer_key='YOUR_CLIENT_ID',  # Replace with your GitHub Client ID
    consumer_secret='YOUR_CLIENT_SECRET',  # Replace with your GitHub Client Secret
    request_token_params={
        'scope': 'user:email',
    },
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

@app.route('/')
def index():
    return 'Welcome to the GitHub OAuth 2.0 example!'

@app.route('/oauth')
def oauth_login():
    return github.authorize(callback=url_for('authorized', _external=True))

@app.route('/callback')
def authorized():
    response = github.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error'],
            request.args['error_description']
        )
    session['github_token'] = (response['access_token'], '')
    user = github.get('user')
    return 'Logged in as: ' + user.data['login']

@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')

if __name__ == '__main__':
    app.run(debug=True)
