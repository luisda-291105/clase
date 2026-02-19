function odtenerDatos() {
    const url = "https://jsonplaceholder.typicode.com/photos"

    fetch(url)
    .then((dato)=> dato.json())
    .then((dato) => {
        console.log(dato)
    })
    .catch((e)=>{
        console.error(e)
    })
}



const btn = document.querySelector("button");

btn.addEventListener("click", odtenerDatos )