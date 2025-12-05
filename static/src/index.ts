document.addEventListener('DOMContentLoaded', function() {
    const spanNumber = document.querySelector('.number') as HTMLSpanElement;
    let number: number = Number(spanNumber?.textContent) || 0;

    const increaseBtn = document.querySelector('.increase') as HTMLButtonElement;

    increaseBtn.addEventListener('click', function() {
        number++;
        spanNumber.textContent = number.toString();
    });
});