function getElement(selector) {
    const element = document.querySelector(selector);
    if (element && element instanceof HTMLElement) {
        return element;
    }
    return null;
}
function activateNavbar(navbar) {
    if (!navbar.classList.contains('active')) {
        navbar.classList.add('active');
        console.log('Navbar activated: scroll');
    }
}
function deactivateNavbar(navbar) {
    if (navbar.classList.contains('active')) {
        navbar.classList.remove('active');
        console.log('Navbar deactivated: scroll up');
    }
}
function handleScroll(navbar) {
    const scrollTrigger = 200;
    const currentScroll = window.scrollY || window.pageYOffset;
    if (currentScroll > scrollTrigger) {
        activateNavbar(navbar);
    }
    else {
        deactivateNavbar(navbar);
    }
}
document.addEventListener('DOMContentLoaded', function () {
    const navbar = getElement('.navbar__container');
    if (!navbar) {
        console.warn('Navbar element not found.');
        return;
    }
    handleScroll(navbar);
    window.addEventListener('scroll', function () {
        let timer;
        return function (e) {
            if (timer) {
                clearTimeout(timer);
            }
            timer = window.setTimeout(() => {
                handleScroll(navbar);
            }, 10);
        };
    }());
});
export {};
//# sourceMappingURL=index.js.map