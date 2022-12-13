function crear_examen() {

    var profesor1    = $('#id_profesor').val();
    var fecha        = $('#fecha').val();
    var hora_inicio  = $('#hora_inicio').val();
    var hora_fin     = $('#hora_fin').val();
    var id_materia1  = $('#materia').val();
    var id_grupo1    = $('#id_grupo').val();

    var profesor = parseInt(profesor1);
    var id_materia = parseInt(id_materia1);
    var id_grupo = parseInt(id_grupo1);

    fecha = fecha[5] + fecha[6] +"/"+fecha[8] + fecha[9] +"/"+fecha[2] + fecha[3];

   hora_fin = hora_fin[0] + hora_fin[1] +" "+hora_fin[3] + hora_fin[4];

   hora_inicio = hora_inicio[0] + hora_inicio[1] +" "+hora_inicio[3] + hora_inicio[4];

    var data = [
        {
            "profesor": profesor,
            "fecha": fecha,
            "horaInicio": hora_inicio ,
            "horaFin": hora_fin,
            "id_Materia": id_materia,
            "id_Grupo": id_grupo
        }
    ];

    console.log(data);

    var request = new XMLHttpRequest();
    request.open('POST', 'http://147.182.172.184/examenes/', true);
    request.setRequestHeader("Content-type", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + localStorage.getItem('token'));

    request.onload = () => {
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) {
            Swal.fire({
                title: "Error al crear",
                text: json.detail,
                type: "error"
            });
        }
        else if (request.status == 201){
            Swal.fire({
                title: json.message,
                text: "Examen creado correctamente",
                type: "success"
            }).then(function() {
                window.location = "examenes.html";
            });
        }
    }
    request.send(JSON.stringify(data));    
}