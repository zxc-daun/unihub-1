
document.addEventListener("DOMContentLoaded", function () {
  const dropdownToggles = document.querySelectorAll("#sidebar .dropdown-toggle");

  dropdownToggles.forEach((toggle) => {
    toggle.parentElement.addEventListener("mouseenter", function () {
      const submenu = toggle.nextElementSibling;
      submenu.style.display = "block";
      setTimeout(() => {
        submenu.classList.add("show");
      }, 1);
    });

    toggle.parentElement.addEventListener("mouseleave", function () {
      const submenu = toggle.nextElementSibling;
      submenu.classList.remove("show");
      setTimeout(() => {
        if (!submenu.classList.contains("show")) {
          submenu.style.display = "none";
        }
      }, 300);
    });
  });
});

document.querySelectorAll("#sidebar ul li a.dropdown-toggle").forEach((item) => {
  item.addEventListener("mouseenter", (event) => {
    const submenu = event.target.nextElementSibling;
    submenu.style.display = "block";
  });

  item.addEventListener("mouseleave", (event) => {
    const submenu = event.target.nextElementSibling;
    submenu.style.display = "none";
  });
});

document.querySelectorAll("#sidebar ul li ul").forEach((submenu) => {
  submenu.addEventListener("mouseenter", (event) => {
    event.target.style.display = "block";
  });

  submenu.addEventListener("mouseleave", (event) => {
    event.target.style.display = "none";
  });
});
