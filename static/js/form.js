
        document.addEventListener("DOMContentLoaded", () => {
          const nameInput = document.querySelector("#name");
          const categoryInput = document.querySelector("#category");
          const nameError = document.querySelector("#name-error");
          const categoryError = document.querySelector("#category-error");

          function validateName() {
            if (!nameInput.value.trim()) {
              nameError.textContent = "Name is required.";
              return false;
            } else {
              nameError.textContent = "";
              return true;
            }
          }

          function validateCategory() {
            if (!categoryInput.value) {
              categoryError.textContent = "Category is required.";
              return false;
            } else {
              categoryError.textContent = "";
              return true;
            }
          }

        const submitForm = async () => {
          const form = document.querySelector("#create-club-form");
          const event = new Event('submit', {cancelable: true});

          form.dispatchEvent(event);

          if (event.defaultPrevented) {
            return;
          }

          const isNameValid = validateName();
          const isCategoryValid = validateCategory();

          if (!isNameValid || !isCategoryValid) {
            return;
          }

          const formData = new FormData(form);

          // Add the files separately
          const imageInput = document.querySelector("#image");
          const constitutionInput = document.querySelector("#constitution");
          formData.append("image", imageInput.files[0]);
          formData.append("constitution", constitutionInput.files[0]);

          const response = await fetch("/api/clubs/", {
            method: "POST",
            headers: {
              "X-CSRFToken": "{{ csrf_token }}",
            },
            body: formData,
          });

          if (response.ok) {
            window.location.href = "/";
            console.log("Club created successfully.");
          } else {
            alert("Failed to create club. Please check your input and try again.");
          }
        }

        document.querySelector("#create-club-form").addEventListener("submit", (event) => {
          event.preventDefault();
        });
        document.querySelector("#submit-btn").addEventListener("click", submitForm);
    });
