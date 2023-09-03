// Maneja el clic en el enlace con la clase 'change-status-link'.
$('.change-status-delete').on('click', function(event) {
    event.preventDefault(); // Evita la acción predeterminada del enlace.
  
    // Obtén el ID de la actividad desde el atributo 'data-id' del enlace.
    var activityId = $(this).data('id');
  
    // Realiza una solicitud GET al endpoint 'CompletedActivity' con el ID de la actividad como parámetro.
    $.get('/change_delete/', { id: activityId }, function(response) {
      // Maneja la respuesta del servidor.
      if (response.message === "La actividad se eliminó correctamente") {
        // Actualiza la interfaz de usuario o muestra un mensaje de éxito al usuario.
        alert('La actividad se eliminó correctamente');
        location.reload();
      } else {
        // Muestra un mensaje de error si la respuesta no indica que el estado cambió.
        alert('Hubo un error al cambiar el estatus de la actividad');
      }
    }).fail(function() {
      // Maneja los errores de la solicitud AJAX.
      alert('Error al comunicarse con el servidor');
    });
  });
  