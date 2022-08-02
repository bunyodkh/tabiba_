let menuBtn = document.getElementById('hamburger');
let mobMenu = document.getElementById('nav-items-mob')

menuBtn.addEventListener('click', e => {
    if (document.getElementById('nav-items-mob').style.display == 'none') {
        document.getElementById('nav-items-mob').style.display = 'block'
    } else {
        document.getElementById('nav-items-mob').style.display = 'none'
    }  
})