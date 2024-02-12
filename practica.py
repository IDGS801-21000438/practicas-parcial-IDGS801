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



@app.route("/resistencia",methods = ['GET','POST'])
def resistencia():
    

    resistencia_clase = forms.formularioResistencias(request.form)
    PrimeraBanda,SegundaBanda,TerceraBanda,rbTolerancia, resistenciaTotal,resistenciaMaxima,resistenciaMinima = 0,0,0,0,0,0,0


    if request.method == 'POST':
        PrimeraBanda = resistencia_clase.primeraBanda.data
        SegundaBanda = resistencia_clase.segundaBanda.data
        TerceraBanda = resistencia_clase.terceraBanda.data
        rbTolerancia = resistencia_clase.rbTolerancia.data

    colores = {
        0:'Negro',
        1:'Cafe',
        2:'Rojo',
        3:'Naranja',
        4:'Amarillo',
        5:'Verde',
        6:'Azul',
        7:'Violeta',
        8:'Gris',
        9:'Blanco'
    }
    colores3 = {
        10:'Negro',
        100:'Cafe',
        1000:'Rojo',
        10000:'Naranja',
        100000:'Amarillo',
        1000000:'Verde',
        10000000:'Azul',
        100000000:'Violeta',
        1000000000:'Gris',
        10000000000:'Blanco',
    }

    if rbTolerancia == 'oro':
       rbTolerancia = 0.05
    elif rbTolerancia == 'plata':
        rbTolerancia = .1   


    valor1 = colores.get(PrimeraBanda)
    valor2 = colores.get(SegundaBanda)
    valor3 = colores3.get(TerceraBanda)

    concatenacion = (str(PrimeraBanda)+str(SegundaBanda)) 
    resistenciaTotal1 = int(concatenacion) * TerceraBanda
    resistenciaTotal = float(rbTolerancia) * resistenciaTotal1
    resistenciaMinima = (resistenciaTotal1 - resistenciaTotal) / 10
    resistenciaMaxima = (resistenciaTotal1 + resistenciaTotal)  /10


  

    print(valor1,valor2)


    return render_template("recistencias.html",form = resistencia_clase,
                           valor1=valor1,
                           valor2=valor2,
                           valor3=valor3,
                           PrimeraBanda = PrimeraBanda,
                           SegundaBanda=SegundaBanda,
                           TerceraBanda=TerceraBanda,
                           rbTolerancia=rbTolerancia,
                           resistenciaTotal=resistenciaTotal,
                           resistenciaMaxima=resistenciaMaxima,
                           resistenciaMinima=resistenciaMinima)

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
