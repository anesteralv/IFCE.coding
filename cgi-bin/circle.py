#C\\Users\\Alunos\\PycharmProject\\venv
import cgitb, cgi
import math
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
################# logica do script
# recebe o valor do raio do usuário
raio_ = float(form.getvalue('raio'))
# calcular area
area_circ = math.pi * math.pow(raio_, 2)

#calcular perímetro
per_circ = 2 * math.pi * raio_
######### HTML

title = "Círculo"
geo_funcs.print_header(title)

print("<h1>Círculo</h1><hr>")
print("<p>Raio: {:.1f}".format(raio_))
print("<p>Perímetro do Círculo: {:.1f}".format(per_circ))
print("<p>Área do Círculo: {:.1f}".format(area_circ))
print("<br><br>Clique <a href=\'../circulo.html\'>aqui </a> para novo cálculo.")
print("<br><br>Clique <a href=\'../index.html\'>aqui </a> para voltar ao início.")
geo_funcs.print_footer()