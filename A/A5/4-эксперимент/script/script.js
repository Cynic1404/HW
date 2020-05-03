let popa = document.querySelector('.header');
popa.addEventListener('mouseenter', header);
popa.addEventListener('mouseout', header2);

function header(){
    let vis=document.querySelector('.main');
    vis.classList.add('flex-column-reverse');
    vis.classList.remove('flex-column');
}

function header2(){
    let vis=document.querySelector('.main');
    vis.classList.remove('flex-column-reverse');
    vis.classList.add('flex-column');
}


let zalupa = document.querySelector('.menu');
zalupa.addEventListener('mouseenter', menu);
zalupa.addEventListener('mouseout', menu2);

function menu(){
    let zzz=document.querySelector('.content');
    zzz.classList.add('d-flex');
    zzz.classList.add('flex-row-reverse');
}

function menu2(){
    let zzz=document.querySelector('.content');
    zzz.classList.remove('d-flex');
    zzz.classList.remove('flex-row-reverse');
}


let govno = document.querySelector('.last');
govno.addEventListener('mouseenter', gg);
govno.addEventListener('mouseout', gg2);

function gg(){
    let ooo=document.querySelector('.zz');
    ooo.classList.remove('flex-column');
    ooo.classList.add('flex-column-reverse');
}

function gg2(){
    let lll=document.querySelector('.zz');
    lll.classList.remove('flex-column-reverse');
    lll.classList.add('flex-column');
}