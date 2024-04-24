'''
Realizzare un single page application che permette di avere le informazioni sulle regioni italiane.
In un file CSV devono essere memeorizzare le informazioni:
- il nome della regione
- il nome del capoluogo
- percorso di un'immagine relativa alla regione.
L'applicazione deve pemettre all'utente di selezionare da un elenco il nome della regione e deve fornire all'utente tutte le informazioni realtive 
alla regione nonchè il meteo realtivo al capoluogo di quella regione. Grafica a scelta
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    #questa rotta resituisce la la homepage della single page application
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    risultato = sorted(list(set(df['nome_regione'])))
    return render_template('home.html', lista = risultato)

@app.route('/elenco')
def elenco():
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    info = df.nomeRegione
    return render_template('json.html', lista = info.to_json())

@app.route('/info/<nomeRegione>')
def info(nomeRegione):
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    info = df[df.nome_regione == nomeRegione]
    return render_template('json.html', lista = info.to_json())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)