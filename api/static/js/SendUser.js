$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    console.log('Evento submit activado');

    const firstName = $('#inputFirst').val();
    const lastName = $('#inputLast').val();
    const email = $('#inputEmail').val();
    const username = $('#inputUser').val();
    const password1 = $('#inputPassword1').val();
    const password2 = $('#inputPassword2').val();
    const csrfToken = $('[name=csrfmiddlewaretoken]').val(); // Agrega esta línea

    const userData = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      username: username,
      password1: password1,
      password2: password2
    };

    const form = this;

    $.ajax({
      type: 'POST',
      url: '/create_user/',
      dataType: 'json',
      data: JSON.stringify(userData),
      contentType: 'application/json',
      headers: {
        'X-CSRFToken': csrfToken // Incluye el token CSRF en los encabezados
      },
      success: function(data) {
        if (data.message === 'Datos insertados exitosamente') {
          alert('Inserción exitosa en la base de datos');
          form.reset();
        } else {
          alert('Error al insertar datos en la base de datos');
        }
      },
      error: function(error) {
        console.error('Error:', error);
        alert('Hubo un error en la solicitud');
      }
    });
  });
});

