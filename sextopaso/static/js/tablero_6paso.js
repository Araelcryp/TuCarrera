// Referencias a los elementos del DOM
const modal = document.getElementById("modal");
const modalTitle = document.getElementById("modal-title");
const closeButton = document.querySelector(".close-button");
const pdfIframe = document.getElementById("pdfIframe");

// Función para convertir enlaces de Google Drive a enlaces embebidos
function getEmbeddedPdfUrl(url) {
  if (url.includes("drive.google.com")) {
    // Extrae el ID del archivo usando una expresión regular
    const regex = /\/d\/([a-zA-Z0-9_-]+)/;
    const match = url.match(regex);
    if (match && match[1]) {
      // Convierte la URL a formato preview para incrustarla en un iframe
      return `https://drive.google.com/file/d/${match[1]}/preview`;
    }
  }
  return url;
}

// Función para abrir el modal con el PDF en un iframe
function openModal(event) {
  let card = event.target.closest(".card");
  if (!card) return;

  const university = card.getAttribute("data-university");
  const pdfUrl = card.getAttribute("data-pdf").trim();

  modalTitle.textContent = university;

  if (!pdfUrl || pdfUrl.includes("NO_PDF")) {
    // Si no hay PDF, se oculta el iframe y se muestra un mensaje
    pdfIframe.style.display = "none";
    if (!document.getElementById("modal-message")) {
      const msg = document.createElement("p");
      msg.id = "modal-message";
      msg.textContent = "Este PDF aún no está disponible.";
      msg.style.textAlign = "center";
      modalTitle.parentNode.insertBefore(msg, modalTitle.nextSibling);
    }
  } else {
    // Si hay un PDF, se muestra el iframe y se remueve cualquier mensaje previo
    pdfIframe.style.display = "block";
    const existingMsg = document.getElementById("modal-message");
    if (existingMsg) {
      existingMsg.remove();
    }
    pdfIframe.src = getEmbeddedPdfUrl(pdfUrl);
  }
  modal.style.display = "block";
}

// Función para cerrar el modal
function closeModal() {
  modal.style.display = "none";
  pdfIframe.src = "";
}

// Asigna el evento de clic a cada tarjeta
document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("click", openModal);
});

// Evento para cerrar el modal al hacer clic en el botón de cierre
closeButton.addEventListener("click", closeModal);

// Cierra el modal si se hace clic fuera del contenido modal
window.addEventListener("click", function (event) {
  if (event.target === modal) {
    closeModal();
  }
});
