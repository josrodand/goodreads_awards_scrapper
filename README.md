# GoodReads Awards Scrapper

Este proyecto tiene como objetivo generar un conjunto de datos que reúne información sobre los **libros ganadores de los premios Goodreads Awards**, del sitio web www.goodreds.com. La aplicación de captura de datos toma como entrada un año determinado, y genera un fichero csv con el ganador de cada categoría para ese año, el cual contiene información sobre el autor, el número de votos o la puntuación del libro en la propia plataforma, además de información del propio libro.

## Descripción

Este proyecto ha sido desarrollado para la asignatura Tipología y ciclo de vida de los Datos, para el Master Universitario en Ciencia de Datos de la Universitat Oberta de Catalunya.

## Miembros del Equipo

Proyecto desarrollado de manera individual por **José Luis Rodríguez Andreu**.

## Ejecución de la aplicación

Para ejecutar la aplicación es necesario instalar las siguientes librerías:

```
pip install pandas
pip install request
pip install beautifulsoup4
```

Ejemplo de ejecución de la aplicación:

```
python goodReadsScrapper.py 2020
```

## Funcionamiento y dataset generado

La aplicación genera un fichero csv de nombre **goodreads_awards_[year].csv**, donde *year* se corresponde al año indicado a la aplicación. En el caso de que se indique un año erróneo o para el cual no haya datos sobre los premios, la aplicación devuelve un mensaje de error.
Cada uno de los registros del conjunto de datos se corresponde al ganador de una determinada categoría para el año escogido, donde se recogen las siguientes características:

* **Category**: Categoría en la que el libro ha resultado ganador.
* **Title**: Título de la obra.
* **Votes**: Número de votos alcanzados por la obra.
* **Autor_name**: Nombre del autor.
* **Book_series**: Serie literaria a la que pertenece el libro, si fuera el caso.
* **Rating_value**: Valoración media (en una escala de 0 a 5) alcanzada en Goodreads.
* **Num_ratings**: Número de valoraciones recibidas por la obra.
* **Num_reviews**: Número de opiniones realizadas por los usuarios para este libro.
* **List_genres**: Lista de géneros asociados al libro según la plataforma y los usuarios. Se corresponde a una cadena de caracteres donde los géneros están separados por el carácter ``_``.
* **Book_format**: Formato del libro (tapa dura, audiolibro…).
* **Num_pages**: Número de páginas.
* **Publish_date**: Fecha de publicación.
* **Original_title**: Título de la obra en el idioma original.
* **Isbn**: ISBN, o código identificativo de la edición.
* **Edition_language**: Idioma de la edición.
* **Setting**: Lugar donde transcurre el libro.
* **Num_awards**: Número de premios que la obra ha recibido.
* **Year**: Año de los premios.

## Descripción del repositorio

* **goodReadsScrapper.py**: Aplicación python de extracción de datos
* **LICENSE**: Documento de licencia.
* **csv**: directorio con los ficheros csv generados
* **pdf**: Directorio del documento pdf con la descripción y resultados de la práctica.