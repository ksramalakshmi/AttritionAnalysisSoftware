import eel
from random import randint
  
eel.init("web")  
  
@eel.expose    
def random_python():
    print("Random function running")
    return randint(1,100)
  
eel.start("main.html")