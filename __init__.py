import json
from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/add", methods=["POST"])
def ADD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sum=a+b
    response = "sum = " + str(sum)
    return response

@app.route("/nand", methods=["POST"])
def NAND(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    nand=~(a&b)
    response = "bitwise nand = " + str(nand)
    return response

@app.route("/sub", methods=["POST"])
def SUB(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sub=a-b
    response = "Difference = " + str(sub)
    return response
@app.route("/logicalAND", methods=["POST"])
def LOGICALAND(): 

    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    response = "Logical AND is = " + str(LOGICALAND)
    return response

@app.route("/exp", methods=["POST"])
def EXP(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    exp=a**b
    response = "exponent = " + str(exp)
    return response
@app.route("/log", methods=["POST"])
def LOG(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    log =math.log(a,b)
    response = "log = " + str(log)
    return response


@app.route("/isEqual", methods=["POST"])
def ISEQUAL():
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    response = str("Equal" if (a == b) else "Not Equal")
    return response

if __name__== "__main__":
    app.run()
