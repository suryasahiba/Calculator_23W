import json
from flask import Flask, render_template, request, jsonify   

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

@app.route("/sub", methods=["POST"])
def SUB(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sub=a-b
    response = "Difference = " + str(sub)
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

@app.route("/antilog", methods=["POST"])
def ANTILOG(): 
    jsonStr = request.get_json() 
    jsonObj = json.loads(jsonStr) 
     
    a=int(jsonObj['N1']) 
    b=int(jsonObj['N2']) 
    antilog = b**a 
    response = "antilog of "+str(a)+" with base "+str(b)+" = " + str(antilog) 
    return response


if __name__== "__main__":
    app.run()
