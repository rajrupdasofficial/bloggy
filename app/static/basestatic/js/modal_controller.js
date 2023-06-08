// Open signup modal
function openModal() {
  var loginModal = document.getElementById('exampleModal');
  var signupModal = document.getElementById('staticBackdrop');

  // Hide the login modal
  var loginBackdrop = bootstrap.Modal.getInstance(loginModal);
  if (loginBackdrop) {
    loginBackdrop.hide();
  }

  // Show the signup modal
  var backdrop = new bootstrap.Modal(signupModal, {
    backdrop: 'static',
    keyboard: false
  });
  backdrop.show();
}

// Open login modal
function openLModal() {
  var signupModal = document.getElementById('staticBackdrop');
  var loginModal = document.getElementById('exampleModal');

  // Hide the signup modal
  var signupBackdrop = bootstrap.Modal.getInstance(signupModal);
  if (signupBackdrop) {
    signupBackdrop.hide();
  }

  // Show the login modal
  var backdrop = new bootstrap.Modal(loginModal, {
    backdrop: 'static',
    keyboard: false
  });
  backdrop.show();
}

