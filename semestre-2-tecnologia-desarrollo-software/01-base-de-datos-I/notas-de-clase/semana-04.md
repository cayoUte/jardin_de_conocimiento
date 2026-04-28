SELECT col1 col2 frmo  nombre de la tabla

DISTINCT
devolver valores distintos(diferentes)

SELECT DISTINCT 
col
FROM nombre tabla

where SE USA filtrar las filas devueltas para una query
SELECT  lista_columna
FROM    nombre_tabla
WHERE   condicion;

ORDER BY se usa para ordenar el conjunoo de resultados en asc odes

SELECT lista col
FOM nombre_tabla
ORDER BY col ASC | DESC // por defecto ordena asc;

tip: no poner en una sola linea, identar siempre.


# ------------- DML ----------------------------------------------------------

## INSERT INTO

La instruccion **INSERT INTO** se usa principalmente para aggregar una o mas filas a la tabla de una bd

**INSERT INTO** table_nme (col1, coln)

**VALUES**(val1, val2, val3, ... , valn) // la insercion debe mapearse por posicion del argumento.

**INSERT INTO** table_nme (col1, coln)

**VALUES**(val1, val2, val3, ... , valn),
        (val1, val2, val3, ... , valn), // la coma indica el fin de la fila
            (val1, val2, val3, ... , valn);

La instruccion **UPDATE** se usa para actualiza registros existentes en una tabla, en un motor de bd 

Sintaxis
**UPDATE** nombre_tabla
**SET** column1 = expresion1, // SET indica que columna quieres cambiar
    column2 = expresion2

**WHERE** condicion // simpre poner where, caso contrario actualiza todas las columnas de la tabla

La instrccion DELETE se usa para eliminar registros existentes en una tabla

**DELETE FROM** nombre_tabla
**WHERE** condicion

-- universidad last_updateNomvre:
-- Docente Ing. Cristian ivadeneira MSc
-- Fecha: 28/04/2026
-- Tema: DDL - DML

select first_name, last_name from actor limit 10;
select addres_id, address, address2, distinct, city_id, postal_code, phone, location, last_update from address limit 10;
select category_id, name, last_update from category limit 10;
select city_id, city, country_id, last_update from city limit 10;
select country_id, country, last_update from country limit 10;
select customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update from customer limit 10;
select film_id, title, description, reease_year, language_id, original_language, rental_duration, rental_rate, lenght, replacement_cost, rating, special_features,  last_update from film limit 10;
select actor_id, film_id, last_update from film_actor limit 10;
select actor_id, film_id, last_update from film_category limit 10;
DESCRIBE actor;
select film_id, title, description from film_text limit 10;
select inventory_id, film_id, store_id from inventory limit 10;
select language_id, name, last_update from language limit 10;
select first_name, last_name from payment limit 10;
select first_name, last_name from rental limit 10;
select first_name, last_name from staff limit 10;
select first_name, last_name from store limit 10;

