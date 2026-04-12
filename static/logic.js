const passid = document.getElementById('passwordInput');
const butid = document.getElementById('buttonid');


butid.addEventListener('click', () =>{

    const brukerinput = passid.value;
    if (brukerinput === '') {
        console.log("Tomt felt")} 
    else {
        fetch('/check_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            password: brukerinput
        })
    })
    }

});