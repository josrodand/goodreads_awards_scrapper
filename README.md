# GoodReads Awards Scrapper

Proyecto de Web Scrapping para lectura de datos de libros desde el sitio web www.goodreads.com.

## Descripción

Este proyecto ha sido desarrollado para la asignatura Tipología y ciclo de vida de los Datos, para el Master Universitario en Ciencia de Datos de la Universitat Oberta de Catalunya.

## Miembros del Equipo

Proyecto desarrollado de manera individual por **José Luis Rodríguez Andreu**.

## Funcionamiento y dataset generado

El objetivo del proyecto es extraer información del sitio web y red social www.goodreads.com de los libros ganadores de los GoodReads Awards del año indicado. El código toma como entrada uno o mas años para los que extrae los datos. 

El dataset generado contiene la siguiente información:

- **category**: Categoria donde ha ganado el libro
- **title**: Titulo
- **votes**: Numero de votos
- **author_name**: Nombre del autor
- **book_series**: Saga a la que pertenece el libro
- **rating_value**: Puntuacion en goodreads
- **num_ratings**: Numero de valoraciones
- **num_reviews**: Numero de reviews
- **list_genres**: Lista de generos asociados al libro
- **book_format**: Formato del libro
- **num_pages**: Numero de paginas
- **publish_date**: Fecha de publicacion
- **publisher**: Editora de publicacion
- **original_title**: Titulo original
- **isbn**: ISBN
- **edition_language**: Idioma de la edicion
- **setting**: Lugar donde transcurre el libro
- **num_awards**: Numero de premios recibidos

## Estado actual

El core principal del proyecto ya se encuentra implementado. Actualmente solo muestra por pantalla los datos de cada categoría encontrada en el año indicado

**TODO**:

- Generación dataset
- codigo main que tome varios años de entrada
- Generación fichero csv
- Incluir gestión de errores adicionales