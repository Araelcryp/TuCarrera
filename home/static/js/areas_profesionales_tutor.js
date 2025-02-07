document.addEventListener('DOMContentLoaded', function () {
    // Función para alternar la visibilidad del dropdown
    function toggleDropdown(dropdownId) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.id !== dropdownId) {
                openDropdown.style.display = "none";
            }
        }

        var dropdown = document.getElementById(dropdownId);
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
    }

    function showInfo(info) {
        var infoText = document.getElementById("info-text");
        if (infoText) {
            infoText.innerHTML = info; // Mostrar el texto con formato HTML
        } else {
            console.error('Elemento con id="info-text" no encontrado');
        }
    }

    // Función para cerrar los dropdowns al hacer clic fuera
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

    // Función para seleccionar un ítem en el dropdown y mostrarlo en el info-text
    function selectItem(item) {
        var dropdown = item.closest('.dropdown-content');
        dropdown.style.display = "none";  // Cierra el dropdown
        showInfo(item.textContent);  // Muestra el nombre del ítem seleccionado
    }

    // Función para normalizar texto (eliminar acentos y convertir a mayúsculas)
    function normalizeText(text) {
        return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toUpperCase();
    }

    // Función para filtrar los elementos del dropdown mientras se escribe en el campo de búsqueda
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

    // Exponer las funciones al ámbito global si las necesitas en el HTML
    window.toggleDropdown = toggleDropdown;
    window.showInfo = showInfo;
    window.selectItem = selectItem;
    window.filterDropdown = filterDropdown;
});