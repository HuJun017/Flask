function calcola_IMC() {
    let altezzaInput = document.getElementById('altezza').value;
    let pesoInput = document.getElementById('peso').value;

    let altezza = parseFloat(altezzaInput);
    let peso = parseFloat(pesoInput);

    let IMC;
    let testo = document.getElementById('testo');

    IMC = peso / (altezza ** 2);
    IMC = IMC.toFixed(2); // CORRETTO: Utilizza IMC invece di risultato
    testo.textContent = IMC;

    //tipo
    let tipo = document.getElementById('tipo');

    if (IMC < 18.5) {
        tipo.textContent = "-1";
    } else if (IMC >= 18.5 && IMC <= 25) {
        tipo.textContent = "0";
    } else if (IMC >= 25 && IMC <= 30) { 
        tipo.textContent = "1";
    } else if (IMC > 30) {
        tipo.textContent = "2";
    }
}
