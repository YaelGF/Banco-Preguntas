function Guardar_carrera(){
    //Guarda una carrera o una lista de carreras
   var carrera = document.getElementById("carrera").value;
   //sesion del coordinador
   //var coordinador = sessionStorage.getItem("coordinador");
    var coordinador = "1";

    var request = new XMLHttpRequest();
    request.open('POST', "http://147.182.172.184/carreras/", true);
    request.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
            var data = JSON.parse(request.responseText);
            console.log(data);
        } else {
            console.log("Error en la llamada");
        }
    }
    request.onerror = function() {
        console.log("Error en la llamada");
    }
    request.send(JSON.stringify({carrera:carrera, coordinador:coordinador}));

    
}