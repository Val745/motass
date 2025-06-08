document.addEventListener("DOMContentLoaded", function () {
    // Mostrar/ocultar contenido de servicios
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

    // Elementos del formulario
    const inputFecha = document.getElementById('dia-modal');
    const selectHora = document.getElementById('hora-modal');
    const formAgendar = document.getElementById('form-agendar-modal');

    // Horarios disponibles
    const horariosSemana = [
        { value: "12:00-13:10", label: "12:00 P.M. – 1:10 P.M." },
        { value: "13:10-14:20", label: "1:10 P.M. – 2:20 P.M." },
        { value: "14:20-15:30", label: "2:20 P.M. – 3:30 P.M." },
        { value: "15:30-16:40", label: "3:30 P.M. – 4:40 P.M." },
        { value: "16:40-17:50", label: "4:40 P.M. – 5:50 P.M." },
        { value: "17:50-19:00", label: "5:50 P.M. – 7:00 P.M." }
    ];

    const horariosSabado = [
        { value: "10:00-11:30", label: "10:00 A.M. – 11:30 A.M." },
        { value: "11:30-13:00", label: "11:30 A.M. – 1:00 P.M." },
        { value: "13:00-14:30", label: "1:00 P.M. – 2:30 P.M." },
        { value: "14:30-16:00", label: "2:30 P.M. – 4:00 P.M." },
        { value: "16:00-17:30", label: "4:00 P.M. – 5:30 P.M." },
        { value: "17:30-19:00", label: "5:30 P.M. – 7:00 P.M." }
    ];

    // Configurar fecha mínima (hoy)
    inputFecha.min = new Date().toISOString().split('T')[0];

    // Manejar cambio de fecha
    inputFecha.addEventListener('input', function () {
        const fechaStr = this.value;
        if (!fechaStr) {
            selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
            selectHora.disabled = true;
            return;
        }

        const fecha = new Date(fechaStr + 'T12:00:00');
        const dia = fecha.getDay();

        // Validar domingos
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

    // Abrir modal al hacer clic en Agendar
    document.querySelectorAll('.agenda-button').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            if (typeof userHasMascotas !== "undefined" && !userHasMascotas) {
                document.getElementById('modal-sin-mascotas').style.display = 'flex';
            } else {
                var servicio = btn.closest('.agendar-servicios').querySelector('h3').innerText.trim();
                document.getElementById('modal-agendar').style.display = 'flex';
                document.getElementById('servicio-modal').value = servicio;
                
                // Resetear el formulario
                formAgendar.reset();
                selectHora.innerHTML = '<option value="">Selecciona un horario</option>';
                selectHora.disabled = true;
            }
        });
    });

    // Cerrar modales
    document.getElementById('cerrar-modal-sin-mascotas').addEventListener('click', function () {
        document.getElementById('modal-sin-mascotas').style.display = 'none';
    });

    document.getElementById('cerrar-modal-agendar').addEventListener('click', function () {
        document.getElementById('modal-agendar').style.display = 'none';
    });

    document.getElementById('ir-a-perfil').addEventListener('click', function () {
        window.location.href = "{% url 'crear_mascota' %}";
    });

    // Cerrar modal al hacer clic fuera del contenido
    document.getElementById('modal-agendar').addEventListener('click', function (e) {
        if (e.target === this) {
            this.style.display = 'none';
        }
    });

    // Envío del formulario
    formAgendar.addEventListener('submit', function (e) {
        e.preventDefault();

        // Validación visual de campos
        let isValid = true;
        const camposRequeridos = [
            document.getElementById('servicio-modal'),
            document.getElementById('mascota-modal'),
            document.getElementById('dia-modal'),
            document.getElementById('hora-modal')
        ];

        camposRequeridos.forEach(campo => {
            if (!campo.value) {
                campo.style.border = '1px solid red';
                isValid = false;
            } else {
                campo.style.border = '';
            }
        });

        if (!isValid) {
            alert('Por favor completa todos los campos marcados en rojo');
            return;
        }

        const formData = new FormData(this);

        fetch(this.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            if (!response.ok) throw new Error('Ese horario ya está ocupado, por favor elige otro');
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('¡Cita agendada con éxito!');
                this.reset();
                document.getElementById('modal-agendar').style.display = 'none';
                window.location.reload(); // Si quieres recargar
            } else {
                throw new Error(data.error || 'Error al guardar la cita');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert(error.message);
        });
    });

    // Función para obtener CSRF token
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

document.addEventListener('DOMContentLoaded', function () {
    const botonesAgendar = document.querySelectorAll('.agenda-button');
    const modalAgendar = document.getElementById('modal-agendar');
    const modalSinMascotas = document.getElementById('modal-sin-mascotas');
    const cerrarModalAgendar = document.getElementById('cerrar-modal-agendar');
    const cerrarModalSinMascotas = document.getElementById('cerrar-modal-sin-mascotas');
    const servicioInput = document.getElementById('servicio-modal');
    const horaSelect = document.getElementById('hora-modal');
    const fechaInput = document.getElementById('dia-modal');
    const irAPerfil = document.getElementById('ir-a-perfil');

    // Mostrar modal de agendamiento con el servicio correspondiente
    botonesAgendar.forEach(function (boton) {
        boton.addEventListener('click', function (e) {
            e.preventDefault();
            const servicio = boton.closest('.agendar-servicios').querySelector('h3').innerText;

            if (userHasMascotas) {
                servicioInput.value = servicio;
                modalAgendar.style.display = 'block';
            } else {
                modalSinMascotas.style.display = 'block';
            }
        });
    });

    // Cerrar modal agendar
    cerrarModalAgendar.addEventListener('click', function () {
        modalAgendar.style.display = 'none';
    });

    // Cerrar modal sin mascotas
    cerrarModalSinMascotas.addEventListener('click', function () {
        modalSinMascotas.style.display = 'none';
    });

    // Redireccionar al perfil para agregar mascota
    irAPerfil.addEventListener('click', function () {
        window.location.href = "/perfil";  // Ajusta esta URL según tu proyecto
    });


    // Cerrar modales al hacer clic fuera del contenido
    window.addEventListener('click', function (e) {
        if (e.target === modalAgendar) {
            modalAgendar.style.display = 'none';
        }
        if (e.target === modalSinMascotas) {
            modalSinMascotas.style.display = 'none';
        }
    });
});