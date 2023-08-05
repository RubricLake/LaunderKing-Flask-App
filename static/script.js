document.addEventListener('DOMContentLoaded', function () {
  const currentUrl = window.location.href;

  if (currentUrl.includes("/register")) // Checks if we are on the register page.
  {
    const form = document.getElementById('register-form');
    const login_form = document.getElementById('login-form');

    form.addEventListener('submit', function (e) {
      const email = document.getElementById('register-email').value;
      const password = document.getElementById('register-password').value;
      const confirm = document.getElementById('register-confirm').value;
      
      // Check email regex stuff
      if (!validEmail(email))
      {
        alert("Invalid Email Address!");
        e.preventDefault();
      }

      if (!passwordsMatch(password, confirm)) // Checks if Password and Confirm match properly
      {
          alert("Passwords do not match!");
          e.preventDefault();
      }
      else{
        console.log("Successful Registration!");
      }
      
    }); // End of register
  } 
  else if (currentUrl.includes("/order"))
  {
      const loginButtons = this.querySelectorAll('.buy-now-button-login')
      loginButtons.forEach(loginButton => {
        loginButton.addEventListener('click', function () {
          window.location.href = "/login";
        });
      });
  }

  

    function passwordsMatch(password, confirm) { // Confirm Password match
      return password === confirm;
    }

    function validEmail(email) { // Do magic regex logic here
      if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
      {
        return true;
      }
        return false;
    }

    

}); // End of DOM load

  

