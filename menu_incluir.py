from GetchUnix import _GetchUnix
import os

class menu_incluir:
    HEADER = '\033[95m'  
    OKBLUE = '\033[94m'  
    OKGREEN = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m'    
    NORMAL = '\033[0m'   
    BOLD = '\033[1m'     
    UNDERLINE = '\033[4m'

    def mod_active_line(self,mod_by):
        new_active = self.active_line + mod_by

        if new_active > len(self.sub_menus)-1:
            self.active_line = len(self.sub_menus)-1
        elif new_active < 0:
            self.active_line = 0
        else:
            self.active_line = new_active




    def __init__(self,nombre,sub_menus):

        self.nombre=nombre

        self.active_line=0

        self.sub_menus = sub_menus

    def print_sub_menu(self,fin=False):                   
        while True:                                   
            os.system("clear")                        
            for sub_menu in self.sub_menus:                    
                index=self.sub_menus.index(sub_menu)           
                                                      
                if index == self.active_line:         
                                                      
                    indicador = "[*] "    
                                                      
                else:                                 
                                                      
                    indicador = "[ ] "      

                if sub_menu.get_selected() == 1:

                    print(indicador+menu_incluir.OKGREEN+sub_menu.nombre+menu_incluir.NORMAL)

                else:
                    print(indicador+sub_menu.nombre)

                print("")                             

            u_input = self.get_user_input()


            if u_input == "quit":
                return "quit"

            elif u_input == "back":
                return "continue"                     
    def execute_install(self):
        
        for sc in self.sub_menus:

            if sc.selected==1:
                sc.run()
    
    def get_user_input(self):                                    
    	"""toma el input del usuario"""                          
    	                                                         
    	getch = _GetchUnix()                                     
    	user_input = getch()                                     
    	                                                         
    	# k=up                                                   
    	# j=down                                                 
    	                                                         
    	if user_input == "k":                                    
    	    self.mod_active_line(-1)                             
    	                                                         
    	elif user_input == "j":                                  
    	    self.mod_active_line(1)                              
    	                                                         
    	elif user_input == " ":                                  
    	                                                         
    	    return self.sub_menus[self.active_line].action() 
    	                                                         
    	elif user_input == "q":                                  
    	                                                         
    	    return "quit"                                        
    	                                                         
    	elif user_input == "b":                                  
    	                                                         
    	    return "back"                                        

    	elif user_input == "i":

    	    self.execute_install()
    	    return "back"

    	return "continue"




