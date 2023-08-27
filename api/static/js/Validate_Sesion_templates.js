// verificar_sesion.js

function verificarSesion() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            if (xhr.responseText != "no_logueado") {
                var username = xhr.responseText;
                document.getElementById("user").textContent = username;
            } else {
                alert("Debes iniciar sesión para acceder a esta página.");
                window.location.href = "pages-login.html";
            }
        }
    };
    xhr.open("GET", "../models/validation_session.php", true);
    xhr.send();
}

verificarSesion(); // Llamar a la función al cargar la página