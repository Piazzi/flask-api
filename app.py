from flask import Flask, abort

app = Flask(__name__)

BASE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%*()|-_=+^/?"

def custom_encode(n):
    """ Returns a 6 digit code for the given number (n) """    
    if n == 0: 
        return str(BASE[0]).zfill(6)
    base_length = len(BASE)
    digits = ''
    while n > 0:
        digits = BASE[n % base_length] + digits
        n = n // base_length
    return str(digits).zfill(6)

def custom_decode(code):
    """ Decodes the given code into a number """    
    baseLength = len(BASE)
    n = 0
    for d in code:
        n = baseLength*n + BASE[:baseLength].index(d)
    return n

@app.route("/encode/<int:number>")
def encode(number):
    num_length = len(str(number))
    if(num_length > 8):
        abort(400)
    return custom_encode(number)

@app.route("/decode/<code>")
def decode(code):
    if(len(str(code)) != 6):
        abort(400)
    return str(custom_decode(code)).zfill(6)

if __name__ == "__main__":
    app.run(debug=True) 