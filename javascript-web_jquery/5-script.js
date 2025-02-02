import $ from 'jquery';

$('DIV#add_item').click(() => {
  $('UL.my_list').append('<li>Item</li>');
});
