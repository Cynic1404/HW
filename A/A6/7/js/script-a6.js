function init() { 

  $("input[type=checkbox]").change(trackChecks); 
  $("input[type=radio]").change(trackRadio); 
  trackChecks(); 
  trackRadio(); 
  console.log("скрипт подгрузился");
  // $("input[type=checkbox]").prop("disabled", true);
}

$(document).ready(init); 



const maxAllowedChecks = 2;

function trackChecks() {
  let checkCount = $("input[type=checkbox]:checked").length;
  $("input[type=checkbox]:not(:checked)").prop("disabled", checkCount >= maxAllowedChecks);
}


function trackRadio() {
  let checkRadio = $("input[type=radio]:checked").length;
  $("input[type=radio]:not(:checked)").prop("disabled", checkRadio === 1);

  }
