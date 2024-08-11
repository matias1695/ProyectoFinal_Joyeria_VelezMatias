Proyecto Final-Joyeria- Velez Matias

El Proyecto Joyas es una plataforma diseñada para facilitar la administración integral de un local comercial dedicado a la venta de joyas. Este proyecto ha sido desarrollado para ofrecer una solución completa que permita gestionar cada aspecto del negocio, desde el manejo de inventario hasta la administración de ventas y tareas del personal.

Clases Principales del Proyecto
Artículos: Permite la gestión del inventario de joyas, incluyendo la carga de nuevos artículos, la consulta, el listado completo y el borrado de productos obsoletos o vendidos.

Clientes: Facilita la administración de la base de datos de clientes, permitiendo agregar nuevos clientes, listar los existentes y gestionar la información de cada uno.

Ventas: Centraliza el control de las transacciones de ventas, desde la creación de nuevas ventas hasta la generación de listados de ventas realizadas.

Tareas: Herramienta para asignar y gestionar las tareas del personal, garantizando un seguimiento efectivo de las labores diarias en el local.


Arquitectura del Proyecto

El proyecto se estructura de la siguiente manera: una aplicación llamada AppJoyeria, donde se encuentran todas las funcionalidades mencionadas anteriormente, y otra aplicación llamada accounts, que se encarga de manejar todo lo relacionado con los usuarios, incluyendo el inicio de sesión y la edición de los perfiles.

Instrucciones para Pruebas
Para realizar pruebas en el proyecto, sigue estos pasos:

Inicia el servidor de desarrollo con el comando python manage.py runserver.
Accede a la aplicación utilizando la URL: http://127.0.0.1:8000.
Una vez realizado lo anterior, serás dirigido directamente al login de nuestra página, donde podrás consultar la página "About Us" a través de un botón ubicado en la esquina superior izquierda. Esta página ofrece un resumen del proyecto.

Para iniciar sesión, puedes utilizar uno de los siguientes usuarios:

rufo25 → mati1995

matias16 → 16jun1995

También puedes crear un usuario nuevo. Estos usuarios son de tipo estándar, por lo que no podrán eliminar elementos de ningún listado, pero sí podrán editar sus datos y subir una imagen de avatar.

Para iniciar sesión como administrador, utiliza el siguiente usuario:

admin → mati1995

Una vez iniciada la sesión, podrás desplazarte por la plataforma y sus diferentes vistas, donde podrás realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en todas nuestras clases principales: Artículos, Ventas, Clientes y Tareas.
