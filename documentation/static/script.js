// Function menampilkan sidebar
document.querySelector('#menu').onclick = () => {

    const displayNavbar = document.querySelector('#navbar');
    const menuClose = document.querySelector('#close');
    const menu = document.querySelector('#menu')

    displayNavbar.style.right = "0";
    displayNavbar.style.transition = "0.5s"
    menuClose.style.display = "block";
    menu.style.display = "none";
}


// Function untuk menutup sidebar
document.querySelector('#close').onclick = () => {
    const displayNavbar = document.querySelector('#navbar');
    const menuClose = document.querySelector('#close');
    const menu = document.querySelector('#menu')

    displayNavbar.style.right = "-100%";
    menuClose.style.display = "none";
    menu.style.display = "block";
}