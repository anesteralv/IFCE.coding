# C\\Users\\Alunos\\PycharmProject\\venv
import cgitb, cgi
import math
import geo_funcs

# habilita a visualização de erros
cgitb.enable(display=0, logdir="./")
# instancia um form para receber dados do navegador
form = cgi.FieldStorage()
################# logica do script
# recebe o valor do raio do usuário
baseMaior_ = float(form.getvalue('baseMaior'))
baseMenor_ = float(form.getvalue('baseMenor'))
Lado1_ = float(form.getvalue('Lado1'))
Lado2_ = float(form.getvalue('Lado2'))

# calcular perímetro
per_trap = (baseMaior_ + baseMenor_ + Lado1_ + Lado2_)

######### HTML

title = "Trapézio"
geo_funcs.print_header(title)

print("<h1>Trapézio</h1><hr>")
print("<p>Base Maior: {:.2f}".format(baseMaior_))
print("<p>Base Menor: {:.2f}".format(baseMenor_))
print("<p>Lado 1: {:.2f}".format(Lado1_))
print("<p>Lado 2: {:.2f}".format(Lado2_))
print("<p>Perímetro do Trapézio: {:.1f}".format(per_trap))
print("<br><br>Clique <a href=\'../per-trapezio.html\'>aqui </a> para novo cálculo.")
print("<br><br>Clique <a href=\'../index.html\'>aqui </a> para voltar ao início.")
geo_funcs.print_footer()
