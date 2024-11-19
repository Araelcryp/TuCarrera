// Obtener elementos del DOM
const modal = document.getElementById('modal');
const closeButton = document.querySelector('.close-button');
const modalIframe = document.getElementById('modal-iframe');
const modalTitle = document.getElementById('modal-title');
const modalDescription = document.getElementById('modal-description');

// Función para abrir la ventana modal con la información de la tarjeta clickeada
function openModal(event) {
    // Verificar si el elemento clickeado es una tarjeta o está dentro de una
    let card = event.target.closest('.card');
    if (!card) return;

    // Extraer información de los atributos de datos
    const university = card.getAttribute('data-university');
    const MapUrl = card.getAttribute('data-image');
    const info = card.getAttribute('data-info');

    // Rellenar el contenido de la ventana modal
    modalTitle.textContent = university;
    modalIframe.src = MapUrl;
    modalIframe.alt = `Ubicacion de ${university}`;
    modalDescription.textContent = info;

    // Mostrar la ventana modal
    modal.style.display = 'block';
}

// Función para cerrar la ventana modal
function closeModal() {
    modal.style.display = 'none';
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