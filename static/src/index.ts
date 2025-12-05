function getElement<T extends HTMLElement>(selector: string): T | null {
    const element = document.querySelector(selector);
    if (element && element instanceof HTMLElement) {
        return element as T;
    }
    return null;
}

function activateNavbar(navbar: HTMLElement): void {
    if (!navbar.classList.contains('active')) {
        navbar.classList.add('active');
        console.log('Navbar activated: scroll');
    }
}

function deactivateNavbar(navbar: HTMLElement): void {
    if (navbar.classList.contains('active')) {
        navbar.classList.remove('active');
        console.log('Navbar deactivated: scroll up');
    }
}

function handleScroll(navbar: HTMLElement): void {
    const scrollTrigger = 200;
    const currentScroll = window.scrollY || window.pageYOffset;
    if (currentScroll > scrollTrigger) {
        activateNavbar(navbar);
    } else {
        deactivateNavbar(navbar);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const navbar = getElement<HTMLDivElement>('.navbar__container');
    if (!navbar) {
        console.warn('Navbar element not found.');
        return;
    }

    handleScroll(navbar);

    window.addEventListener('scroll', function() {
        let timer: number | undefined;
        return function(this: Window, e: Event) {
            if (timer) {
                clearTimeout(timer);
            }
            timer = window.setTimeout(() => {
                handleScroll(navbar);
            }, 10);
        };
    }());
});