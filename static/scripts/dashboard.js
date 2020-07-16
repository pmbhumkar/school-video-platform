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
    $('.collapsible').collapsible();
    
    
    $('.dropdown-trigger').dropdown();    
})

// $("#cp1").click(() => {
//     selection = document.querySelector('#selector');
//     selection.style.display = 'none';

//     video = document.querySelector('#video-player');
//     video.style.display = 'block';
//     url = "{{ url_for('static', filename='videoFile.mp4') }}";
//     // url = "../videoFile.mp4"
//     iframe = document.querySelector('#player');
//     iframe.src = url;

// })

// $("#back").click(() => {
//     selection = document.querySelector('#selector')
//     selection.style.display = 'block'

//     video = document.querySelector('#video-player')
//     video.style.display = 'none'
// })

