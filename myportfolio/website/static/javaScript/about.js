const boxes = document.querySelectorAll('.box');
window.addEventListener('scroll', checkBoxes)
checkboxes()

function checkBoxes() {
    const triggerBottom = window.innerHeight / 5 * 3
    boxes.forEach(box => {
        const boxTop = box.getBoundingClientRect().top
        if (boxTop < triggerBottom) {
            box.classList.add('show')
        }
        else
        {
            box.classList.remove('show')
        }
    })
}

// let button1 = document.getElementById('icnbtn');

// function hide() {
//     box
// }