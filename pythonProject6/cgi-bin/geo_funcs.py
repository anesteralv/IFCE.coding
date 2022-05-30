#C\\Users\\Alunos\\Desktop\\pythonProject2\\venv

import cgitb, cgi
import math

def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                    <head>
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" 
                        integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
                        <title>{}</title>
                    <head>
                    <body> """.format(title))

def print_footer():
    print("</body></html>")