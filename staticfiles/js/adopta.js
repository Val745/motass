document.addEventListener("DOMContentLoaded", function () {
  console.log("✅ Script cargado correctamente.");

  /* --- CABECERA --- */
  const header = document.getElementById("Header");
  if (header) {
      window.addEventListener("scroll", function () {
          const scroll = window.scrollY;
          if (scroll > 10) {
              header.style.backgroundColor = "rgb(44, 203, 179)";
          } else {
              header.style.backgroundColor = "transparent";
          }
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
      if (!carouselInner || !slides.length) {
          console.error("❌ No se encontró el carrusel o las diapositivas.");
          return;
      }

      if (index >= slides.length) {
          currentIndex = 0;
      } else if (index < 0) {
          currentIndex = slides.length - 1;
      } else {
          currentIndex = index;
      }

      const offset = -currentIndex * 100;
      carouselInner.style.transform = `translateX(${offset}%)`;
  }

  function nextSlide() {
      showSlide(currentIndex + 1);
  }

  function prevSlide() {
      showSlide(currentIndex - 1);
  }

  // Cambiar de slide automáticamente cada 7 segundos
  setInterval(nextSlide, 7000);

  // Asignar eventos a las flechas del carrusel
  const prevButton = document.querySelector('.carousel-control-prev');
  const nextButton = document.querySelector('.carousel-control-next');

  if (prevButton) {
      prevButton.addEventListener('click', prevSlide);
  }
  if (nextButton) {
      nextButton.addEventListener('click', nextSlide);
  }
    /* --- CONTADOR ANIMADO CON NÚMEROS ROSADOS Y UN "+" ANTES --- */
    const counters = document.querySelectorAll(".number");

    function animateCounters() {
        counters.forEach(counter => {
            const target = +counter.getAttribute("data-target");
            let count = 0;
            const duration = 1000; // Duración total en milisegundos (5 segundos)
            const interval = 50; // Tiempo entre actualizaciones en milisegundos (más alto = más lento)
            const steps = duration / interval; // Cantidad de actualizaciones
            const increment = target / steps; // Cuánto aumentar en cada actualización

            const updateCount = () => {
                count += increment;
                if (count < target) {
                    counter.innerText = `+${Math.floor(count).toLocaleString()}`;
                    setTimeout(updateCount, interval);
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

    const headers = document.querySelectorAll(".ayuda-donaciones h3");

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;

            // Oculta todos los demás
            document.querySelectorAll(".ayuda-contenido").forEach(item => {
                if (item !== content) item.style.display = "none";
            });

            // Alterna el display de la sección actual
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });

        function compartirPagina() {
            if (navigator.share) {
                navigator.share({
                    title: document.title,
                    text: "¡Mira esta increíble labor!",
                    url: window.location.href
                })
                .then(() => console.log("✅ Compartido con éxito."))
                .catch((error) => console.log("❌ Error al compartir:", error));
            } else {
                alert("Tu navegador no admite la función de compartir.");
            }
        }

        // Asegurar que el botón existe antes de asignar el evento
        const btnCompartir = document.querySelector(".btn-compartir");
        if (btnCompartir) {
            btnCompartir.addEventListener("click", compartirPagina);
        } else {
            console.warn("⚠️ No se encontró el botón de compartir.");
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
