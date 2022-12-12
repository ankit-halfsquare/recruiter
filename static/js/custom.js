function add() {
  //var name=$$("name").getValue();
   var form = document.getElementById("myForm");
   var serializedData = $(form).serialize();
  console.log("serializedData",serializedData)
  var method = "POST";
  //var Url = " {% url 'v-0.9.1/project-listCreateAPI-View' %}";
  var Url = url
  //console.log(name,url);
    var crf_token = $('[name="csrfmiddlewaretoken"]').attr("value");
    elem = document.getElementById("loader")
    elem.style.visibility = "visible"
    $.ajax({
      method: method,
      url: Url,
      data: serializedData,
      headers: { "X-CSRFToken": crf_token },
    })
      .done(function (msg) {
      document.getElementById('name').value = '';

        console.log("msg", msg);
        elem.style.visibility = "hidden"
        //$$("tableId").clearAll()
        $$("tableId").load(Url);
        $$("tableId").render();
        $$("tableId").refresh();

        //launch_toast();
        //window.location.href = window.location.href;
      })
      .fail(function (error) {
        console.log("error", error.responseJSON);
      });
  }