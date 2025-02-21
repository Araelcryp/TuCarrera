const modal = document.getElementById("modal");
const closeButton = document.querySelector(".close-button");
const modalTitle = document.getElementById("modal-title");
const modalVideo = document.getElementById("modal-video-src");

function openModal(event) {
  let card = event.target.closest(".card");
  if (!card) return;

  const university = card.getAttribute("data-university");
  const VideoUrl = card.getAttribute("data-video");

  modalTitle.textContent = university;
  modalVideo.src = VideoUrl;

  modal.style.display = "block";
}

function closeModal() {
  modal.style.display = "none";
  modalVideo.src = "";
}

document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("click", openModal);
});

closeButton.addEventListener("click", closeModal);

window.addEventListener("click", function (event) {
  if (event.target == modal) {
    closeModal();
  }
});
