if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

let intervalid = null;

function count() {
    let counter = parseInt(localStorage.getItem('counter'));
    counter++;

    localStorage.setItem('counter', counter);
    document.querySelector('h1').innerHTML = counter;

    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }

}

document.addEventListener('DOMContentLoaded', function () {

    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('#start').onclick = function () {
        // evita multiples intervalos
        if (intervalid === null) {
            intervalid = setInterval(count, 1000);
        }
    };

    document.querySelector('#stop').onclick = function () {
        clearInterval(intervalid);
        intervalid = null;
    };

    document.querySelector('#clear').onclick = function () {
        // detener el contador si esta corriendo
        clearInterval(intervalid);
        intervalid = null;
        // reiniciar contador
        localStorage.setItem('counter', 0);
        document.querySelector('h1').innerHTML = 0;
    };
});

