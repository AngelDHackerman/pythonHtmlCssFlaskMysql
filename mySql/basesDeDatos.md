
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

### Insertar registros.

`insert into Usuario (email, userName)
values ('angel@angel.com', 'chanchitoFeliz')` 			Con esto agregamos info a email y a userName.

`delete from Usuario where email = 'angel@angel.com' limit 1` 	Elimina el campo donde email es angel@angel.com

`alter table Usuario add primary key (id);` 					Agregamos una llave primaria al campo id.

`alter table Usuario modify column id int auto_increment;` 		Asi le decimos al campo id que es auto incrementado.

`select * from Usuario;` 

`select * from Usuario where email = 'felipe@chanchito.com';`

`select * from Usuario where edad < 31;` 

`update Usuario set edad = 32 where id = 1;` 

`delete from Usuario where id = 1; ` 