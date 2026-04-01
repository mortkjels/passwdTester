async function testFlask() {
    const response = await fetch("http://localhost:8250/");
    const text = await response.text();
    console.log(text);
}

testFlask();