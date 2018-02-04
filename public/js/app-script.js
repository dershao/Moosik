$(document).ready(function() {
  $('#tweet-form').on('submit', function() {

    var name = $('#subheading').text();

    $.ajax({
      type: 'POST',
      url: '/twitter',
      data: {name: name},
      success: function(data) {

        location.reload();
      }
    });
    return false;
  });
});
