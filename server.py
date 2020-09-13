from flask import Flask, jsonify, request
import socket
from app.insurance_policy import get_insurance_policy
from app.disaster_type import get_fema_json

app = Flask(__name__.split('.')[0])

@app.route("/",methods=['GET','POST'])
def func():
    if request.method == 'POST':
        test = request.get_json(force=True)
        return get_fema_json(test['state'])
    elif request.method == 'GET':
        test = request.args['state']
        return get_insurance_policy(test)
    

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)