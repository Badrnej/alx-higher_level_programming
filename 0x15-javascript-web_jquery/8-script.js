$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  for (var i = 0; i < data.count; i++) {
    $('<li></li>').appendTo('#list_movies')
    $('#list_movies li:last-child').text(data.results[i].title)
    console.log(data.results[i].title)
  }
});
