const buttonDrop = document.querySelector('.button-drop')
const navMenu = document.querySelector('.nav-menu')

buttonDrop.addEventListener('click', () => {
    buttonDrop.classList.toggle('active')
    navMenu.classList.toggle('active')
})