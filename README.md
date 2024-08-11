Proyecto Joyas

El "Proyecto Joyas" es una plataforma que busca llevar la administración de un local comercial dedicado a la venta de joyas. Nuestro proyecto consta de 3 clases:

Artículos

Clientes

Ventas En estas clases, el usuario podrá realizar las gestiones de cada uno de los ítems antes mencionados (carga, consulta, borrado).

Lo anterior se encuentra en project_joyeria\AppJoyeria\models.py.

En el archivo project_joyeria\AppJoyeria\views.py se encuentran las funciones de cada una de nuestras vistas.

En el archivo project_joyeria\AppJoyeria\urls.py se encuentran cada uno de los paths para poder acceder a cada uno de nuestros templates.

Para realizar las pruebas, pueden hacerlo de la siguiente manera:

Ya con el servidor corriendo (python manage.py runserver), usar la siguiente URL: http://127.0.0.1:8000/AppJoyeria/, donde en el margen superior de la pantalla habrá 4 opciones (INICIO ARTÍCULOS - VENTAS - CLIENTES). Presionando cualquiera de ellas, los llevará a la página donde estarán los accesos directos a cada funcionalidad.
**No hay un orden específico para probar las funciones. Lo único que hay que tener en cuenta es que lo correspondiente a los Artículos ya tiene todo lo solicitado funcionando (carga, búsqueda, listado). En cambio, lo que corresponde a Clientes y Ventas solo tiene carga y listado.