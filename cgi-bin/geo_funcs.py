#C\\Users\\Alunos\\Desktop\\pythonProject2\\venv

import cgitb, cgi
import math

def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                    <head>
                        <title>{}</title>
                    <head>
                    <body> """.format(title))

def print_footer():
    print("</body></html>")