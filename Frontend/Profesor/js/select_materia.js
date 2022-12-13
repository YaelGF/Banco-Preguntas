//Funcion que devuelve un select option con las materias que tiene la api
function select_materia() {

    var url = "http://147.182.172.184/materias/";
    var select = document.getElementById("materia");
    var option = document.createElement("option");

    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.length; i++) {
                option.value = data[i].id_Materia;
                //option.value = data[i].materia;
                option.text = data[i].materia;
                select.add(option);
                option = document.createElement("option");
            }
        })
    .catch(err => console.log(err));
}
