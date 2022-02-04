from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return 'Hello, world!', 200

@app.route('/api/status', methods=['GET'])
def api_status():
    return '', 200

app.run(host='0.0.0.0', port=80)
