import $ from 'jquery';

$(document).ready(() => {
  // The old URL doesn't work.
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});
