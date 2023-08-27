$(document).ready(function() {
    $('form').on('submit', function(event) {
      event.preventDefault();
      console.log('Evento submit activado');
  
      const firstName = $('#inputFirst').val();
      const lastName = $('#inputLast').val();
      const email = $('#inputEmail').val();
      const username = $('#inputUser').val();
      const password = $('#inputPassword').val();
  
      // Realiza validaciones aquí si es necesario
  
      const userData = {
        firstName: firstName,
        lastName: lastName,
        email: email,
        username: username,
        password: password
      };
  
      const form = this; // Captura el formulario actual
  
      $.ajax({
        type: 'POST',
        url: '../models/user_create.php',
        dataType: 'json',
        data: JSON.stringify(userData),
        contentType: 'application/json',
        success: function(data) {
          // Manejar la respuesta del servidor aquí
          if (data.message === 'Datos insertados exitosamente') {
            alert('Inserción exitosa en la base de datos');
            form.reset(); // Resetea el formulario actual
          } else {
            alert('Error al insertar datos en la base de datos');
          }
        },
        error: function(error) {
          console.error('Error:', error);
          // Manejar errores aquí
        }
      });
    });
  });