const cards = document.querySelectorAll(".card");
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const modalVideo = document.getElementById("modal-video-src");
const modalVideoContainer = document.querySelector(".modal-video-container");
const closeButton = document.querySelector(".close-button");

cards.forEach((card) => {
  card.addEventListener("click", () => {
    const videoUrl = card.getAttribute("data-video").trim();
    modalTitle.textContent = card.getAttribute("data-university");

    if (videoUrl.includes("VIDEO_ID")) {
      // No hay video: ocultamos el contenedor del iframe y limpiamos el src
      modalVideoContainer.style.display = "none";
      modalVideo.src = "";
      // Si no existe el mensaje, lo agregamos justo debajo del título
      if (!document.getElementById("modal-message")) {
        const msg = document.createElement("p");
        msg.id = "modal-message";
        msg.textContent = "Este video aún no está disponible.";
        msg.style.textAlign = "center";
        modalTitle.parentNode.insertBefore(msg, modalTitle.nextSibling);
      }
    } else {
      // Existe video: mostramos el contenedor y cargamos la URL
      modalVideoContainer.style.display = "block";
      modalVideo.src = videoUrl;
      // Si existiera el mensaje, lo removemos
      const existingMsg = document.getElementById("modal-message");
      if (existingMsg) {
        existingMsg.remove();
      }
    }
    // Mostramos el modal
    modal.style.display = "block";
  });
});

// Evento para cerrar el modal
closeButton.addEventListener("click", () => {
  modal.style.display = "none";
  modalVideo.src = "";
});

// Cerrar el modal si se hace clic fuera de su contenido
window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
    modalVideo.src = "";
  }
});
