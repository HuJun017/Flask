function get_elenco() {
    fetch('https://3245-hujun017-flask-i1ii7bh5k9w.ws-eu110.gitpod.io/elenco')
    .then(response => response.json())
    .then(data => {
        document.getElementById('elenco').innerHTML = data
        console.log(data)
        for (let regione in data) {
            document.getElementById('elenco').innerHTML += data[regione] + "<br />"
        }
    })
}