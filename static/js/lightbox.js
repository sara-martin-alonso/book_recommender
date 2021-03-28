
const lightbox = document.querySelector('.lightbox')

const lightboxImg = document.querySelector('.lightbox__img')

const lightboxIcon = document.querySelector('.lightbox__icon')


lightboxMini.forEach(function (cadaMini, i) {
    cadaMini.addEventListener('click', function () {
        lightbox.classList.add('ver')
        lightboxImg.src = this.src
    })
})
lightboxIcon.addEventListener('click', function () {
    lightbox.classList.remove('ver')
})

document.body.addEventListener('keydown', function (e) {
    console.log(e.key)
    if (e.key == 'Escape') {
        lightbox.classList.remove('ver')
    }
    
})
