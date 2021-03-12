const timeWarn = document.getElementsByClassName('timeWarn')
console.log('1')
const form = document.getElementById('form');
console.log('2')
const front__p = document.getElementsByClassName('front__p')
console.log('3')
const lightboxMini = document.querySelectorAll('.graphs__img')
console.log('4')

const read_more = document.getElementsByClassName('open_descr')
console.log('8')
const full_descr = document.getElementsByClassName('book__descr--open')
console.log('9')
const short_descr = document.getElementsByClassName('book__descr')
console.log('10')
const collapse = document.getElementsByClassName('close_descr')
console.log('11')
const i_open_info = document.getElementsByClassName('fa-info-circle')
console.log('12')
const info_panel = document.getElementsByClassName('info__container')
console.log('13')
const i_close_info = document.getElementsByClassName('fa-times-circle')
console.log('14')

form.addEventListener('submit', function () {
    timeWarn[0].classList.add('show')
    front__p[0].classList.add('move')
    setTimeout(() => {
        timeWarn[0].classList.remove('show')
        front__p[0].classList.remove('move')
    }, 10000);
})
console.log('18')
for (let i = 0; i < read_more.length; i++) {
    const element = read_more[i];
    element.addEventListener('click', function () {
        full_descr[i].classList.add('show')
        element.classList.add('hide')
        collapse[i].classList.add('show')
    })
}
console.log('19')
for (let i = 0; i < collapse.length; i++) {
    const element = collapse[i];
    element.addEventListener('click', function () {
        full_descr[i].classList.remove('show')
        read_more[i].classList.remove('hide')
        element.classList.remove('show')
    })
}
console.log('20')
i_open_info[0].addEventListener('click', function () {
    info_panel[0].classList.add('show')
})
console.log('21')
i_close_info[0].addEventListener('click', function () {
    info_panel[0].classList.remove('show')
})

console.log('22')


