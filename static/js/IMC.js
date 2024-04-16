function calcola_IMC() {
    let altezzaInput = document.getElementById('altezza').value;
    let pesoInput = document.getElementById('peso').value;

    let altezza = parseFloat(altezzaInput);
    let peso = parseFloat(pesoInput);

    let IMC;
    let testo = document.getElementById('testo');

    IMC = peso / (altezza ** 2);
    IMC = risultato.toFixed(2);
    testo.textContent = IMC;

    //tipo
    let tipo= document.getElementById('tipo');

    if (IMC < 18.5) {
        tipo.textContent = "sottopeso"
    } else if (IMC >= 18.5 && IMC <= 25) {
        tipo.textContent = "normopeso"
    } else if (IMC >= 25 && IMC <= 30) { 
        tipo.textContent = "sovrappeso"
    } else if (IMC > 30) {
        tipo.textContent = "obeso"
    }
}