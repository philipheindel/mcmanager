document.querySelector("#btnSyncWorld").addEventListener("click", callSyncWorld);

function callSyncWorld() {
    fetch("/syncworld", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

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