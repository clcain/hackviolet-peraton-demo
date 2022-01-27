from flask import Flask

app = Flask(__name__)

@app.route('/api/status', methods=['GET'])
def api_status():
    return 'HEALTHY', 200

app.run(host='0.0.0.0', port=80)
