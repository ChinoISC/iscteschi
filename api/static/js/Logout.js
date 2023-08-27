$(document).ready(function() {
    $('#logoutButton').on('click', function() {
        $.post('/logout/', function(data) {
            // Manejar la respuesta del servidor si es necesario
            if (data.message === 'Logout exitoso') {
                alert('Sesión cerrada exitosamente');
                // Redirigir al usuario a la página de inicio u otra página deseada
                window.location.href = '/login/';
            } else {
                alert('Error al cerrar sesión');
            }
        });
    });
});