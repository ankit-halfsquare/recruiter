function add() {
    var form = document.getElementById("myForm");
    var serializedData = $(form).serialize();
    console.log("serializedData",serializedData)
    var method = "POST";
    //var Url = " {% url 'v-0.9.1/project-listCreateAPI-View' %}";
    var Url = url
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr("value");
    $.ajax({
      method: method,
      url: Url,
      data: serializedData,
      headers: { "X-CSRFToken": crf_token },
    })
      .done(function (msg) {
        console.log("msg", msg);
        //launch_toast();
        window.location.href = window.location.href;
      })
      .fail(function (error) {
        console.log("error", error.responseJSON);
      });
  }