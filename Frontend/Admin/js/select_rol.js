function select_rol() {
    var url = "http://147.182.172.184/usuarios/tipos/";
    var select = document.getElementById("id_rol");
    var option = document.createElement("option");

    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.length; i++) {
                option.value = data[i].id_TipoUsuario;
                var grupo = data[i].tipoUsuario;
                option.text = grupo;
                select.add(option);
                option = document.createElement("option");
            }
        })
    .catch(err => console.log(err));
}