const sidebar = document.querySelector('.sidebar');
const menuBtn = document.getElementById('menuToggle');

menuBtn.addEventListener('click', () => {
    sidebar.style.left = "0px";
});

document.addEventListener('click', (event) => {
    const isClickInside = sidebar.contains(event.target) || menuBtn.contains(event.target);

    if (!isClickInside) {
        sidebar.style.left = "-172px";
    }
});