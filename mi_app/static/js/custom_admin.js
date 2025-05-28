document.addEventListener('DOMContentLoaded', function () {
    console.log("JS cargado correctamente");

    const botones = document.querySelectorAll('.submit-row input[type="submit"]');

    if (botones.length > 0) botones[0].id = 'btn-guardar';
    if (botones.length > 1) botones[1].id = 'btn-guardar-anadir';
    if (botones.length > 2) botones[2].id = 'btn-guardar-editar';
    if (botones.length > 3) botones[3].id = 'btn-eliminar';
});
