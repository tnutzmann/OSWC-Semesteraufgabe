#!/usr/bin/python3
'''
Erster Versuch eines CGI Scriptes
'''

import cgi
import presentation_layer.todo_list as tl
import logging

logging.basicConfig( level=logging.DEBUG, filename='todo_cgi.log')

form = cgi.FieldStorage()
try:
    tl.draw(form)
except ValueError as ex:
        logging.error(ex)



#print('Content-Type:text/html')
#print()

#print('''
#<!DOCTYPE html>
#<html lang="de">
#  <head>
#    <meta charset="utf-8">
#    <meta name="viewport" content="width=device-width, initial-scale=1.0">
#    <title>Titel</title>
#  </head>
#  <body>
#''')

#for i in range(1, 10):
#    print(f'hallo {i} <br>')

#print('''
#  </body>
#</html>
#''')
