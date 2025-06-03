// GLOBAL VARIABLES
// CONSTANTS
const loginForm = document.getElementById("login-form");

// EVENT LISTENERS
loginForm.addEventListener("submit", handleLogin);

// FUNCTIONS

/* This function takes the data input in the login modal form and 
handles user login errors found within base.html.
Using ajax we display errors to the user without having to refresh
the page.


*@param {Click} e - This is information of the event that triggers the
 function

*/
function handleLogin(e) {
    // Prevent default page reload behaviour
    e.preventDefault();
    // Create new instance of form data on each submit click
    // to pass to validation
    const formData = new FormData(loginForm);
    fetch(loginForm.action, {
        method: "POST",
        headers: {
            "X-Requested-With": "XMLHttpRequest"
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = data.home_url;
            } else {
                const loginErrorsDisplay = document.getElementsByClassName("login-errors")[0];
                loginErrorsDisplay.innerHTML = '';
                const errors = JSON.parse(data.errors);
                for (let field in errors) {
                    errors[field].forEach(error => {
                        const p = document.createElement("p");
                        p.textContent = error.message;
                        loginErrorsDisplay.appendChild(p);
                    });
                }
            }
        })
}