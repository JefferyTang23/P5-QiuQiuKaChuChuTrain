function emenu() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");

    console.log(emenu.style.display);

    blind.style.display = "block";
    emenu.style.display = "block";
}

function cmenu() {
    let blind = document.getElementById("blind");
    let cmenu = document.getElementById("cmenu");

    blind.style.display = "block";
    cmenu.style.display = "block";
}

function rmenu() {
    let blind = document.getElementById("blind");
    let rmenu = document.getElementById("rmenu");

    blind.style.display = "block";
    rmenu.style.display = "block";
}

function amenu() {
    let blind = document.getElementById("blind");
    let amenu = document.getElementById("amenu");

    blind.style.display = "block";
    amenu.style.display = "block";
}

function unblind() {
    let blind = document.getElementById("blind");
    let emenu = document.getElementById("emenu");
    let cmenu = document.getElementById("cmenu");
    let rmenu = document.getElementById("rmenu");
    let amenu = document.getElementById("amenu");

    blind.style.display = "none";
    emenu.style.display = "none";
    cmenu.style.display = "none";
    rmenu.style.display = "none";
    amenu.style.display = "none";
}