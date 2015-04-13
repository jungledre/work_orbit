$(function() {
  $('.inputTime').on("click", function(e) {
    e.preventDefault();
    var time = $(this).val();
    var mode = $("#inputMode").val();
    var location = $("#inputLocation").val();

    if (location.length <= 20) {
      $('#alert').toggleClass("hidden").delay(2000).queue(function() { $(this).toggleClass("hidden"); });
    } else{
    $.ajax({
      method: "post",
      url:'/process',
      data: '',
      success: function(result) {
        window.location='/map/'+ time + '/' + mode + '/' + location;
      }
    })
  }
  })
})
