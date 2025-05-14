document.addEventListener('DOMContentLoaded', function () {
    const closeBtn = document.querySelector('.close-btn');
    const errorPopup = document.querySelector('.error-popup');

    if (closeBtn && errorPopup) {
        closeBtn.addEventListener('click', function () {
            errorPopup.style.display = 'none';
        });
    }
});