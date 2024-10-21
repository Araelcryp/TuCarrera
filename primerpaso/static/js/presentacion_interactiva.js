document.getElementById('mainContainer').addEventListener('click', function(event) {
    var displayedImage = document.getElementById('displayedImage');
    var backgroundImage = document.getElementById('backgroundImage');

    if (event.target.tagName !== 'image' && displayedImage.src) {
        resetToBackground();
    }
});

function mostrarImagen(event, imageName) {
    event.preventDefault();
    event.stopPropagation();

    var image = document.getElementById('displayedImage');
    var backgroundImage = document.getElementById('backgroundImage');

    // Fade out the current image
    image.classList.remove('visible');
    image.classList.add('hidden');
    backgroundImage.classList.add('background-opaque');

    // After fade out, change the image source and fade in
    setTimeout(function() {
        image.src = imageName;
        image.classList.remove('hidden');
        image.classList.add('visible');
    }, 500);
}

function resetToBackground() {
    var image = document.getElementById('displayedImage');
    var backgroundImage = document.getElementById('backgroundImage');
    
    // Fade out the image and then hide it
    image.classList.remove('visible');
    image.classList.add('hidden');
    backgroundImage.classList.remove('background-opaque');

    setTimeout(function() {
        image.src = '';
    }, 500);
}