function select_profesor() {
    var url = "http://147.182.172.184/usuarios/";
    var select = document.getElementById("id_profesor");
    var option = document.createElement("option");

    fetch(url)
        .then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.length; i++) {
                tipo_usuario = data[i].id_TipoUsuario;
                if (tipo_usuario == 2) {

                    option.value = data[i].id_Usuario;
                    option.text = data[i].nombre;
                    
                    select.add(option);
                    option = document.createElement("option");
                }
            }
        })
    .catch(err => console.log(err));
}