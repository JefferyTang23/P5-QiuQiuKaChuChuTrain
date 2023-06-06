function emenu() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");

    blind.style.display = "block";
    emenu.style.display = "block";
}

function unblind() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");

    blind.style.display = "none";
    emenu.style.display = "none";
}