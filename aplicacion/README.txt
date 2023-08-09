Autor: Simon Valles
Titulo: Preentrega numero 3. 


Objetivo del trabajo practico entregado:

Este programa consiste en el diseño de una pagina web en la cual se pueden crear:

-Articulos a vender
-Cursos ofertados  
-Ofertas de instrumentos (Articulos con descuento especial)
-Partners (compañias con convenios comerciales)

El programa contiene en el apartado de VIEWS las funciones principales y sus correspondientes formularios.
Adicionalmente la funcion buscarComision.

------------------------------------------------------------------------------------------------------
                    ¿COMO EJECUTAMOS EL PROGRAMA?

Direccion url para accesar a la pagina de inicio http://127.0.0.1:8000/aplicacion/

Como funcionalidades tenemos las siguientes aplicaciones:

-Haciendo click en los botones en cabecera se puede acceder a:

ARTICULOS
CURSOS
OFERTAS
PARTNERS
BUSCAR COMISION
ADMINISTRACION

Cada boton redirecciona a una pagina que muestra los datos almacenados en nuestra base de datos.

-Para la carga de datos podemos usar tres metodos:

    1. Mediante entradas al Browser: 
        http://127.0.0.1:8000/aplicacion/articulos_form/
        http://127.0.0.1:8000/aplicacion/cursos_form/
        http://127.0.0.1:8000/aplicacion/ofertas_form/
        http://127.0.0.1:8000/aplicacion/partners_form/
    2. via DBbrowser. Cargando los datos em las tablas generadas para cada modelo.
    3. por ADMINISTRACION (usuario: admin - contraseña: admin)

--------------------------------------------------------------------------------------------------------

Para cumplir con la consigna en cuanto a la "busqueda" dentro de la base de datos se generó el template
buscarComision.html y podemos acceder a la información desde el boton "Buscar Comision" posicionado
en la pagina de inicio. 

El campo requerido es la comision. Ingresando una comision (ejemplo 9999) te muestra todos los datos:

ID 
CURSO 
COMISION 
NOMBRE DE ALUMNO INSCRITO (no tiene el nombre del tutor)


Esto nos redirecciona a una pagina en la cual se coloca el numero de comision y te devuelve todos los datos 
del curso, asociado a la comision buscada.

Fin! por ahora