document.getElementById('priceForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let bedrooms = document.getElementById('bedrooms').value;
    let square_footage = document.getElementById('square_footage').value;
    let location = document.getElementById('location').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'bedrooms': bedrooms,
            'square_footage': square_footage,
            'location': location
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = 'Predicted Price: $' + data.predicted_price.toFixed(2);
    })
    .catch(error => console.error('Error:', error));
});
