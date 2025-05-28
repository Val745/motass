document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Script cargado correctamente.");

    /* --- CABECERA --- */
    const header = document.getElementById("Header");
    if (header) {
        window.addEventListener("scroll", function () {
            header.style.backgroundColor = window.scrollY > 10 ? "rgb(44, 203, 179)" : "transparent";
        });
    }

    /* --- MODAL DE CONTACTO --- */
    const modalContacto = document.getElementById("modal-contacto");
    const contactBtn = document.getElementById("contactanos-btn");
    const closeBtn = modalContacto?.querySelector(".close");

    if (contactBtn && modalContacto) {
        contactBtn.addEventListener("click", () => modalContacto.style.display = "flex");
    }
    if (closeBtn) {
        closeBtn.addEventListener("click", () => modalContacto.style.display = "none");
    }

    /* --- CARRUSEL --- */
    let currentIndex = 0;
    function showSlide(index) {
        const carouselInner = document.querySelector('.carousel-inner');
        const slides = document.querySelectorAll('.carousel-item');
        if (!carouselInner || !slides.length) return;

        currentIndex = (index + slides.length) % slides.length;
        carouselInner.style.transform = `translateX(${-currentIndex * 100}%)`;
    }

    function nextSlide() { showSlide(currentIndex + 1); }
    function prevSlide() { showSlide(currentIndex - 1); }

    setInterval(nextSlide, 7000);

    document.querySelector('.carousel-control-prev')?.addEventListener('click', prevSlide);
    document.querySelector('.carousel-control-next')?.addEventListener('click', nextSlide);

    /* --- CONTADOR ANIMADO --- */
    const counters = document.querySelectorAll(".number");
    const speed = 150;

    function animateCounters() {
        counters.forEach(counter => {
            const target = +counter.getAttribute("data-target");
            const increment = Math.ceil(target / speed);
            let count = 0;

            const updateCount = () => {
                count += increment;
                counter.innerText = count < target ? `+${count.toLocaleString()}` : `+${target.toLocaleString()}`;
                if (count < target) requestAnimationFrame(updateCount);
            };
            updateCount();
        });
    }

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                observer.disconnect();
            }
        });
    }, { threshold: 0.5 });

    const contadorSection = document.querySelector(".contador");
    if (contadorSection) observer.observe(contadorSection);

    /* --- MODALES DE LOGIN Y REGISTRO --- */
    function setupModal(modalId, openBtnId) {
        const modal = document.getElementById(modalId);
        const openBtn = document.getElementById(openBtnId);
        const closeBtn = modal?.querySelector(".close");

        if (modal && openBtn) {
            openBtn.addEventListener("click", () => modal.style.display = "block");
        }
        if (closeBtn) {
            closeBtn.addEventListener("click", () => modal.style.display = "none");
        }
        window.addEventListener("click", event => {
            if (event.target === modal) modal.style.display = "none";
        });
    }

    setupModal("loginModal", "iniciar-sesion-btn");
    setupModal("registerModal", "registrarse-btn");

    /* --- Transición entre login y registro --- */
    const openRegisterButton = document.getElementById("openRegisterModal");
    const loginModal = document.getElementById("loginModal");
    const registerModal = document.getElementById("registerModal");

    if (openRegisterButton && loginModal && registerModal) {
        openRegisterButton.addEventListener("click", event => {
            event.preventDefault();
            loginModal.style.display = "none";
            registerModal.style.display = "block";
        });
    }

    /* --- Redirección a login después de registro --- */
    const registerForm = document.getElementById("registerForm");
    if (registerForm) {
        registerForm.addEventListener("submit", event => {
            event.preventDefault();
            registerModal.style.display = "none";
            loginModal.style.display = "block";
        });
    }

    /* --- MODAL DE AGENDAR CONSULTA --- */
    const modalCita = document.getElementById("consulta-modal");
    const openBtn = document.getElementById("abrir-modal-cita");
    const closeBtnCita = document.getElementById("cerrar-modal");
    const closeBtnExtra = document.querySelector(".cerrar-modal-boton");

    if (openBtn && modalCita) {
        openBtn.addEventListener("click", function () {
            console.log("🟢 Abriendo modal de consulta");
            modalCita.style.display = "flex";
        });
    }

    if (closeBtnCita) {
        closeBtnCita.addEventListener("click", function () {
            console.log("🔴 Cerrando modal de consulta");
            modalCita.style.display = "none";
        });
    }

    if (closeBtnExtra) {
        closeBtnExtra.addEventListener("click", function () {
            console.log("🔴 Cerrando modal de consulta (botón extra)");
            modalCita.style.display = "none";
        });
    }

    window.addEventListener("click", function (event) {
        if (event.target === modalCita) {
            console.log("🔴 Clic fuera del modal de consulta");
            modalCita.style.display = "none";
        }
    });

    /* --- ENVÍO DEL FORMULARIO DE REGISTRO --- */
    if (registerForm) {
        registerForm.addEventListener("submit", async function (event) {
            event.preventDefault(); // Evita que la página se recargue

            const formData = new FormData(registerForm);
            const formObject = Object.fromEntries(formData.entries()); // Convierte a objeto JSON

            try {
                const response = await fetch("http://localhost:8080/api/registro", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formObject),
                });

                const result = await response.json();
                if (response.ok) {
                    console.log("✅ Registro exitoso:", result);
                    alert("Registro exitoso");
                    registerForm.reset(); // Limpia el formulario
                } else {
                    console.error("⚠️ Error en el registro:", result);
                    alert("Error en el registro");
                }
            } catch (error) {
                console.error("🚨 Error de conexión:", error);
                alert("No se pudo conectar al servidor");
            }
        });
    }
});
