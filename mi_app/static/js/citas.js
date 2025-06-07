document.addEventListener("DOMContentLoaded", function () {
    // Mostrar/ocultar contenido al hacer clic en los headers
    const headers = document.querySelectorAll(".agendar-servicios h3");
    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            document.querySelectorAll(".agendar-contenido").forEach(item => {
                if (item !== content) item.style.display = "none";
            });
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });

    const inputFecha = document.getElementById('dia-modal');
    const selectHora = document.getElementById('hora-modal');

    // Horarios por día
    const horariosSemana = [
        { value: "12:00-13:10", label: "12:00 p. m. – 1:10 p. m." },
        { value: "13:10-14:20", label: "1:10 p. m. – 2:20 p. m." },
        { value: "14:20-15:30", label: "2:20 p. m. – 3:30 p. m." },
        { value: "15:30-16:40", label: "3:30 p. m. – 4:40 p. m." },
        { value: "16:40-17:50", label: "4:40 p. m. – 5:50 p. m." },
        { value: "17:50-19:00", label: "5:50 p. m. – 7:00 p. m." }
    ];
    const horariosSabado = [
        { value: "10:00-11:30", label: "10:00 a. m. – 11:30 a. m." },
        { value: "11:30-13:00", label: "11:30 a. m. – 1:00 p. m." },
        { value: "13:00-14:30", label: "1:00 p. m. – 2:30 p. m." },
        { value: "14:30-16:00", label: "2:30 p. m. – 4:00 p. m." },
        { value: "16:00-17:30", label: "4:00 p. m. – 5:30 p. m." },
        { value: "17:30-19:00", label: "5:30 p. m. – 7:00 p. m." }
    ];

    // Bloquear domingos y fechas pasadas
    inputFecha.min = new Date().toISOString().split('T')[0];

    // Único event listener para inputFecha
    inputFecha.addEventListener('input', function() {
        const fechaStr = this.value;
        if (!fechaStr) {
            selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
            selectHora.disabled = true;
            return;
        }

        const fecha = new Date(fechaStr + 'T12:00:00');
        const dia = fecha.getDay();

        // Si es domingo
        if (dia === 0) {
            alert('La veterinaria está cerrada los domingos. Por favor, elige otro día.');
            this.value = '';
            selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
            selectHora.disabled = true;
            return;
        }

        // Cargar horarios según el día
        selectHora.disabled = false;
        selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
        const horarios = (dia === 6) ? horariosSabado : horariosSemana;

        horarios.forEach(h => {
            const option = document.createElement('option');
            option.value = h.value;
            option.textContent = h.label;
            selectHora.appendChild(option);
        });
    });

    // Al abrir el modal, limpiar los horarios si no hay fecha seleccionada
    document.querySelectorAll('.agenda-button').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            if (typeof userHasMascotas !== "undefined" && !userHasMascotas) {
                document.getElementById('modal-sin-mascotas').style.display = 'flex';
            } else {
                var servicio = btn.closest('.agendar-servicios').querySelector('h3').innerText.trim();
                document.getElementById('modal-agendar').style.display = 'flex';
                document.getElementById('servicio-modal').value = servicio;
                if (!inputFecha.value) {
                    selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
                    selectHora.disabled = true;
                }
            }
        });
    });

    // Modal sin mascotas: cerrar o ir a perfil
    document.getElementById('cerrar-modal-sin-mascotas').onclick = function() {
        document.getElementById('modal-sin-mascotas').style.display = 'none';
    };
    document.getElementById('ir-a-perfil').onclick = function() {
        window.location.href = '/crear_mascota/';
    };

    // Cerrar modal al hacer clic en la X
    var cerrarBtn = document.getElementById('cerrar-modal-agendar');
    if (cerrarBtn) {
        cerrarBtn.onclick = function() {
            document.getElementById('modal-agendar').style.display = 'none';
        };
    }

    // Cerrar modal al hacer clic fuera del contenido
    var modal = document.getElementById('modal-agendar');
    if (modal) {
        modal.onclick = function(e) {
            if (e.target === this) this.style.display = 'none';
        };
    }

    // Validar y guardar cita por AJAX
    const btnGuardar = document.getElementById('guardar-cita');
    if (btnGuardar) {
        btnGuardar.addEventListener('click', function(e) {
            const mascota = document.getElementById('mascota-modal');
            const fecha = inputFecha.value;
            const hora = selectHora.value;

            if (!mascota || !mascota.value || !fecha || !hora) {
                e.preventDefault();
                alert('Por favor, completa todos los campos antes de guardar la cita.');
                return false;
            }

            // Enviar datos al backend por AJAX
            e.preventDefault();
            fetch('/guardar_cita/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    mascota: mascota.value,
                    fecha: fecha,
                    hora: hora
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('¡Cita guardada exitosamente!');
                    document.getElementById('modal-agendar').style.display = 'none';
                    // Aquí puedes limpiar el formulario si quieres
                } else {
                    alert('Error al guardar la cita: ' + (data.error || 'Intenta de nuevo.'));
                }
            })
            .catch(error => {
                alert('Error de red al guardar la cita.');
                console.error(error);
            });
        });
    }

    // Función para obtener el token CSRF (si usas Django)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});