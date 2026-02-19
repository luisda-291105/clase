
const peliculas = [
    {
        id: 1,
        titulo: "El Origen",
        sinopsis:
            "Un ladrón especializado en infiltrarse en los sueños recibe la tarea de implantar una idea en la mente de un empresario.",
        genero: "Ciencia ficción",
        lanzamiento: "2010-07-16",
        imagen: "https://ejemplo.com/imagenes/el-origen.jpg",
    },
    {
        id: 2,
        titulo: "Titanic",
        sinopsis:
            "Dos jóvenes de diferentes clases sociales se enamoran a bordo del famoso transatlántico durante su trágico viaje inaugural.",
        genero: "Romance / Drama",
        lanzamiento: "1997-12-19",
        imagen: "https://ejemplo.com/imagenes/titanic.jpg",
    },
    {
        id: 3,
        titulo: "Avengers: Endgame",
        sinopsis:
            "Los Vengadores se reúnen una vez más para revertir las acciones de Thanos y restaurar el equilibrio del universo.",
        genero: "Acción / Superhéroes",
        lanzamiento: "2019-04-26",
        imagen: "https://ejemplo.com/imagenes/endgame.jpg",
    },
    {
        id: 4,
        titulo: "Coco",
        sinopsis:
            "Un niño que sueña con ser músico viaja accidentalmente al mundo de los muertos para descubrir la verdad sobre su familia.",
        genero: "Animación / Familiar",
        lanzamiento: "2017-11-22",
        imagen: "https://ejemplo.com/imagenes/coco.jpg",
    },
    {
        id: 5,
        titulo: "Joker",
        sinopsis:
            "La historia del origen de Arthur Fleck, un hombre marginado que evoluciona hasta convertirse en el icónico villano.",
        genero: "Drama / Thriller",
        lanzamiento: "2019-10-04",
        imagen: "https://ejemplo.com/imagenes/joker.jpg",
    },
];




// forma 1
function ObtenerPelicula(pelicula) {
    // promesa para esperar el resultado de peliculas
    return new Promise((resolve, reject) => {
        // simular tiempo de peliculas
        setTimeout(() => {
            // sino tiene datos
            if (pelicula.length == 0) {
                reject("error: no hay datos en la bd");
            } else {
                // si tiene datos
                resolve(peliculas);
            }
        }, 2000);
    });
}

// es similar ar try catch de java 
ObtenerPelicula(peliculas).then((p)=> {
    // en caso de que no tenga error 
    console.log(p)
}).catch((e) => {
    // en caso de que tenga error
    console.error(e)
})




// forma 2

async function mostrarPelicula(pelicula) {
    try {
        // al usar await la variable espera que el tiempo necesario para que se ejecute
        let movies = await ObtenerPelicula(pelicula)
        console.log(movies)
    } catch (error) {
        console.error(error)
    }
}

mostrarPelicula(peliculas)