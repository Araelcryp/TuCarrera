document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".question");
    const progressBar = document.getElementById("progressBar");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const submitButton = document.getElementById("submitButton");
    const alertModal = document.getElementById("alertModal");
    const closeModal = alertModal.querySelector(".close");
    const closeModalButton = document.getElementById("closeModalButton");
    let currentQuestion = 0;

    // Function to update question visibility
    function updateQuestions() {
        questions.forEach((question, index) => {
            question.style.display = index === currentQuestion ? "block" : "none";
        });
        progressBar.style.width = ((currentQuestion + 1) / questions.length) * 100 + "%";
        prevButton.style.display = currentQuestion === 0 ? "none" : "inline-block";
        nextButton.style.display = currentQuestion === questions.length - 1 ? "none" : "inline-block";
        submitButton.style.display = currentQuestion === questions.length - 1 ? "inline-block" : "none";
    }

    // Function to show modal
    function showModal(message) {
        const modalContent = alertModal.querySelector("p");
        modalContent.textContent = message; // Cambia el texto de la modal dinámicamente
        alertModal.style.display = "block";
    }

    // Close the modal when the user clicks the "X" button
    closeModal.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    // Close the modal when the user clicks outside of it
    window.addEventListener("click", (event) => {
        if (event.target === alertModal) {
            alertModal.style.display = "none";
        }
    });

    closeModalButton.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    // Function to calculate results
    function calculateResults() {
        const form = document.getElementById("testForm");
        const formData = new FormData(form);
        const results = {
            A: 0,
            B: 0,
            C: 0,
            D: 0,
            E: 0,
            F: 0,
            G: 0,
        };

        const questionMapping = {
            question1: "C",
            question2: "F",
            question3: "E",
            question4: "E",
            question5: "B",
            question6: "F",
            question7: "B",
            question8: "D",
            question9: "A",
            question10: "A",
            question11: "C",
            question12: "G",
            question13: "E",
            question14: "C",
            question15: "B",
            question16: "D",
            question17: "A",
            question18: "G",
            question19: "D",
            question20: "B",
            question21: "C",
            question22: "A",
            question23: "C",
            question24: "E",
            question25: "B",
            question26: "F",
            question27: "C",
            question28: "E",
            question29: "D",
            question30: "A",
            question31: "F",
            question32: "G",
            question33: "F",
            question34: "G",
            question35: "G",
        };

        formData.forEach((value, key) => {
            if (value === "si") {
                const category = questionMapping[key];
                results[category]++;
            }
        });

        // Find the top 3 categories
        const sortedResults = Object.entries(results).sort((a, b) => b[1] - a[1]);
        const topCategories = sortedResults.slice(0, 3);

        displayResults(topCategories);
    }

    // Function to display results
    function displayResults(topCategories) {
        const descriptions = {
            A: "Inteligencia verbal / Lingüística: Tienes una capacidad y facilidad de usar correctamente las palabras, ya sea en forma oral y escrita. Puedes aprender a hablar idiomas fácilmente o los idiomas no es algo que se te dificulte. Disfrutas de actividades como platicar, exponer, escribir, leer, debatir, dialogar o explicar tus ideas.",
            B: "Inteligencia Lógica / Matemática: Tienes facilidad con los números y para razonar de forma lógica, es sencillo para ti relacionar patrones, comprender diagramas o esquemas y resolver problemas.",
            C: "Inteligencia Visual / Espacial: Disfrutas de las artes visuales, tienes una sensibilidad para los colores y las formas, posees habilidades para el diseño.",
            D: "Inteligencia Corporal: Tienes una gran habilidad física en cuanto a coordinación, equilibrio, fuerza, flexibilidad, velocidad y destreza.",
            E: "Inteligencia Musical / Rítmica: Tienes gran sensibilidad al ritmo, el tono o la melodía de una pieza musical, puedes expresar y comunicar tus sentimientos y emociones a través de la música.",
            F: "Inteligencia Intrapersonal: Tienes un gran autoconocimiento, eres consciente de tus estados de ánimo y de tus motivaciones.",
            G: "Inteligencia Interpersonal: Tienes la habilidad para empatizar con los demás, te es sencillo organizar a las personas y explicarles o enseñarles algún tema.",
        };

        let resultText = "Resultados:\n\n";
        topCategories.forEach(([category, score]) => {
            resultText += `${descriptions[category]} (Puntaje: ${score})\n\n`;
        });

        // Redirect to results page
        const encodedResults = encodeURIComponent(resultText);
        window.location.href = `resultados.html?results=${encodedResults}`;
    }

    // Event listeners for navigation buttons
    nextButton.addEventListener("click", (e) => {
        const current = questions[currentQuestion];
        const selectedOption = current.querySelector("input[type='radio']:checked");
        if (!selectedOption) {
            showModal("Por favor selecciona una respuesta antes de continuar.");
            return;
        }
        currentQuestion++;
        updateQuestions();
    });

    prevButton.addEventListener("click", () => {
        currentQuestion--;
        updateQuestions();
    });

    submitButton.addEventListener("click", (event) => {
        event.preventDefault();
        calculateResults();
    });

    // Initialize
    updateQuestions();
});
