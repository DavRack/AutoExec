import os
class script:

    scripts = []
    

    def get_selected(self):
        return self.selected

    def __init__(self,nombre):

        self.nombre = nombre
        self.comando = nombre
        self.selected=-1
        script.scripts.append(self)

    def action(self):
        self.selected=self.selected*-1
        return self.selected

    def run(self):
        comando="./scripts/"+self.comando
        os.system(comando)

        
