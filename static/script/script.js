// PIRMINIS HOMEPAGE veikiantis:
document.addEventListener('DOMContentLoaded', () => {
    if ('geolocation' in navigator) {
        navigator.geolocation.getCurrentPosition(function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            fetch(`/get_weather_data?lat=${latitude}&lon=${longitude}`)
                .then(response => response.json())  
                .then(data => {
                    if (data) {
                        document.querySelector('#latitude').textContent = latitude.toFixed(2);
                        document.querySelector('#longitude').textContent = longitude.toFixed(2);
                        document.querySelector('#temp').textContent = data.temperature;
                        document.querySelector('#windSpeed').textContent = data.wind_speed;
                        document.querySelector('#humidity').textContent = data.humidity;
                        document.querySelector('#cloudCover').textContent = data.cloud_cover;
                        document.querySelector('#precipitation').textContent = data.precipitation;
                    } else {
                        console.error('JSON structure is wrong:', data);
                    }
                })
                .catch(error => console.error('Error fetching weather data:', error));
        });
    }
});


document.querySelector('#deleteCityButton').addEventListener('click', event => {
    event.preventDefault();

    if (confirm('Are you sure you want to delete this city?')) {
        window.location.href = document.querySelector('#deleteCityButton').dataset.url;
    }
});