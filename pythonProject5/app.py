from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        y = request.form.get('unidade')
        if y == 'F-C':
            valor = float(request.form.get('valor'))
            x = (valor - 32) * 5 / 9
            return "<h1>Valor convertido para: {:.2f} Graus Celsius</h1>".format(x)
        if y == 'C-F':
            valor = float(request.form.get('valor'))
            x = (valor * 9 / 5) + 32
            return "<h1>Valor convertido para: {:.2f} Graus Fahrenheit</h1>".format(x)
        if y == 'K-C':
            valor = float(request.form.get('valor'))
            x = valor - 273.15
            return "<h1>Valor convertido para: {:.2f} Graus Celsius</h1>".format(x)
        if y == 'C-K':
            valor = float(request.form.get('valor'))
            x = valor + 273.15
            return "<h1>Valor convertido para: {:.2f} Kelvin</h1>".format(x)
        if y == 'K-F':
            valor = float(request.form.get('valor'))
            x = (valor - 273.15) * 9/5 + 32
            return "<h1>Valor convertido para: {:.2f} Graus Fahrenheit</h1>".format(x)
        if y == 'F-K':
            valor = float(request.form.get('valor'))
            x = (valor - 32) * 5/9 + 273.15
            return "<h1>Valor convertido para: {:.2f} Kelvin</h1>".format(x)
        if y == 'km-m':
            valor = float(request.form.get('valor'))
            x = valor * 1000
            return "<h1>Valor convertido para: {:.2f} metros</h1>".format(x)
        if y == 'km-cm':
            valor = float(request.form.get('valor'))
            x = valor * 100000
            return "<h1>Valor convertido para: {:.2f} centímetros</h1>".format(x)
        if y == 'm-cm':
            valor = float(request.form.get('valor'))
            x = valor * 100
            return "<h1>Valor convertido para: {:.2f} centímetros</h1>".format(x)
        if y == 'm-mm':
            valor = float(request.form.get('valor'))
            x = valor * 1000
            return "<h1>Valor convertido para: {:.2f} milímetros</h1>".format(x)
        if y == 'm-km':
            valor = float(request.form.get('valor'))
            x = valor / 1000
            return "<h1>Valor convertido para: {:.2f} quilômetros</h1>".format(x)
        if y == 'cm-m':
            valor = float(request.form.get('valor'))
            x = valor / 100
            return "<h1>Valor convertido para: {:.2f} metros</h1>".format(x)
        if y == 'cm-km':
            valor = float(request.form.get('valor'))
            x = valor / 100000
            return "<h1>Valor convertido para: {:.5f} quilômetros</h1>".format(x)
        if y == 'kg-g':
            valor = float(request.form.get('valor'))
            x = valor * 1000
            return "<h1>Valor convertido para: {:.2f} gramas</h1>".format(x)
        if y == 'g-kg':
            valor = float(request.form.get('valor'))
            x = valor / 1000
            return "<h1>Valor convertido para: {:.4f} quilogramas</h1>".format(x)
        if y == 'mg-kg':
            valor = float(request.form.get('valor'))
            x = valor / 1000000
            return "<h1>Valor convertido para: {:.6f} quilogramas</h1>".format(x)
        if y == 'kg-mg':
            valor = float(request.form.get('valor'))
            x = valor * 1000000
            return "<h1>Valor convertido para: {:.2f} miligramas</h1>".format(x)
        if y == 'mg-g':
            valor = float(request.form.get('valor'))
            x = valor / 1000
            return "<h1>Valor convertido para: {:.3f} gramas</h1>".format(x)
