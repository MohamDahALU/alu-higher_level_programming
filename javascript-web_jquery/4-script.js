import $ from 'jquery';

$(document).ready(() => {
  $('#toggle_header').click(() => {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
