const toggle = document.querySelector(".navbar__toggle");
const menu = document.querySelector(".navbar__menu");
const search = document.querySelector(".navbar__search");

toggle.addEventListener("click", function() {
  menu.classList.toggle("navbar__menu--active");
});

const currentYear = new Date().getFullYear();
const copyright = document.querySelector('footer p');
copyright.textContent = `Copyright © ${currentYear}`;
