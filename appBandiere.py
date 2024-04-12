from flask import Flask, render_template

app = Flask(__name__)

#default USA
@app.route('/')
@app.route('/en')
def hello_world():
    return render_template("indexBandiere.html", Titolo='Welcome', Testo='Hello, world!', Immagine='usa.png')

#Italy
@app.route('/it')
def hello_world_it():
    return render_template("indexBandiere.html", Titolo='Benvenuti', Testo='Ciao, mondo!', Immagine='italy.png')

#SpainEmpire
@app.route('/ie')
def hello_world_ie():
    return render_template("indexBandiere.html", Titolo='Bienvenido', Testo='Hola, Mundo! El imperio ha vuelto', Immagine='spanish empire.jpeg')

#Spain
@app.route('/es')
def hello_world_es():
    return render_template("indexBandiere.html", Titolo='Bienvenido', Testo='Hola, Mundo!', Immagine='spain.png')

#N_Germany
@app.route('/dr')
def hello_world_dr():
    return render_template("indexBandiere.html", Titolo='Willkommen', Testo='Hallo, Welt! Das Reich ist zurück!', Immagine='germany.png')

#Germany
@app.route('/de')
def hello_world_de():
    return render_template("indexBandiere.html", Titolo='Willkommen', Testo='Hallo, Welt!', Immagine='germany-new.png')

#Soviet Union
@app.route('/su')
def hello_world_su():
    return render_template("indexBandiere.html", Titolo='Добро пожаловать', Testo='Привет, товарищ!', Immagine='soviet.png')

#Uk
@app.route('/uk')
def hello_world_uk():
    return render_template("indexBandiere.html", Titolo='Welcome', Testo='Hello World!', Immagine='uk.png')

#Austria
@app.route('/at')
def hallo_welt_at():
    return render_template("indexBandiere.html", Titolo='Willkommen', Testo='Hallo, Welt!', Immagine='austria.png')

#Russia
@app.route('/ru')
def hello_world_ru():
    return render_template("indexBandiere.html", Titolo='Добро пожаловать', Testo='Привет, мир!', Immagine='russia.png')

#Ukraine
@app.route('/ua')
def hello_world_ukr():
    return render_template("indexBandiere.html", Titolo='Ласкаво просимо', Testo='Привіт Світ!', Immagine='ukr.png')

#China
@app.route('/cn')
def hello_world_cn():
    return render_template("indexBandiere.html", Titolo='欢迎', Testo='你好世界!', Immagine='china.png')

#South Korea
@app.route('/sk')
def hello_world_sk():
    return render_template("indexBandiere.html", Titolo='환영', Testo='안녕하세요 세계!', Immagine='skorea.png')

#Japan
@app.route('/jp')
def hello_world_jp():
    return render_template("indexBandiere.html", Titolo='いらっしゃいませ', Testo='こんにちは世界!', Immagine='japan.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)