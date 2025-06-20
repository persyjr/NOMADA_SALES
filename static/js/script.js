function cargarDatos() {
    fetch("")
        .then(res => res.json())
        .then(data => {
            const tabla = document.getElementById("tabla-datos");
            tabla.innerHTML = "";

            data.forEach(persona => {
                const fila = document.createElement("tr");

                fila.innerHTML = `
                    <td>${persona.nombre}</td>
                    <td>${persona.email}</td>
                    <td>
                        <button onclick='editar(${JSON.stringify(persona)})' class="w-100 btn btn-primary">Editar</button>
                        <button onclick='eliminar(${persona.id})'  class="w-100 btn btn-danger">Eliminar</button>
                    </td>
                `;
                tabla.appendChild(fila);
            });
        })
        .catch(error => console.error("Error al cargar datos:", error));
}

function eliminar(id) {
    if (!confirm("¿Seguro que deseas eliminar este registro?")) return;

    fetch("actions/delete.php", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id })
    })
    .then(() => cargarDatos())
    .catch(error => console.error("Error al eliminar:", error));
}

function editar(persona) {
    for (let key in persona) {
        if (document.getElementById(key)) {
            document.getElementById(key).value = persona[key];
        }
    }
}

document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(this);

    const isUpdate = formData.get("id");

    const url = isUpdate ? "actions/update.php" : "actions/create.php";

    fetch(url, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(res => {
        alert(res.message);
        this.reset();
        document.getElementById("id").value = "";
        cargarDatos();
    })
    .catch(error => console.error("Error al guardar:", error));
});

window.onload = cargarDatos;