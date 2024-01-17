const apiKey = "b2a0cf072e2a1d9876bd86f507e546a7";
const apiURL = "https://api.openweathermap.org/data/2.5/weather?units=metric";


function titleCase(str) {
    return str.replace(/\w\S*/g, function(word) {
        return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    });
}

async function getWeather (city) {
    var response = await fetch(apiURL + `&q=${city}` + `&appid=${apiKey}`);
    var data = await response.json();

    if (response.status == 404) {
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    } else {
        document.querySelector(".city-name").innerHTML = data.name;
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + "km/h";
        document.querySelector(".weather-icon").src = `images/${titleCase(data.weather[0].main)}.png`;

        document.querySelector(".weather").style.display = "block";
        document.querySelector(".error").style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function() {
    let searchBtn = document.querySelector(".search button")
    searchBtn.style.transition = "transform 0.2s ease-in-out";

    searchBtn.addEventListener('mousedown', () => {
        searchBtn.style.transform = "scale(0.8)";
    });

    searchBtn.addEventListener('mouseup', ()=> {
        searchBtn.style.transform = "scale(1)";
        let cityName = document.querySelector(".search input").value;

        if (cityName) {
            getWeather(cityName)
        } else {
            getWeather("delhi")
        }
    });
});
