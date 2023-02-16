const toggle = document.querySelector(".navbar__toggle");
const menu = document.querySelector(".navbar__menu");
const search = document.querySelector(".navbar__search");


toggle.addEventListener("click", function() {
  menu.classList.toggle("navbar__menu--active");
});
// Select the carousel and controls


// Set up the event listeners for the controls
prevBtn.addEventListener('click', () => {
carousel.scrollBy({
left: -300,
behavior: 'smooth'
});
});

nextBtn.addEventListener('click', () => {
carousel.scrollBy({
left: 300,
behavior: 'smooth'
});
});

// Update the scroll position variable when the user scrolls
carousel.addEventListener('scroll', () => {
scrollPos = carousel.scrollLeft;
});

// Reset the scroll position if the user resizes the window
window.addEventListener('resize', () => {
carousel.scrollTo({
left: scrollPos,
behavior: 'auto'
});
});
const currentYear = new Date().getFullYear();
const copyright = document.querySelector('footer p');
copyright.textContent = `Copyright © ${currentYear}`;

const carousel = document.querySelector('#our-clubs__carousel');
const prevBtn = document.querySelector('.our-clubs__prev-btn');
const nextBtn = document.querySelector('.our-clubs__next-btn');

// Set the initial position of the carousel
let scrollPos = 0;

// Set up the event listeners for the controls
prevBtn.addEventListener('click', () => {
  carousel.scrollBy({
    left: -600,
    behavior: 'smooth'
  });
});

nextBtn.addEventListener('click', () => {
  carousel.scrollBy({
    left: 600,
    behavior: 'smooth'
  });
});

// Update the scroll position variable when the user scrolls
carousel.addEventListener('scroll', () => {
  scrollPos = carousel.scrollLeft;
});

