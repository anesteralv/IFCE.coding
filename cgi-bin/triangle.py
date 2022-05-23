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
base_ = float(form.getvalue('base'))
altura_ = float(form.getvalue('altura'))
# calcular area
area_tria = (base_ * altura_)/2
######### HTML

title = "Triângulo"
geo_funcs.print_header(title)

print("<h1>Triângulo</h1><hr>")
print("<p>Base: {:.2f}".format(base_))
print("<p>Altura: {:.2f}".format(altura_))
print("<p>Área do Triângulo: {:.1f}".format(area_tria))
print("<br><br>Clique <a href=\'../triangle.html\'>aqui </a> para novo cálculo.")
print("<br><br>Clique <a href=\'../index.html\'>aqui </a> para voltar ao início.")
geo_funcs.print_footer()