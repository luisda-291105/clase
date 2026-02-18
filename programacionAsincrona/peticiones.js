let contenedorPeliculas = document.querySelector("#contenedorPeliculas");
let button = document.querySelector("button");

button.addEventListener("click", () => {
    obtenerInfo();
});

function obtenerInfo() {
    // forma 1 then() - catch
    // let url = "https://jsonplaceholder.typicode.com/users";
    let url = "http://localhost/apiPosts/posts.txt";

    // metodo para realizar peticion
    fetch(url)
        .then((d) => d.json())
        .then((posts) => {
            posts.forEach((p) => {
                contenedorPeliculas.innerHTML += `
                    <div class="card my-5 mx-auto" style="width: 18rem;">
                        <div class="card-body">
                            <h5 class="card-title">${p.title}</h5>
                            <h6 class="card-subtitle mb-2 text-body-secondary">${p.userId}</h6>
                            <img src="${p.url}" class="card-img-top" alt="...">
                        </div>
                    </div>
                `;

            });
            console.log(posts)
        })
        .catch((e) => {
            console.error(e);
        });
}
