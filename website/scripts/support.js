function showReportForm() {
  document.getElementById("container").classList.add("popup-active");
  document.body.classList.add("popup-active");
  document.getElementById("bug-report-form").classList.add("active");
}
windowFunctions.push(showReportForm);

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
  emailInput.addEventListener("input", function () {
    emailInput.setCustomValidity("");
  })

  if (!trustedDomains.includes(emailDomain)) {
    emailInput.setCustomValidity("Please provide an email from a trusted provider. Ex: outlook, gmail, yahoo,..etc")
    return false;
  }
  return true;
}
windowFunctions.push(validateReport);

document.addEventListener("keyup", (event) => {
  if (event.key == 'Enter') {
    alert(window.innerWidth);
  }
})

function showChat() {
  document.getElementById("infinityChat").style.display = "flex";
  document.getElementById("infinityBtn").onclick = hideChat;
}

function hideChat() {
  document.getElementById("infinityChat").style.display = "none";
  document.getElementById("infinityBtn").onclick = showChat;
}