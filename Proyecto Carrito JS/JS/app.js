
const carrito = document.querySelector('#carrito');
const contenedorCarrito = document.querySelector('#lista-carrito tbody');
const listaCurso = document.querySelector('#lista-cursos');
const vaciarCarrito = document.querySelector('#vaciar-carrito');
let articulosCarrito = []; 

cargarEventlistener();
function cargarEventlistener(){
    //Al agregar un curso presionando "agregar carrito" pasa esto
    listaCurso.addEventListener('click', agregarCurso);
}

function agregarCurso(e){
    e.preventDefault();
    if (e.target.classList.contains('agregar-carrito')){
        const cursoSeleccionado = e.target.parentElement.parentElement
        leerDatosCurso(cursoSeleccionado);
    }
}
function leerDatosCurso(curso){
    const infoCurso = {
        imagen: curso.querySelector('img').src,
        titulo: curso.querySelector('h4').textContent,
        precio: curso.querySelector('.precio span').textContent,
        id: curso.querySelector('a').getAttribute('data-id'),
        cantidad: 1
    }
    articulosCarrito = [...articulosCarrito, infoCurso]

    function carritoHTML(){

        articulosCarrito.forEach(curso => {
            const {imagen, titulo, precio, cantidad, id} = curso;
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>
                    <img src = "${imagen}" width="100">
                </td>
                <td>${titulo}</td>
                <td>${precio}</td>
                <td>${cantidad}</td>
                <td>
                    <a href ="#" class="borrar-curso" data-id="${id}">x</a
                </td>
            `;
            contenedorCarrito.appendChild(row);            
    })
}
}
