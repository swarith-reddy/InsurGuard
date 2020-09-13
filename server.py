from flask import Flask, jsonify, request
import socket
from app.insurance_policy import get_insurance_policy

app = Flask(__name__.split('.')[0])

@app.route("/",methods=['GET','POST'])
def func(state):
    if request.method == 'GET':
        return get_insurance_policy(state)

if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000, debug=True)