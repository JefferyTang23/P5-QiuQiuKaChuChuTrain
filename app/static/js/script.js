function emenu() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");

    console.log(emenu.style.display);

    blind.style.display = "block";
    emenu.style.display = "flex";
}

function unblind() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");

    blind.style.display = "none";
    emenu.style.display = "none";
}