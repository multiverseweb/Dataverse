function checkPurpose(purpose) {
  // All possible custom modal purposes/types
  const modalPurposes = ['download dataverse', 'submit feedback', 'login/signup error', 'no reply'];
  return modalPurposes.includes(purpose); // Returns a boolean 
}


export function showModal(message, purpose) {
  // Check if no modal purpose was provided
  if(purpose === undefined || purpose === '') {
    console.error(`Please provide a correct login purpose. See 'website/pages/scripts/sharedUtilities.js' => showModal`);
  } else {
    // Check whether the modal purpose is currently available
    if(!checkPurpose(purpose)) {
      console.error(`Modal purpose '${purpose}' is unavailable, See 'website/pages/scripts/sharedUtilities.js' => showModal`);
      return;
    }

    document.getElementById('modal').style.display = 'block';
    document.getElementById('modal-message').innerText = message;
    document.getElementById('close-modal').style.display = 'block';

    if(purpose === 'download dataverse') {
      // Check if the accept and close buttons has been already hidden
      if(document.getElementById('accept-modal').style.display === 'none') {
        document.getElementById('accept-modal').style.display = 'block';
      
      document.getElementById('close-modal').innerText = 'later';
      document.getElementById('modal-buttons').style.gap = '25%';
      }
    } else if(purpose === 'submit feedback') {
      document.getElementById('accept-modal').style.display = 'none';    
      document.getElementById('close-modal').innerText = 'close';
      document.getElementById('modal-buttons').style.gap = '0';
    } else if(purpose === 'login/signup error') {
      document.getElementById('accept-modal').style.display = 'none';    
      document.getElementById('close-modal').innerText = 'Got it!';
      document.getElementById('modal-buttons').style.gap = '0';
    } else if(purpose === 'no reply') {
      document.getElementById('accept-modal').style.display = 'none';    
      document.getElementById('close-modal').style.display = 'none';
    }
  }
}

export function closeModal() {
  document.getElementById('modal').style.display = 'none';
}


// Attach the functions to the Global scope of the HTML, so it can be used on the 'onclick' attributes
window.showModal = showModal;
window.closeModal = closeModal;