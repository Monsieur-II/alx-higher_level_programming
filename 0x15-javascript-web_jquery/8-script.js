#!/usr/bin/node

$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    $.each(data.results, (index, value) => {
      const list = document.createElement('li');
      list.innerHTML = value['title'];
      $('ul#list_movies').append(list);
    });
  });
});
