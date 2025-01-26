document.addEventListener("DOMContentLoaded", function () {
    const questions = document.querySelectorAll(".question");
    const progressBar = document.getElementById("progressBar");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const submitButton = document.getElementById("submitButton");
    const alertModal = document.getElementById("alertModal");
    const closeModal = alertModal?.querySelector(".close");
    const closeModalButton = document.getElementById("closeModalButton");
    let currentQuestion = 0;

    const categories = {
        rojo: [1, 5, 9, 10, 14, 23, 36, 39],
        morado: [2, 6, 11, 15, 29, 41, 45, 46],
        azul: [3, 7, 13, 18, 22, 32, 38, 42],
        verde: [19, 28, 31, 40, 49, 52, 53, 55],
        amarillo: [20, 24, 33, 35, 48, 50, 54, 56],
        gris: [8, 12, 17, 21, 26, 30, 34, 47],
        menta: [4, 16, 25, 27, 37, 43, 44, 51]
    };

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

    function calculateResults() {
        const form = document.getElementById("testForm");
        const formData = new FormData(form);
        const scores = {
            rojo: 0,
            morado: 0,
            azul: 0,
            verde: 0,
            amarillo: 0,
            gris: 0,
            menta: 0
        };

        console.log("Form data entries:", [...formData.entries()]);

        formData.forEach((value, key) => {
            const questionNumber = parseInt(key.replace('question', ''));
            if (value === 'si') {
                for (let category in categories) {
                    if (categories[category].includes(questionNumber)) {
                        scores[category]++;
                        break;
                    }
                }
            }
        });

        formData.forEach((value, key) => {
            const questionNumber = parseInt(key.replace('question', ''));
            if (value === 'si') {
                for (let category in categories) {
                    if (categories[category].includes(questionNumber)) {
                        scores[category]++;
                        break;
                    }
                }
            }
        });

        let maxCategory = null;
        let maxScore = 0;

        for (let category in scores) {
            if (scores[category] > maxScore) {
                maxScore = scores[category];
                maxCategory = category;
            }
        }

        displayResult(maxCategory);
    }

    function displayResult(category) {
        let resultText = '';
        switch (category) {
            case 'rojo':
                resultText = 'ÁREA PROFESIONAL: CIENCIAS SOCIALES\nCARRERAS PROFESIONALES EN ADMINISTRACIÓN Y NEGOCIOS';
                break;
            case 'morado':
                resultText = 'ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS\nCARRERAS PROFESIONALES EN INGENIERÍA Y MANUFACTURA';
                break;
            case 'azul':
                resultText = 'ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS\nCARRERAS PROFESIONALES EN TECNOLOGÍAS DE LA INFORMACIÓN';
                break;
            case 'verde':
                resultText = 'ÁREA PROFESIONAL: HUMANIDADES Y ARTES\nCARRERAS PROFESIONALES EN HUMANIDADES Y ARTES';
                break;
            case 'amarillo':
                resultText = 'ÁREA PROFESIONAL: CIENCIAS BIOLÓGICAS, QUÍMICAS Y DE LA SALUD\nCARRERAS PROFESIONALES EN CIENCIAS DE LA SALUD';
                break;
            case 'gris':
                resultText = 'ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS\nCARRERAS PROFESIONALES EN CIENCIAS NATURALES, MATEMÁTICA Y ESTADÍSTICA';
                break;
            case 'menta':
                resultText = 'ÁREA PROFESIONAL: ARTES Y HUMANIDADES\nCARRERAS PROFESIONALES EN EDUCACIÓN';
                break;
            default:
                resultText = 'No se ha podido determinar una categoría.';
        }

        const encodedResult = encodeURIComponent(resultText);
        window.location.href = `/resultados-segundo-paso?results=${encodedResult}`;
    }

    // Function to show modal
    function showModal(message) {
        const modalContent = alertModal?.querySelector("p");
        if (modalContent) {
            modalContent.textContent = message;
            alertModal.style.display = "block";
        }
    }

    // Close modal logic
    closeModal?.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === alertModal) {
            alertModal.style.display = "none";
        }
    });

    closeModalButton?.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    // Navigation buttons event listeners
    nextButton.addEventListener("click", () => {
        const current = questions[currentQuestion];
        const selectedOption = current.querySelector("input[type='radio']:checked");
        if (!selectedOption) {
            showModal("Por favor selecciona una respuesta antes de continuar.");
            return;
        }
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            updateQuestions();
        }
    });

    prevButton.addEventListener("click", () => {
        if (currentQuestion > 0) {
            currentQuestion--;
            updateQuestions();
        }
    });

    submitButton.addEventListener("click", (event) => {
        event.preventDefault();
        calculateResults();
    });

    updateQuestions();
});
