function select_carrera() {

    var url = "http://147.182.172.184/carreras/";
    var select = document.getElementById("carrera");
    var option = document.createElement("option");

    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            for (var i = 0; i < data.length; i++) {
                option.value = data[i].id_Carrera;
                option.text  = data[i].carrera;
                select.add(option);
                option = document.createElement("option");
            }
        })
    .catch(err => console.log(err));
}