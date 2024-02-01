from cmath import sqrt
import math
from flask import Flask, render_template,request
import forms 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/distancia", methods = ['GET','POST'])
def distancia():
     distancia_clase = forms.formularioDistancia(request.form)
     primerX, primerY, segundoX, segundoY, distanciaTotal = None, None, None, None, None

     if request.method == 'POST':
        primerX = distancia_clase.primerX.data
        primerY = distancia_clase.primerY.data
        segundoX = distancia_clase.segundoX.data
        segundoY = distancia_clase.segundoY.data
        numero1 = segundoX - primerX
        numero2 = segundoY - primerY
        distanciaTotal = math.sqrt((segundoX-primerX)**2 + (segundoY - primerY)**2)

        print("Distancia: {}".format(distanciaTotal))



     return render_template("distanciaForm.html", form = distancia_clase,primerX = primerX, primerY = primerY, segundoX = segundoX,segundoY = segundoY,distanciaTotal=distanciaTotal)

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
