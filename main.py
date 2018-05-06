import subprocess
from subprocess import Popen, PIPE
from script import script
from menu_incluir import menu_incluir
import os
import time

scripts_name=subprocess.run(['ls', 'scripts/'],shell=False, stdout=subprocess.PIPE)

scripts_name = scripts_name.stdout.decode('utf-8')

scripts = scripts_name.split()

# crea los objetos scrip
for sc in scripts:
    script(sc)

# da permisos de ejecucion

for sc in scripts:
    scripts_name=subprocess.run('cd scripts && sudo chmod +x '+sc ,shell=True, stdout=subprocess.PIPE)
    


# crea los objetos menu

inclu_menu = menu_incluir("incluir",script.scripts)

inclu_menu.print_sub_menu()


