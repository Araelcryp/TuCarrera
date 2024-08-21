document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('nav ul li a');

    for (const link of links) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            window.scrollTo({
                top: targetElement.offsetTop - document.querySelector('header').offsetHeight, // Ajusta el desplazamiento si tienes un menú fijo
                behavior: 'smooth'
            });
        });
    }
});