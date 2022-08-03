let menuBtn = document.getElementById('hamburger');
let mobMenu = document.getElementById('nav-items-mob')

let searchBtn = document.getElementById('search-control')


menuBtn.addEventListener('click', e => {
    if (document.getElementById('nav-items-mob').style.display == 'block') {
        return document.getElementById('nav-items-mob').style.display = 'none'
    } 
    
    return document.getElementById('nav-items-mob').style.display = 'block' 
})


searchBtn.addEventListener('click', e => {
    if (document.getElementById('search-form').style.display == 'block') {
        return document.getElementById('search-form').style.display = 'none'
    } 
    return document.getElementById('search-form').style.display = 'block'
})