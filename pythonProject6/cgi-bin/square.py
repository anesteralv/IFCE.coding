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
lado_ = float(form.getvalue('lado'))
# calcular area
area_quad = math.pow(lado_, 2)

#calcular perímetro
per_quad = 4 * lado_
######### HTML

title = "Quadrado"
geo_funcs.print_header(title)

print("<h1>Quadrado</h1><hr>")
print("<p>Lado: {:.2f}".format(lado_))
print("<p>Área do Quadrado: {:.2f}".format(area_quad))
print("<p>Perímetro do Quadrado: {:.2f}".format(per_quad))
print("<br><br>Clique <a href=\'../quadrado.html\'>aqui </a> para novo cálculo.")
print("<br><br>Clique <a href=\'../index.html\'>aqui </a> para voltar ao início.")
geo_funcs.print_footer()