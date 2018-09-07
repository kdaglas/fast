function showRice() { 
        document.getElementById('rice').style.display = "block";
}

function showMatooke() { 
    document.getElementById('matooke').style.display = "block";
}

function showPosho() { 
    document.getElementById('posho').style.display = "block";
}

function showPotatoes() { 
    document.getElementById('potatoes').style.display = "block";
}

function showSpaghetti() { 
    document.getElementById('spaghetti').style.display = "block";
}

function showFries() { 
    document.getElementById('fries').style.display = "block";
}

function showJunk() { 
    document.getElementById('junk').style.display = "block";
}

function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}