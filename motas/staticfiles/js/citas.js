document.addEventListener("DOMContentLoaded", function () {
    const headers = document.querySelectorAll(".agendar-servicios h3");

    headers.forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;

            // Oculta todos los demás
            document.querySelectorAll(".agendar-contenido").forEach(item => {
                if (item !== content) item.style.display = "none";
            });

            // Alterna el display de la sección actual
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });
});
