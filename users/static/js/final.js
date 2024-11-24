if (typeof confetti !== 'undefined') {
    const canvas = document.getElementById('confettiCanvas');
    const confettiInstance = confetti.create(canvas, { resize: true, useWorker: true });
    const duration = 3 * 1000;
    const end = Date.now() + duration;
    const colors = ['#0264A8', '#66B2FF', '#023f81', '#FFD700', '#FFA500'];

    (function frame() {
        confettiInstance({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: colors
        });
        confettiInstance({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: colors
        });
        if (Date.now() < end) requestAnimationFrame(frame);
    })();
} else {
    console.error("Confetti library not loaded.");
}