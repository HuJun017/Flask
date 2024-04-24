function getElenco() {
    fetch('https://3246-hujun017-flask-i1ii7bh5k9w.ws-eu110.gitpod.io/elenco')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for (let regione in data) {
            document.getElementById('elenco').innerHTML += data[regione] + '<br />'
        }
    })
}