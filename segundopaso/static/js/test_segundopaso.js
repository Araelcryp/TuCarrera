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
