$(function() {
  $('.inputTime').on("click", function(e) {
    e.preventDefault();
    var time = $(this).val();
    var mode = $("#inputMode").val();
    var location = $("#inputLocation").val();

    $.ajax({
      method: "post",
      url:'/process',
      data: '',
      success: function(result) {
        window.location='/map/'+ time + '/' + mode + '/' + location;
      }
    })
  })
})
