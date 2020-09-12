from flask import Flask, jsonify, request
import socket


app = Flask(__name__.split('.')[0])


@app.route("/",methods=['GET','POST'])
def func():
    if request.method == 'GET':
        return "get request"
    elif request.method == 'POST':
        bod = request.get_json()
        return bod

if __name__ == "__main__":
    app.run(host=socket.gethostbyname(socket.gethostname()), port=8000, debug=True)