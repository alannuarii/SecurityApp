const awal = document.querySelector(".navbar-toggler");
const camera = document.getElementById("camera");

awal.addEventListener("click", (e) => {
  e.preventDefault();
  awal.firstElementChild.classList.toggle("bi-chevron-double-right");
  camera.classList.toggle("d-none");
});
