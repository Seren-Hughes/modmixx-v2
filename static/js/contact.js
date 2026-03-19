
// Contact form submission handling to prevent errors/double submits and show feedback
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contact-form");
  const submitBtn = document.getElementById("contact-submit-btn");
  
  if (!form || !submitBtn) return;
  
  let locked = false;
  
  // Store the default text
  const defaultText = submitBtn.getAttribute("data-default-text") || "Send";
  
  form.addEventListener("submit", function (event) {
    // Prevent accidental double-submit clicks
    if (locked) {
      event.preventDefault();
      return;
    }
    
    locked = true;
    submitBtn.disabled = true;
    submitBtn.setAttribute("aria-busy", "true");
    submitBtn.textContent = "Verifying...";
    
    // After a short delay, show sending state
    window.setTimeout(function () {
      if (submitBtn.disabled) {
        submitBtn.textContent = "Sending...";
      }
    }, 700);
  });
  
  // Reset button state if form has errors (when page reloads with validation errors)
  if (form.querySelector(".errorlist") || form.querySelector(".is-invalid")) {
    locked = false;
    submitBtn.disabled = false;
    submitBtn.removeAttribute("aria-busy");
    submitBtn.textContent = defaultText;
  }
});
