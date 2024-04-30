'''
realizzare un single page application che permette di avere informazioni sulle regioni italiane.
in un file csv devono essere memorizzate le seguenti informazioni: 
-nome della regione
-nome del capoluogo
-popolazione della regione
-popolazione del capoluogo
-percorso di un' immagine relativa alla regione.
l'applicazione deve permettere all'utente di selezionare da un elenco il nome della regione e 
deve fornire all'utente tutte le informazioni relative alla regione nonché il meteo relativo al
capoluogo di quella regione. Grafica a scelta.
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    #questa rotta restituisce la homepage della nostra single page application
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    risultato = sorted(list(set(df['nome_regione'])))
    return render_template('home.html', lista = risultato)

@app.route('/elenco')
def elenco():
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    info = df.nome_regione.sort_values()
    info.reset_index(drop=True, inplace=True)
    return render_template('json.html', tabella = info.to_json())

@app.route('/info/<nomeRegione>')
def info(nomeRegione):
    import pandas as pd
    df = pd.read_csv('/workspace/Flask/data/regioni.csv')
    info = df[df.nome_regione == nomeRegione]
    return render_template('json.html', tabella = info.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)