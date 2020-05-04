const maxHits = 10  ;

let hits = 0;
let firstHitTime;
let lastHitTime;
let counter = 1;
let errorscounter = 0;

function round() {
  // FIXME: надо бы убрать "target" прежде чем искать новый

  let divSelector = randomDivId();
  console.log(divSelector)
  $(divSelector).addClass("target");
  $(divSelector).text(counter);
  // TODO: помечать target текущим номером

  // FIXME: тут надо определять при первом клике firstHitTime

  if (hits === maxHits) {
    lastHitTime = getTimestamp();
    console.log("last click" , lastHitTime);
    endGame();
  }
}

function endGame() {
  // FIXME: спрятать игровое поле сначала
  reset()
  let totalPlayedMillis = getTimestamp() - firstHitTime;
  console.log('vo', totalPlayedMillis)
  let totalPlayedSeconds = (totalPlayedMillis / 1000).toFixed(0);
  $("#total-time-played").text(totalPlayedSeconds);
  $("#errors").text(errorscounter);
  $("#win-message").removeClass('d-none')
  $(".game-field").hide()
  
}

function handleClick(event) {
  // FIXME: убирать текст со старых таргетов. Кажется есть .text?
  if ($(event.target).hasClass("target")) {
    hits = hits + 1;
    reset()
    counter+=1;
    round();
  } else
  {  
    $(event.target).addClass("miss");
    errorscounter +=1;
  }
    
  }
  // TODO: как-то отмечать если мы промахнулись? См CSS класс .miss


function init() {
  // TODO: заказчик просил отдельную кнопку, запускающую игру а не просто по загрузке
  round();
  $(".game-field").hide();
  $(".game-field").click(handleClick);
  $("#button-reload").click(function() {
    $(".game-field").show();
    hits = 0;
    counter = 1;
    reset()
    round()
    firstHitTime = getTimestamp();
    errorscounter =0;
    $('#win-message').addClass('d-none')
    });
}

function reset(){
  $('.game-field').removeClass("target");
  $('.game-field').text("")
  $('.game-field').removeClass("miss");
}

$(document).ready(init);
