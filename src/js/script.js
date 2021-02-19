var input = document.getElementById("ipAddress");

input.addEventListener("input", updateInput);

function updateInput() {
    input.value = input.value.replace(" ", ".")
}

function connect() {
    eel.connect(input.value)
    window.location.pathname = "/app.html"
}