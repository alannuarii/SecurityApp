const awal = document.querySelector(".navbar-toggler");

awal.addEventListener("click", (e) => {
  e.preventDefault();
  awal.firstElementChild.classList.toggle("bi-chevron-double-right");
});
