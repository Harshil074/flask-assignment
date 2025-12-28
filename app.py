from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    return jsonify({
        "message": "Item stored successfully",
        "item": data
    })
