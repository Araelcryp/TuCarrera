// Obtener elementos del DOM
const modal = document.getElementById('modal');
const modalTitle = document.querySelector('modal-title');
const closeButton = document.querySelector('.close-button');
const pdfIframe = document.getElementById('modal-pdf');
let pdfDoc = null;


// Load and render PDF with PDF.js library
function loadPdf(url) {
    const loadingTask = pdfjsLib.getDocument(url);
    loadingTask.promise.then(function (pdf) {
        pdfDoc = pdf;
        return pdf.getPage(1);
    }).then(function (page) {
        const context = canvas.getContext("2d");
        const viewport = page.getViewport({ scale: 1.5 });

        canvas.height = viewport.height;
        canvas.width = viewport.width;

        page.render({ canvasContext: context, viewport: viewport });
    });
}

// Función para abrir la ventana modal con la información de la tarjeta clickeada
function openModal(event) {
    // Verificar si el elemento clickeado es una tarjeta o está dentro de una
    let card = event.target.closest('.card');
    if (!card) return;

    // Extraer información de los atributos de datos
    const university = card.getAttribute('data-university');
    const PDFUrl = card.getAttribute('data-pdf');

    // Rellenar el contenido de la ventana modal
    modalTitle.textContent = university;

    if (pdfDoc) {
        loadPdf(pdfDoc, PDFUrl);
    }

    // Mostrar la ventana modal
    modal.style.display = 'block';
}

// Función para cerrar la ventana modal
function closeModal() {
    modal.style.display = 'none';
    modalVideo.src = '';
}

// Event listener para abrir la ventana modal al hacer clic en una tarjeta
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', openModal);
});

// Event listener para cerrar la ventana modal al hacer clic en el botón de cierre
closeButton.addEventListener('click', closeModal);

// Event listener para cerrar la ventana modal al hacer clic fuera del contenido modal
window.addEventListener('click', function (event) {
    if (event.target == modal) {
        closeModal();
    }
});

