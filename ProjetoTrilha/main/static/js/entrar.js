let bnt = document.querySelector('#logar');
let fecha = document.querySelector('#fecha');
bnt.addEventListener('click',()=>{
    let mc = document.querySelector('#main-container').style.display = 'none'
    let lg = document.querySelector('#login').style.display = 'flex'
})
fecha.addEventListener('click',()=>{
    let mc = document.querySelector('#main-container').style.display = 'inline-block'
    let lg = document.querySelector('#login').style.display = 'none'
})