// /static/js/script.js

document.getElementById('doorbellButton').addEventListener('click', function() {
    fetch('/doorbell', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMessage').innerText = data.message;
    })
    .catch(error => {
        document.getElementById('responseMessage').innerText = 'Hubo un error al intentar activar el timbre.';
    });
});
