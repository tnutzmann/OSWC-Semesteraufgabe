#!/usr/bin/python3
import presentation_layer.todo_list as tl

# das hier ist das spätere cgi script und ruft alles andere auf
print ("Content-type:text/html\n")
print (tl.print_all())