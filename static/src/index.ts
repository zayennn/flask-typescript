document.addEventListener('DOMContentLoaded', function() {
    const navbar: any = document.querySelector('.navbar__container')

    window.addEventListener('scroll', function() {
        if ( window.scrollY > 200 ) {
            console.log('scroll');
            navbar?.classList.add('active')
        } else {
            navbar?.classList.remove('active')
        }
    })
});