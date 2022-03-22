
### PRIMEROS PASOS


`create database nombreBaseDeDatos;`			Crear una base de datos

`drop database nombreBaseDeDatos;`			Eliminar una base de datos.

`use nombreBaseDeDatos;`					Indicarle a mysql que base de datos vamos a usar.


`create table nombreDeLaTabla(campos tipoDato, ...);`	crea una nueva tabla.
ejemplo:
`create table Usuario(id int, email varchar(255), userName varchar(50))`


### Tablas

`drop table nombreDeLaTabla` 				Eliminamos esa tabla

`alter table Usuario add edad int;` Agregamos una columna llamada edad a la tabla de Usuario.

`alter table Usuario drop column edad;` Eliminamos la columna edad de la tabla usuario.

`alter table Usuario modify column email varchar(50);` Cambiamos el tipo de dato de la columna email.