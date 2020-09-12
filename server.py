from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def func():
    return "testing"

if __name__ == "__main__":
    app.run(port=8000, debug=True)