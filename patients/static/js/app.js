$( document ).ready(function() {



  $(".close").click(function() {
      $("modal").css("display", "none");
      $(".modal").hide();
  });


$("#close").click(
  function() {
    $("modal").css("display", "none");
    $(".modal").hide();
  }
)



$("#mit-chan-delete").click( function () {
var id = $(".list-group-item-heading").attr("index")


  $.ajax({
        url: '/profile/ajax/delete_post',
        data: {
          'id': id,
        },
        dataType: 'json',
        success: function(data) {

          $("modal").css("display", "none");
          $(".modal").hide();


   $("[index=" + id + "]").prev().css("display","none");
   console.log( $("[index=" + id + "]").parent().css("display", "none"));
   $("[index=" + id + "]").parent().append("<p> No perscriptions </p>")

        },
      });





});

$("#mit-chan-submit").click( function () {
  var title = $("#modal-text").val();
  var body = $("#modal-msg").val();
  var query =  $(".list-group-item-heading").attr("index")



  $.ajax({
        url: '/profile/ajax/edit_post',
        data: {
          'title': title,
          'body': body,
          'query': query,
        },
        dataType: 'json',
        success: function(data) {

           $("[index=" + query + "]").text(data.new_note)
           $("[index=" + query + "]").next().text(data.new_message)




        },
      });





});



  $(".list-group-item ").click(function() {



    $(".modal").show();





  //  list-group-item-heading
  //  $("#title").text( $(this).find(".list-group-item-heading").text())
    $("#modal-text").val( $(this).find(".list-group-item-heading").text() )
    $("#modal-msg").val( $(this).find(".list-group-item-text").text() )

    var old_data =  $("#modal-msg").val()
    $("#mit-chan-hidden").val(old_data);







    $("modal").css("display", "block");



  });



});
