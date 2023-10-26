$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    console.log('Evento submit activado');

    // Obtiene el valor del token CSRF del formulario
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    const title = $('#inputTitle').val();
    const description = $('#inputDescription').val();
    const color = $('#colorSelect').val();
    const dates = $('#fecha').val();
    

    const activityData = {
      title: title,
      description: description,
      color: color,
      dates: dates,
    };

    const form = this;

    $.ajax({
      type: 'POST',
      url: '/create_activity/',
      dataType: 'json',
      data: JSON.stringify(activityData),
      contentType: 'application/json',
      headers: {
        'X-CSRFToken': csrfToken // Incluye el token CSRF en los encabezados
      },
      success: function(data) {
        if (data.message === 'Actividad creada exitosamente') {
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
