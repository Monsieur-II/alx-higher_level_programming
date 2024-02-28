#!/usr/bin/node

$('div#add_item').click(() => {
  const list = document.createElement('li');
  list.innerHTML = 'Item';
  $('ul.my_list').append(list);
});
