$(document).ready(function () {
    // $("#nav-placeholder").load("../../templates/nav.html", () => {
    //     let n = document.querySelectorAll(".logged-in");
    //     let l = document.querySelectorAll(".logged-out");
    //     n.forEach(ele => {
    //         ele.style.display = 'block';
    //     });
    //     l.forEach(ele => {
    //         ele.style.display = 'none';
    //     });
    // })
    $('.modal').modal();
    console.log('Loaded video');
    
    $('.dropdown-trigger').dropdown();    
})