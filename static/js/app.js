const read_more = document.getElementsByClassName('open_descr')
const full_descr = document.getElementsByClassName('book__descr--open')
const short_descr = document.getElementsByClassName('book__descr')
const collapse = document.getElementsByClassName('close_descr')

for (let i = 0; i < read_more.length; i++) {
    const element = read_more[i];
    element.addEventListener('click', function () {
        full_descr[i].classList.add('show')
        element.classList.add('hide')
        collapse[i].classList.add('show')
    })
}

for (let i = 0; i < collapse.length; i++) {
    const element = collapse[i];
    element.addEventListener('click', function () {
        full_descr[i].classList.remove('show')
        read_more[i].classList.remove('hide')
        element.classList.remove('show')
    })
}

const i_open_info = document.getElementsByClassName('fa-info-circle')
const info_panel = document.getElementsByClassName('info__container')
const i_close_info = document.getElementsByClassName('fa-times-circle')

i_open_info[0].addEventListener('click', function () {
    info_panel[0].classList.add('show')
})

i_close_info[0].addEventListener('click', function () {
    info_panel[0].classList.remove('show')
})





const lightboxMini = document.querySelectorAll('.graphs__img')
const lightbox = document.querySelector('.lightbox')
const lightboxImg = document.querySelector('.lightbox__img')
const lightboxIcon = document.querySelector('.lightbox__icon')



lightboxMini.forEach(function (cadaMini, i) {
    cadaMini.addEventListener('click', function () {
        lightbox.classList.add('ver')
        lightboxImg.src = this.src
    })
})


lightboxIcon.addEventListener('click', function(){
    lightbox.classList.remove('ver')
})

document.body.addEventListener('keydown', function(e){
    console.log(e.key)
    if (e.key == 'Escape'){
        lightbox.classList.remove('ver')
    }

})


const anim_book = document.querySelector('.fa-book-open')

anim_book.addEventListener('mouseover',function(){
    anim_book.classList.add('animate')
    setTimeout(() => {
        anim_book.classList.remove('animate')  
    }, 1001);    
})