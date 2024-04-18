from flask import Flask, request, jsonify
from chat import usage_demo
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/', methods=['POST', 'OPTIONS'])
def handle_request():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'OK'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'OPTIONS, POST')
        return response
    elif request.method == 'POST':
        data = request.json
        input_text = data.get('input')
        if input_text:
            response_text = usage_demo(input_text)
            response = jsonify({'message': response_text})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
