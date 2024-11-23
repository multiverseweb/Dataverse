import { attachToWindow } from "./sharedUtilities.js";
import { windowFunctions } from "./script.js";

// Function to show the issue report form
function showReportForm() {
    document.getElementById("container").classList.add("popup-active");
    document.body.classList.add("popup-active");
    document.getElementById("bug-report-form").classList.add("active");
  }
  windowFunctions.push(showReportForm);
  
  // Function to close the issue report form
  function closeReportForm() {
    document.getElementById("container").classList.remove("popup-active");
    document.body.classList.remove("popup-active");
    document.getElementById("bug-report-form").classList.remove("active");
  }
  windowFunctions.push(closeReportForm);
  
  function validateReport() {
    const form = document.forms["Bug Report Form"];
    const emailInput = form["email"];
    const emailValue = form["email"].value.trim();
    const trustedDomains = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com", "protonmail.com", "icloud.com", "tutanota.com"];
    const emailDomain = emailValue.split('@')[1].toLowerCase();
    emailInput.addEventListener("input", function() { // Reset the validity message after change in input
      emailInput.setCustomValidity("");
    })
    
    if(!trustedDomains.includes(emailDomain)) {
      emailInput.setCustomValidity("Please provide an email from a trusted provider. Ex: outlook, gmail, yahoo,..etc")
      return false;
    }
    return true;
  }
  windowFunctions.push(validateReport);

document.addEventListener("keyup", (event) => {
    if(event.key == 'Enter') {
        alert(window.innerWidth);
    }
})

// Attach functions required by the DOM to the window
attachToWindow(windowFunctions);