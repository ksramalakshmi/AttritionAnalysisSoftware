import eel
from random import randint
import attrition

eel.init("web")  
  
@eel.expose    
def attrition_predict(dataset):
    msg = attrition.predict_attrition(dataset)
    return msg
  
eel.start("main.html")