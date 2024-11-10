function openModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.add("show"); // Añade la clase para mostrar la modal
}

function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove("show"); // Quita la clase para ocultar la modal
}

// Cerrar la modal al hacer clic fuera del contenido
window.onclick = function(event) {
    const modals = document.getElementsByClassName("modal");
    for (let i = 0; i < modals.length; i++) {
        if (event.target === modals[i]) {
            modals[i].classList.remove("show"); // Quita la clase para ocultar la modal
        }
    }
};
