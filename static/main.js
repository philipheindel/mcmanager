document.querySelector("#btnCopyWorld").addEventListener("click", callCopyWorld);
document.querySelector("#btnStartServer").addEventListener("click", callStartServer);
document.querySelector("#btnStopServer").addEventListener("click", callStopServer);
document.querySelector("#txtServerIp").addEventListener("keyup", cacheServerIp);
document.querySelector("#txtServerPort").addEventListener("keyup", cacheServerPort);
document.addEventListener("DOMContentLoaded", function() {
    
    cacheServerIp();
    
    cacheServerPort();
 }, false);

//#region Helper Functions
function buildTargetUrl(path) {
    var serverIp = document.querySelector("#txtServerIp").value;
    var serverPort = document.querySelector("#txtServerPort").value;
    var targetUrl = "http://" + serverIp + ":" + serverPort + path;
    
    console.log("Built URL: " + targetUrl);

    return targetUrl;
}

function storeValue(key, value) {
    var cachedValue = window.localStorage.getItem(key);
    if (cachedValue === null || cachedValue === undefined || cachedValue === "" || cachedValue !== value) {
        window.localStorage.setItem(key, value);
    }

}
//#endregion Helper Functions

//#region Event Handlers
function callCopyWorld() {
    fetch(buildTargetUrl("/CopyWorld"), {
        method: "POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

function callStartServer() {
    fetch(buildTargetUrl("/StartServer"), {
        method: "POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

function callStopServer() {
    fetch(buildTargetUrl("/StopServer"), {
        method: "POST",
        mode: "cors",
        headers: {"Content-Type": "application/json"},
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}

function cacheServerIp() {
    storeValue("serverIp", document.querySelector("#txtServerIp").value);
}

function cacheServerPort() {
    storeValue("serverPort", document.querySelector("#txtServerPort").value);
}
//#endregion Event Handlers
