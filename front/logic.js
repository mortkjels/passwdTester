const passid = document.getElementById('passwordInput');
const butid = document.getElementById('buttonid');


butid.addEventListener('click', () =>{

    const brukerinput = passid.value;
    if (brukerinput === '') {
        console.log("Feltet er tomt");} 
    else {
        console.log("Du skrev inn: " + brukerinput);
    }

});