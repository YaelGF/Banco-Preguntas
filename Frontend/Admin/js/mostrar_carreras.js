function mostrar_carreras(){
  
    fetch('http://147.182.172.184/carreras/')
    .then(response => response.json())
    .then(data => {
        console.log(data);
        let html = '';
        data.forEach(carrera => {
            html += `
            <center>
                <div class="col-md-4">
                    <div class="card mb-4 shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">${carrera.carrera}</h5>
                            <p class="card-text">Coordinador@: ${carrera.nombre} ${carrera.apellidoPaterno} ${carrera.apellidoMaterno}</p>

                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <button type="button" class="btn btn-sm btn-outline-secondary" onclick="location.href='detalle_carrera.html?${carrera.id_Carrera}'">Ver</button>
                                    <button type="button" class="btn btn-sm btn-outline-secondary" onclick="location.href='update_carrera.html?${carrera.id_Carrera}'">Editar</button>
                                    <button type="button" class="btn btn-sm btn-outline-secondary" onclick="location.href='delete_carrera.html?${carrera.id_Carrera}'">Eliminar</button>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
            </center>
            `;
        });
        document.getElementById('carreras').innerHTML = html;
    })

}