document.querySelector("#dayButton").addEventListener("click", setDay);
document.querySelector("#weatherButton").addEventListener("click", setWeather);

function setDay() {
    let data = {
        "action" : "set",
        "time" : "day"
    }

    fetch("/time", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

function setWeather() {
    let data = {
        "weather" : "clear"
    }

    fetch("/weather", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}