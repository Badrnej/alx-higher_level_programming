$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
  console.log(data);
  $('#hello').text(data.hello);
  console.log(data.hello);
});
