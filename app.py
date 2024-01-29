from flask import Flask, request, jsonify

obj= Flask(__name__)

@obj.route('/')
def Welcome():
    return "Welcome to Flask"

@obj.route('/calci', methods=["GET"])
def calculator():
    operator= request.json["operator"]
    number1= request.json["number1"]
    number2= request.json["number2"]

    if operator=="addition":
        result= int(number1) + int(number2)
    elif operator=="subraction":
        result=int(number1)- int(number2)
    elif operator=="multiplication":
        result=int(number1)* int(number2)
    elif operator=="division":
        result=int(number1)/ int(number2)
    else:
        result= "Error"
    return "The operation is {} and the result is {}".format(operator, result)

if __name__ == '__main__':
    obj.run()
