document.addEventListener("DOMContentLoaded", function () {
    const adoptarBtn = document.getElementById("adoptar-btn");
    const modal = document.getElementById("modal");
    const closeModal = document.querySelector(".close");
    const btnEntiendo = document.getElementById("btnEntiendo");
    const infoSection = document.getElementById("info-section");
    const formulario = document.getElementById("formularioAdopcion");

    // Ocultar formulario al inicio
    formulario.style.display = "none";

    // Mostrar el modal cuando se haga clic en "ADOPTAR"
    adoptarBtn.addEventListener("click", function () {
        modal.style.display = "block";
    });

    // Cerrar el modal al hacer clic en la "X"
    closeModal.addEventListener("click", function () {
        modal.style.display = "none";
        // Restaurar el estado inicial (información visible, formulario oculto)
        infoSection.style.display = "block";
        formulario.style.display = "none";
    });

    // Mostrar el formulario y ocultar la información cuando se haga clic en "ENTIENDO"
    btnEntiendo.addEventListener("click", function () {
        infoSection.style.display = "none"; // Ocultar información
        formulario.style.display = "block"; // Mostrar formulario
    });

    // Cerrar modal si se hace clic fuera del contenido
    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
            infoSection.style.display = "block";
            formulario.style.display = "none";
        }
    });
});

