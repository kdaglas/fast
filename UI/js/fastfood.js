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

function auth_for_user(){
    var user = document.getElementsByName('user');
    for (var k = 0, length = user.length; k < length; k++){
        if (user[k].checked){
            if(user[k].value == 'customer'){
                window.location.href = "home.html";
            }
            else if(user[k].value == 'admin'){
                window.location.href = "admin.html";
            }
            break;
        }
    }
}

function hideOrder() {
    document.getElementById("meal_card").style.display = "none";
}