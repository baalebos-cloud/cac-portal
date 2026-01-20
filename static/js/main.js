// ===============================
// GLOBAL UTILITIES
// ===============================

function showAlert(message, type = "success") {
  const alertBox = document.createElement("div");
  alertBox.className = `alert alert-${type}`;
  alertBox.innerText = message;

  document.querySelector(".container")?.prepend(alertBox);

  setTimeout(() => {
    alertBox.remove();
  }, 4000);
}

// ===============================
// FORM VALIDATION
// ===============================

document.addEventListener("DOMContentLoaded", () => {

  const forms = document.querySelectorAll("form");

  forms.forEach(form => {
    form.addEventListener("submit", (e) => {

      const requiredFields = form.querySelectorAll("[required]");
      let valid = true;

      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          field.style.border = "1px solid red";
          valid = false;
        } else {
          field.style.border = "1px solid #ccc";
        }
      });

      if (!valid) {
        e.preventDefault();
        showAlert("Please fill all required fields", "error");
      }
    });
  });

});

// ===============================
// FILE UPLOAD PREVIEW
// ===============================

function previewImage(input, previewId) {
  const file = input.files[0];
  const preview = document.getElementById(previewId);

  if (file && preview) {
    const reader = new FileReader();
    reader.onload = () => {
      preview.src = reader.result;
    };
    reader.readAsDataURL(file);
  }
}

// ===============================
// PAYMENT STATUS HANDLER
// ===============================

function paymentStatus(status) {
  if (status === "success") {
    showAlert("Payment successful. Your application is being processed.");
  } else {
    showAlert("Payment failed. Please try again.", "error");
  }
}

// ===============================
// ADMIN ACTION CONFIRMATION
// ===============================

function confirmAction(message) {
  return confirm(message || "Are you sure you want to continue?");
}
