document.addEventListener('DOMContentLoaded', function () {
    const spanNumber = document.querySelector('.number');
    let number = Number(spanNumber?.textContent) || 0;
    const increaseBtn = document.querySelector('.increase');
    increaseBtn.addEventListener('click', function () {
        number++;
        spanNumber.textContent = number.toString();
    });
});
export {};
//# sourceMappingURL=index.js.map