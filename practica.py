from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resultado", methods=["GET","POST"])
def calcular():
    operacion = request.form.get("operacion")
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")

    if operacion == "suma":
        resultado = int(num1) + int(num2)
    elif operacion == "resta":
        resultado = int(num1) - int(num2)
    elif operacion == "multiplicacion":
        resultado = int(num1) * int(num2)
    elif operacion == "division":
        if int(num2) == 0:
            resultado = "División por cero no permitida"
        else:
            resultado = int(num1) / int(num2)
    else:
        resultado = "Operación no válida"

    return f"El resultado de la {operacion} es: {resultado}"

if __name__ == "__main__":
    app.run(debug=True)

     
class practica:
    
        def __init__(self):   
            self.numero = input("Dame un numero entero porfavor: ") 

        def imprime(self):
         for punto in range(1, int(self.numero) +1):
                print("*" * punto)


        

             





if __name__=="__main__":
        app.run(debug=True)
