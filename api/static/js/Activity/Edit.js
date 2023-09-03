// Maneja el clic en el enlace con la clase 'change-status-edit'.
$('.change-status-edit').on('click', function(event) {
  event.preventDefault(); // Evita la acción predeterminada del enlace.

  // Obtén el ID de la actividad desde el atributo 'data-id' del enlace.
  var activityId = $(this).data('id');

  // Redirige al usuario a la página deseada con el ID de la actividad como parámetro.
  window.location.href = '/change_edit/?id=' + activityId; // Reemplaza '/change_edit/' con tu URL real.
});
