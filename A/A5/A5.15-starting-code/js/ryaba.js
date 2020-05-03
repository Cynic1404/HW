const dataURL = "https://api.jsonbin.io/b/5e905926172eb643896166e7";


function init() {
	$("#button-fetch").click(handleButton);
}

var $yes;
var text = ""; 

$.getJSON(
  dataURL,
  function (data){
    // data.text.forEach(element => text+=(element+'<br>'));
    text = data.text.join('<br>');
    
  }
);


function handleButton(){
  var a = text;
  $( ".text" ).remove();
  // $('.form-control').each(function(){
  //   var name = this.name;
  //   var value = this.value;
  //   a = a.replace(name, value);
  // });

  let var1 = $("input[name=var1]").val();
  let var2 = $("input[name=var2]").val();
  let var3 = $("input[name=var3]").val();
  let var4 = $("input[name=var4]").val();
  let var5 = $("input[name=var5]").val();
  let var6 = $("input[name=var6]").val();
  let speach = $("input[name=speach]").val();
      // a = a.replace(/{var1}/g, var1);
      a = a.replace("{var1}", var1)
      a = a.replace(/{var2}/g, var2);
      a = a.replace(/{var3}/g, var3);
      a = a.replace(/{var4}/g, var4);
      a = a.replace(/{var5}/g, var5);
      a = a.replace(/{var6}/g, var6);
      a = a.replace(/{speach}/g, speach);
      $yes = $('<div class="text">'+a+'</div>');
      
      $yes.appendTo($('#result'))
    }

init()



const arrayOfArrays = [[], [], [1,2,3], [], [1,4]]
function notEmptyArray(arr) {
    return arr.filter(
        function(item) {
            return length(item)!== 0
    });
}

const newArr = notEmptyArray(arrayOfArrays);