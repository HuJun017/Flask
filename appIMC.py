#realizzare un sito web che attraverso l'utlizzo di js, calcoli l'imc. Il sito deve essere sia in inglese che italiano. 
#L'utente inserisce il peso e l'altezza, il progrmma risponde con l'IMC, uno resposo e un'immagine adatta.
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def calcola_IMC_en():
    return render_template("indexIMC.html", 
    Titolo = "BMI Calculator", 
    Descrizione = "Calculate here your BMI", 
    Calcola = "Calculate",  
    Risultato = "Result", 
    Tipo = "Type")

@app.route('/it')
def calcola_IMC_it():
    return render_template("indexIMC.html", 
    Titolo = "Calcolatore IMC", 
    Descrizione = "Calcola qui il tuo IMC", 
    Calcola = "Calcola",  
    Risultato = "Risultato", 
    Tipo = "Tipo")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)