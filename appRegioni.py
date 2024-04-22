from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def about():
    regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv' )
    nomi = list(set(regioni["denominazione_regione"]))
    nomi.sort()
    return render_template('regioni.html', regioni=nomi)

@app.route('/info/<regione>', methods=['GET'])
def info(regione): 
    import pandas as pd
    regioni_italiane = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv' )
    info = regioni_italiane[regioni_italiane.denominazione_regione == regione.capitalize()]
    return render_template('table.html', tabella = info.to_html())

@app.route('/info_json/<regione>', methods=['GET'])
def info_json(regione): 
    import pandas as pd
    regioni_italiane = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv' )
    info = regioni_italiane[regioni_italiane.denominazione_regione == regione.capitalize()]
    return render_template('json.html', tabella = info.to_json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
