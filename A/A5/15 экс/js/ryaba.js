const dataURL = "https://api.jsonbin.io/b/5e905926172eb643896166e7";
const fileds = ['var1','var2','var3','var4','var5','var6']

function get_froms(){
  let obj = {}
  fileds.forEach(function(field){
    obj[field]=$("input[name="+field+"]").val()
  })
  return obj;
}


function handleButton(){
  var text = ""; 
  $.getJSON(
    dataURL,
    function (data){
      $('#result').show();
    
      obj = get_froms()

      data.text.forEach(function(a){
        for (key in obj){
          a = a.replace("{" + key+ "}", obj[key]);
        };
        text = text+a+'<br>';
        $('form').hide();
        $('#result').html(text); 
    }
  );
})}

function init() {
  $("#button-fetch").click(handleButton);
  $('.zz').click(show);
}

function show(){
  $('form').show();
  $('#result').hide()
}



$(document).ready(init())



// const dataURL = "https://api.jsonbin.io/b/5e905926172eb643896166e7";





// function handleButton(){
//   var text = ""; 
//   $.getJSON(
//     dataURL,
//     function (data){
//       $('#result').show();
//       let obj = { 
//       var1 : $("input[name=var1]").val(),
//       var2 : $("input[name=var2]").val(),
//       var3 : $("input[name=var3]").val(),
//       var4 : $("input[name=var4]").val(),
//       var5 : $("input[name=var5]").val(),
//       var6 : $("input[name=var6]").val(),
//       speach : $("input[name=speach]").val()}

//       data.text.forEach(function(a){
//         for (key in obj){
//           a = a.replace("{" + key+ "}", obj[key]);
//         };
//         text = text+a+'<br>';
//         $('form').hide();
//         $('#result').html(text); 
//     }
//   );
// })}

// function init() {
//   $("#button-fetch").click(handleButton);
//   $('.zz').click(show);
// }

// function show(){
//   $('form').show();
//   $('#result').hide()
// }



// $(document).ready(init())
