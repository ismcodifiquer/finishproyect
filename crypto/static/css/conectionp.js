const btn = document.getElementById("Calculate");
const lblQ = document.getElementById("cantidad_dada");
const request = new XMLHttpRequest();

function reqHandler() {
    if (this.readyState === 4 && this.status == 200) {
    /* Comprobamos que el estado es 4 (operación completada)
        * los estados que podemos comprobar son:
        * 0 = UNSET (No se ha llamado al método open())
        * 1 = OPENED (Se ha llamdo al método open())
        * 2 = HEADERS_RECEIVED (Se ha llamado al método send())
        * 3 = LOADING (Se está recibiendo la respuesta)
        * 4 = DONE (Operación completada)
    */
        console.log(this.responseText);
        let respuesta = JSON.parse(this.responseText);

        if (respuesta.correct) {
            lblQ.value = respuesta.result.cantidad_dada
        } else {
            lblQ.valie = respuesta.message;
        }
    }
}

function btnClickHandler(ev) {
    const valor = document.getElementById("To").value;
    

    request.open('GET', `https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=1&symbol=BTC&convert=EUR&CMC_PRO_API_KEY=bab92701-0b6f-4e32-82cc-22af0e4cab19${EUR}`, true);
    request.send();

}

request.onload = reqHandler
btn.addEventListener('click', btnClickHandler);