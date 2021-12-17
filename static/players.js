let playerInput = document.querySelector("#playerName");
let addPlayerButton = document.querySelector("#addPlayerButton");

addPlayerButton.addEventListener("click", addPlayer);

function addPlayer() {
    let action = "add";
    submitPlayer(action, playerInput.value);
}

function submitPlayer(action, player) {
    let data = {
        "action" : action,
        "player" : player
    }

    fetch("/whitelist", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    }).then(res => {
        console.log("Request complete! response:", res);
    });
}
