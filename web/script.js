// Onclick of the button
document.querySelector("button").onclick = function () {  
    eel.attrition_predict()(function(message){                      
      alert(message)
    })
  }