document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var errorMessage = document.getElementById('error-message');

    // Simple validation
    if (username === 'iitpatna' && password === '12345') {
        alert("Login Sucessful !")
        errorMessage.textContent = '';
        // Redirect to another page or perform other actions here
        
        window.location.href = 'http://127.0.0.1:5000';
    } else {
        errorMessage.textContent = 'Invalid username or password';
    }
});
