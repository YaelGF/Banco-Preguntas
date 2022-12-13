function Guardar_carrera(){
    //Guarda una carrera o una lista de carreras
   var carrera = document.getElementById("carrera").value;
   //sesion del coordinador
   //var coordinador = sessionStorage.getItem("token");
    var coordinador = 3;

    var request = new XMLHttpRequest();
    request.open('POST', "http://147.182.172.184/carreras/", true);
    request.setRequestHeader("accept", "application/json");
    request.setRequestHeader("Content-Type", "application/json");

    request.onload = () => {
        
        const response  = request.responseText;
        const json      = JSON.parse(response); 
        
        const status    = request.status;

        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }

        else if (request.status == 202){

            console.log("Response: " + response);
            console.log("JSON: " + json);
            console.log("Status: " + status);

            Swal.fire({
                title: json.message,
                text: "Carrera almacenada correctamente",
                type: "success"
            }).then(function() {
                window.location = "carreras.html";
            });
            
        }
    };
    request.send(JSON.stringify([{carrera:carrera, coordinador:coordinador}]));

    
}