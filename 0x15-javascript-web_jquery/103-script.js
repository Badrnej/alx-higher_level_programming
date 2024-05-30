document.addEventListener("DOMContentLoaded", function() {
  $('#btn_translate').click(function() {
    var languageCode = $('#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, function(data) {
      console.log(data);
      $('#hello').text(data.hello);
    });
  });
  $('#language_code').on('keypress', function(e) {
    var keyCode = e.keycode || e.which;
    if (keyCode == 13 ) {
      var languageCode = $('#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + languageCode, function(data) {
        console.log(data);
        $('#hello').text(data.hello);
      });
    }
  });
});
