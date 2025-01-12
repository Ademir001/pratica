import json
carros ={
    "Marca":"HONDA",
    "Modelo":"htvf",
    "Funcao":"Correr"
}
carro_2 = json.dumps(carros, indent=4, separators=(":","="))
