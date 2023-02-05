const toggle = document.querySelector(".navbar__toggle");
const menu = document.querySelector(".navbar__menu");

toggle.addEventListener("click", function() {
  menu.classList.toggle("navbar__menu--active");
});
