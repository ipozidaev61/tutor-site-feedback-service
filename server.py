import os
from flask import Flask, request, render_template, jsonify, abort, make_response
from requests import get, post
import json

app = Flask(__name__, static_folder='public', template_folder='views')

@app.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    # Other headers can be added here if needed
    return response
  

token = os.environ.get('TOKEN')
        
@app.route('/')
def homepage():
    """Displays the homepage."""
    return render_template('index.html')
  
@app.route('/v1/feedback/postFeedback', methods=['POST'])
def postFeedback():
    data = json.loads(request.data)
    message = "Feedback from: " + data["name"] + "\n\n" + "E-mail: " + data["email"] + "\n\n" + data["feedback"]
    req = get('https://api.telegram.org/bot' + token + '/sendMessage?chat_id=468110974&parse_mode=Markdown&text=' + message)
    return req.content, req.status_code

if __name__ == '__main__':
    app.run()