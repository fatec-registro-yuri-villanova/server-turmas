from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/turmas')
def get_turmas():
    turmas = [
        {"id": "dsm1", "name": "DSM 1", "color": "#FF6B6B"},
        {"id": "dsm2", "name": "DSM 2", "color": "#4ECDC4"},
        {"id": "dsm3", "name": "DSM 3", "color": "#45B7D1"},
        {"id": "dsm4", "name": "DSM 4", "color": "#96CEB4"},
        {"id": "dsm5", "name": "DSM 5", "color": "#FFEEAD"},
        {"id": "dsm6", "name": "DSM 6", "color": "#D4A5A5"}
    ]
    return jsonify(turmas)

if __name__ == '__main__':
    app.run()