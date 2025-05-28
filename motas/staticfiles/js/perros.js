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
