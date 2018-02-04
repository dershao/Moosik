$(document).ready(function() {
  $('#tweet-form').on('submit', function() {

    var name = $('#subheading').text();

    $('#btn-wrapper').hide();
    $('.loader').show();

    $.ajax({
      type: 'POST',
      url: '/twitter',
      data: {name: name},
      success: function(data) {

        $('#image').attr("src", data.imageUrl);
        $('#img-link').attr("href", data.trackUrl);
        $('#subheading').text('Moosik detected ' + data.sentiment);
        $('.loader').hide();
        $('#btn-wrapper').show();
      }
    });

    $('#img-link').on('click', function() {
      $(this).hide();
      window.location.replace("http://127.0.0.1:3000/app");
    });

    return false;
  });
});
