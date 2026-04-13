const passid = document.getElementById('passwordInput');
const butid = document.getElementById('buttonid');


butid.addEventListener('click', () =>{ //Utfører en handling når en bruker klikker på submit

    const brukerinput = passid.value; //Brukerinput er da lik verdien til passordet som er fylt inn.
    if (brukerinput === '') {
        console.log("Tomt felt")} 
    else {
        fetch('/check_password', { //URL lokasjon for API request til serveren. 
        method: 'POST', //metode som brukes, POST fordi vi skal sende til server, GET henter kun verdeir. 
        headers: {
            'Content-Type': 'application/json'
        }, //format
        body: JSON.stringify({
            password: brukerinput
        })
    })
    }

});