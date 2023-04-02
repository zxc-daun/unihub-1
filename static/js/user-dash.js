const userIcon = document.querySelector('.user-icon');
const userDropdown = document.querySelector('.user-dropdown');

userIcon.addEventListener('click', () => {
  userDropdown.style.display = userDropdown.style.display === 'none' ? 'block' : 'none';
});
