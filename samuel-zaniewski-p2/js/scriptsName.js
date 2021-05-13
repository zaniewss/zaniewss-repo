function init(){
    document.getElementById('Generate-Name').onclick = randomName();
}

function randomName(){
    document.getElementById('content2').textContent = "";
    var num = 0;
    num = Math.floor(Math.random() * 5);
        
    if (num = 0 ){
        document.getElementById('content2').textContent = "Aerphix";
    } else if (num = 1 ){
        document.getElementById('content2').textContent = "Cynderboom";
    } else if (num = 2 ){
        document.getElementById('content2').textContent = "Lemonzinger";
    } else if (num = 3 ){
        document.getElementById('content2').textContent = "Smemmers";
    } else if (num = 4 ){
        document.getElementById('content2').textContent = "Denimchicken";
    } else if (num = 5 ){
        document.getElementById('content2').textContent = "Exophase";
    }    
}

init();