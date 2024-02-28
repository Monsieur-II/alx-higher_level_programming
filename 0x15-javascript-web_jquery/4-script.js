#!/usr/bin/node

$('div#toggle_header').click(() => {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
});
