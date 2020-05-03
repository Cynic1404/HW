let popa = document.querySelector('.aaa');
popa.addEventListener('mouseenter', showVis);
popa.addEventListener('mouseout', hideVis);

function showVis(){
    let vis=document.querySelector('.block');
    vis.classList.add('vis');
    console.log('showPopup работает');
}

function hideVis(){
    let vis=document.querySelector('.block');
    vis.classList.remove('vis');
    console.log('showPopup работает');
}