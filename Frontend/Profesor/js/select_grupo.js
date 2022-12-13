function select_grupo() {
    var url = "http://147.182.172.184/grupos/";
    var select = document.getElementById("id_grupo");
    var option = document.createElement("option");

    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.length; i++) {
                option.value = data[i].id_Grupo;
                var grupo = data[i].carrera + "-" + data[i].grupo;
                option.text = grupo;
                select.add(option);
                option = document.createElement("option");
            }
        })
    .catch(err => console.log(err));
}