  $(document).ready(function(){
    $('#id_email').on('blur' , validate);
    function validate(){
      var email = $('#id_email').val();
      $.ajax({
        method : "GET",
        url: 'http://127.0.0.1:8000/stereolife/auth/registration/validate-email/',
        data: {
          'email': email
        },
        dataType: 'json',
        success: function (data) {
        console.log(data);
          if (data.is_taken) {
            $('#error-mail').text(data.is_taken);
            $('#btn').attr('disabled' , 'disabled');
            }
            else if (data.ok) {
               $('#error-mail').text('');
               $('#btn').removeAttr('disabled');
            }
          },
          error: function(data){
                console.log(data);

          }

      })
    }
  })