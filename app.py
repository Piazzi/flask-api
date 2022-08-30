from flask import Flask, abort

app = Flask(__name__)

# # Atividade 1
# Construa uma rota GET /encode/:number que deverá transformar a variável number em um código com um número fixo de seis caracteres.
# # Atividade 2
# Construa uma rota GET /decode/:code que irá decodificar o resultado da primeira rota e retornar o number inicial.
# # Regras
# - Considere uma variável number inteira com oito dígitos no máximo.
# - O alfabeto pode conter os seguintes códigos: a-z, A-Z, 0-9, !@#$%*()|-_=+^/?
# # Exemplo
# ```
# GET /encode/1234 return ABCDEF
# GET /decode/ABCDEF return 1234

def custom_encode(n):
    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%*()|-_=+^/?"
    if n == 0: 
        return base[0]
    base_length = len(base)
    digits = ''
    while n > 0:
        digits = base[n % base_length] + digits
        n  = n // base_length
    
    encoded_num_length = len(str(digits))
    leading_zeros = 0
    if(encoded_num_length < 8):
        leading_zeros = 9 - encoded_num_length
        
    return str(digits).zfill(leading_zeros)

@app.route("/encode/<int:number>")
def encode(number):
    num_length = len(str(number))
    
    if(num_length > 8):
        abort(400)
  
    return custom_encode(number)

@app.route("/decode/<code>")
def decode(number):
    if(len(str(number)) != 6):
        abort(400)
    return code 

if __name__ == "__main__":
    app.run(debug=True) 