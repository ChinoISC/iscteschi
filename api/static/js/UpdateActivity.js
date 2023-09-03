$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    console.log('Evento submit activado');

    // Obtiene el valor del token CSRF del formulario
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    const id = $('#inputId').val();
    const title = $('#inputTitle').val();
    const description = $('#inputDescription').val();
    const color = $('#colorSelect').val();

    const activityData = {
      id: id,
      title: title,
      description: description,
      color: color,
    };

    const form = this;

    $.ajax({
      type: 'POST',
      url: '/change_edit/',
      dataType: 'json',
      data: JSON.stringify(activityData),
      contentType: 'application/json',
      headers: {
        'X-CSRFToken': csrfToken // Incluye el token CSRF en los encabezados
      },
      success: function(data) {
        if (data.message === 'La actividad se actualizo') {
          alert('La actividad se actualizo');
          window.location.href='/view_activity';
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
