$(document).ready(function() {
  // Handle form submission
  $('#form1').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the form data
    var formData = new FormData($(this)[0]);

    // Send the AJAX request
    $.ajax({
      type: 'POST',
      url: '{% url 'account:signup' %}',  // Replace with your Django signup URL
      data: formData,
      processData: false,
      contentType: false,
      success: function(response) {
        // Handle the successful response
        console.log(response);
        // Do something with the response, e.g., show a success message
      },
      error: function(xhr, status, error) {
        // Handle the error
        console.log(xhr.responseText);
        // Do something with the error, e.g., display an error message
      }
    });
  });
});
