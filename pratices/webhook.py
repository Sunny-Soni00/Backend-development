from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def send_simple_message():
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox879e0451d6194147a9e1661c46027e66.mailgun.org/messages",
  		auth=("api", "6cd2419e08bef1e7fb02d143d58e4a0f-c02fd0ba-c6396975"),
  		data={"from": "Webhook 10 <mailgun@sandbox879e0451d6194147a9e1661c46027e66.mailgun.org>",
  			"to": ["kshitiz.t@atriauniversity.edu.in"],
  			"subject": "Hello",
  			"text": "bhai bhai bhai"})


@app.route('/', methods=['POST'])
def index():
    send_simple_message()
    return "Message Sent"

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Webhook received")
    data = request.get_json()
    print(data)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
