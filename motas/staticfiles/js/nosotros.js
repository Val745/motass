document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Script cargado correctamente.");


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

    //los desplegables
    const headers = document.querySelectorAll(".razon h3");

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;

            // Oculta todos los demás
            document.querySelectorAll(".razon p").forEach(item => {
                if (item !== content) item.style.display = "none";
            });

            // Alterna el display de la sección actual
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });

        const carousel = document.querySelector('.carousel');
        const prevBtn = document.getElementById('prev');
        const nextBtn = document.getElementById('next');
        const images = document.querySelectorAll('.carousel img');
        const totalImages = images.length;
        const imagesToShow = 3; // Mostrar 3 imágenes a la vez

        let currentIndex = 0;

        // Función para mostrar las imágenes actuales
        function showImages() {
            const offset = -currentIndex * (300 + 30); // 300px (ancho de la imagen) + 30px (margen)
            carousel.style.transform = `translateX(${offset}px)`;

            // Oculta o muestra los botones según la posición
            if (currentIndex === 0) {
                prevBtn.classList.add('hidden'); // Oculta la flecha izquierda
            } else {
                prevBtn.classList.remove('hidden'); // Muestra la flecha izquierda
            }

            // Oculta la flecha derecha cuando la cuarta imagen sea visible
            if (currentIndex >= totalImages - imagesToShow) {
                nextBtn.classList.add('hidden'); // Oculta la flecha derecha
            } else {
                nextBtn.classList.remove('hidden'); // Muestra la flecha derecha
            }
        }

        // Función para avanzar al siguiente conjunto de imágenes
        function next() {
            if (currentIndex < totalImages - imagesToShow) {
                currentIndex++;
                showImages();
            }
        }

        // Función para retroceder al conjunto anterior de imágenes
        function prev() {
            if (currentIndex > 0) {
                currentIndex--;
                showImages();
            }
        }

        // Event listeners para los botones
        if (nextBtn && prevBtn) {
            nextBtn.addEventListener('click', next);
            prevBtn.addEventListener('click', prev);
        }

        // Inicializar el carrusel
        showImages();
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
});
