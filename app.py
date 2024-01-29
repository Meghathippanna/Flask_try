from flask import Flask, request, render_template

obj= Flask(__name__)

@obj.route('/')
def Welcome():
    return "Welcome buddy"

@ob.route('/calci')
def calculator():
    operator=
    number1=
    number2=

if operator=='addition':
    result=number1+number2
elif operator=="subraction":
    result=number1-number2
elif operator=="multiplication":
    result=number1*number2
elif operator=="division":
    result=number1/number2
else:
    print("Unknown Operator. Please check")


if __name__ == '__main__':
    obj.run()
