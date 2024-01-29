from flask import Flask, request, render_template

obj= Flask(__name__)

@obj.route('/')
def Welcome():
    return "Welcome buddy"

@ob.route('/calci')
def calculator():
    operator= request.json(operator)
    number1= request.json(number1)
    number2= request.json(number2)

if operator=='addition':
    result=number1+number2
    print(result)
elif operator=="subraction":
    result=number1-number2
    print(result)
elif operator=="multiplication":
    result=number1*number2
    print(result)
elif operator=="division":
    result=number1/number2
    print(result)
else:
    print("Unknown Operator. Please check")

if __name__ == '__main__':
    obj.run()
