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

    function updateQuestions() {
        questions.forEach((question, index) => {
            question.style.display = index === currentQuestion ? "block" : "none";
        });
        progressBar.style.width = ((currentQuestion + 1) / questions.length) * 100 + "%";
        prevButton.style.display = currentQuestion === 0 ? "none" : "inline-block";
        nextButton.style.display = currentQuestion === questions.length - 1 ? "none" : "inline-block";
        submitButton.style.display = currentQuestion === questions.length - 1 ? "inline-block" : "none";
    }

    function showModal(message) {
        const modalContent = alertModal.querySelector("p");
        modalContent.textContent = message;
        alertModal.style.display = "block";
    }

    closeModal.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    window.addEventListener("click", (event) => {
        if (event.target === alertModal) {
            alertModal.style.display = "none";
        }
    });

    closeModalButton.addEventListener("click", () => {
        alertModal.style.display = "none";
    });

    function calculateResults() {
        const form = document.getElementById("testForm");
        const formData = new FormData(form);
        const results = { A: 0, B: 0, C: 0, D: 0, E: 0, F: 0, G: 0 };

        const questionMapping = {
            question1: "C", question2: "F", question3: "E", question4: "E",
            question5: "B", question6: "F", question7: "B", question8: "D",
            question9: "A", question10: "A", question11: "C", question12: "G",
            question13: "E", question14: "C", question15: "B", question16: "D",
            question17: "A", question18: "G", question19: "D", question20: "B",
            question21: "C", question22: "A", question23: "C", question24: "E",
            question25: "B", question26: "F", question27: "C", question28: "E",
            question29: "D", question30: "A", question31: "F", question32: "G",
            question33: "F", question34: "G", question35: "G"
        };

        formData.forEach((value, key) => {
            if (value === "si") {
                const category = questionMapping[key];
                results[category]++;
            }
        });

        // Enviar los resultados a Django
        fetch("/guardar-resultados/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken") // Necesario para Django
            },
            body: JSON.stringify(results)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la respuesta del servidor: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                window.location.href = "/resultados-primer-paso/";  // ✅ Redirige correctamente
            } else {
                showModal("Hubo un error al guardar los resultados. Inténtalo de nuevo.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            showModal("Hubo un problema con la conexión al servidor.");
        });
    }

    nextButton.addEventListener("click", () => {
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

    // **Evitar que "Enter" envíe el formulario automáticamente**
    document.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            let activeElement = document.activeElement;
            if (activeElement.type === "radio") {
                event.preventDefault();
            }
        }
    });

    // Función para obtener el token CSRF de Django
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    updateQuestions();
});
