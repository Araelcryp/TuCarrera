function toggleDropdown(dropdownId) {
    // Cerrar otros dropdowns
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.id !== dropdownId) {
            openDropdown.style.display = "none";
        }
    }

    // Toggle el dropdown actual
    var dropdown = document.getElementById(dropdownId);
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
}

function showInfo(info) {
    var infoText = document.getElementById("info-text");
    infoText.textContent = info;
}

// Cerrar los dropdowns al hacer clic fuera, pero no si se hace clic en la barra de búsqueda o dentro del dropdown
window.onclick = function(event) {
    if (!event.target.matches('.dropdown-btn') && !event.target.matches('.dropdown-search') && !event.target.closest('.dropdown-content')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
};

// Cerrar el dropdown al seleccionar un elemento de la lista
function selectItem(item) {
    var dropdown = item.closest('.dropdown-content');
    dropdown.style.display = "none";  // Cierra el dropdown
    showInfo(item.textContent);  // Puedes hacer algo adicional al seleccionar el ítem
}

// Función para eliminar acentos y normalizar texto
function normalizeText(text) {
    return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase();
}

// Filtrar el dropdown correspondiente
function filterDropdown(dropdownId, inputId) {
    var input = document.getElementById(inputId);
    var filter = normalizeText(input.value);  // Normaliza el input
    var div = document.getElementById(dropdownId);
    var a = div.getElementsByTagName('a');
    
    for (var i = 0; i < a.length; i++) {
        var txtValue = normalizeText(a[i].textContent || a[i].innerText);  // Normaliza el texto del dropdown
        if (txtValue.indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}
