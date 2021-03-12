
const lightbox = document.querySelector('.lightbox')
console.log('5')
const lightboxImg = document.querySelector('.lightbox__img')
console.log('6')
const lightboxIcon = document.querySelector('.lightbox__icon')
console.log('7')

lightboxMini.forEach(function (cadaMini, i) {
    cadaMini.addEventListener('click', function () {
        lightbox.classList.add('ver')
        lightboxImg.src = this.src
    })
})
console.log('15')
lightboxIcon.addEventListener('click', function () {
    lightbox.classList.remove('ver')
})
console.log('16')

document.body.addEventListener('keydown', function (e) {
    console.log(e.key)
    if (e.key == 'Escape') {
        lightbox.classList.remove('ver')
    }
    
})
console.log('17')