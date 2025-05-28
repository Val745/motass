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

  /* --- CONTADOR ANIMADO CON NÚMEROS ROSADOS Y UN "+" ANTES --- */
  const counters = document.querySelectorAll(".number");
  const speed =150; // Velocidad ajustada

  function animateCounters() {
      counters.forEach(counter => {
          const target = +counter.getAttribute("data-target");
          const increment = Math.ceil(target / speed);
          let count = 0;

          const updateCount = () => {
              count += increment;
              if (count < target) {
                  counter.innerText = `+${count.toLocaleString()}`;
                  requestAnimationFrame(updateCount);
              } else {
                  counter.innerText = `+${target.toLocaleString()}`;
              }
          };

          updateCount();
      });
  }

  // Activar animación cuando el usuario llegue a la sección
  const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
          if (entry.isIntersecting) {
              animateCounters();
              observer.disconnect();
          }
      });
  }, { threshold: 0.5 });

  const contadorSection = document.querySelector(".contador");
  if (contadorSection) {
      observer.observe(contadorSection);
  }

    //los desplegables
    const headers = document.querySelectorAll(".servicio h3");

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            const link = content.nextElementSibling; // "Ver más"

            // Oculta todos los demás
            document.querySelectorAll(".contenido").forEach(item => {
                if (item !== content) {
                    item.style.display = "none";
                    item.nextElementSibling.style.display = "none"; // Oculta "Ver más"
                }
            });

            // Alterna el display de la sección actual
            if (content.style.display === "block") {
                content.style.display = "none";
                link.style.display = "none";
            } else {
                content.style.display = "block";
                link.style.display = "block"; // Muestra "Ver más"
            }
        });
    });
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
