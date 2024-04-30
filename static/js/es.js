function getElenco() {
    fetch('https://3245-hujun017-flask-i1ii7bh5k9w.ws-eu110.gitpod.io/elenco')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for (let regione in data) {
            document.getElementById('elenco').innerHTML += '<a href=https://3245-hujun017-flask-i1ii7bh5k9w.ws-eu110.gitpod.io/info/' + data[regione] + '>' + data[regione] + '</a>' + '<br />'
        }
    })
    let bottone = document.getElementById('bottone');
    bottone.style.display = 'none';
}