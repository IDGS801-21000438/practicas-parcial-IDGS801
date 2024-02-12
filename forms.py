from wtforms import Form,StringField, EmailField, TelField, IntegerField




class formularioDistancia (Form):
    primerX = IntegerField ('primerX')
    primerY = IntegerField('primerY')
    segundoX = IntegerField ('segundoX')
    segundoY = IntegerField('segundoY')
    

class formularioResistencias (Form):

    primeraBanda = IntegerField ('PrimeraBanda')
    segundaBanda = IntegerField ('SegundaBanda')
    terceraBanda = IntegerField ('TerceraBanda')
    rbTolerancia = StringField ('rbTolerancia')
