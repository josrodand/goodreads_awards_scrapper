import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
import requests


def get_categories(year):
    """
    toma como entrada la url de los awards del año X y devuelve una lista de tuplas
    con el titulo de la categoria y la url del ganador y nominaciones de esta.
    Inputs: 
        year: año de lectura
    Returns:
    list_cat: lista de tuplas (categoria, url)
    """
    
    url_goodreads = 'https://www.goodreads.com'
    url_awards = f'{url_goodreads}/choiceawards/best-books-{year}'
    
    page_awards = requests.get(url_awards)
    soup_main = BeautifulSoup(page_awards.content, 'html.parser')
    
    elements = soup_main.find_all(class_ = 'category clearFix')
    list_cat = []
    for elem in elements:
        element_category = elem.a.text.replace('\n', '')
        url_best_cat = f"{url_goodreads}{elem.a.get('href')}"
        list_cat.append((element_category, url_best_cat))
    
    return list_cat


def scrap_winner_page(winner_cat_url):
    """
    Hace scraping a la pagina de la categoria y extrae el titulo,
    el numero de votos y la url (directorio) del libro.
    Inputs
        winner_cat_url: url de la pagina del ganador de categoria
    Returns:
        title: Titulo del libro
        num_votes: Numero de votos
        url_book: Directorio dentro de la url donde se encuentra
        la pagina del libro
    """
    page_cat_winner = requests.get(winner_cat_url)
    soup_cat = BeautifulSoup(page_cat_winner.content, 'html.parser')
    title = soup_cat.find(class_ = 'winningTitle choice gcaBookTitle').text
    num_votes = int(soup_cat.find(class_ = 'greyText gcaNumVotes').text \
                    .replace(',', '') \
                    .replace('\n', '') \
                    .replace('votes', ''))
    url_book = soup_cat.find(class_ = 'winningTitle choice gcaBookTitle').get('href')
    
    return title, num_votes, url_book


def get_databox(soup_book):
    """
    Devuelve un diccionario con los datos del elemento databox de cada libro.
    Inputs:
        soup_book: elemento soup del libro
    Returns:
        dict_databox: diccionario con los resultados
    """
    # leemos la tabla de boox data box:
    databox_key = soup_book.find('div' , id = 'bookDataBox').find_all('div', class_ = 'infoBoxRowTitle')
    databox_key = [elem.text.strip() for elem in databox_key]
    databox_value = soup_book.find('div' , id = 'bookDataBox').find_all('div', class_ = 'infoBoxRowItem')
    databox_value = [elem.text.strip() for elem in databox_value]
    dict_databox = {key:value for key, value in zip(databox_key, databox_value)}
    
    return dict_databox


def load_data_category(cat_elem):
    """
    Scrapea la url del libro ganador de una categoría y devuelve un diccionario con
    los datos
    Inputs:
        cat_elem: tupla de informacion [categoría, url]
    Returns:
        dict_book: Diccionario con la siguiente informacion:
            category: Categoria donde ha ganado el libro
            title: Titulo
            votes: Numero de votos
            author_name: Nombre del autor
            book_series: Saga a la que pertenece el libro
            rating_value: Puntuacion en goodreads
            num_ratings: Numero de valoraciones
            num_reviews: Numero de reviews
            list_genres: Lista de generos asociados al libro
            book_format: Formato del libro
            num_pages: Numero de paginas
            publish_date: Fecha de publicacion
            publisher: Editora de publicacion
            original_title: Titulo original
            isbn: ISBN
            edition_language: Idioma de la edicion
            setting: Lugar donde transcurre el libro
            num_awards: Numero de premios recibidos
    """
    
    dict_book = {}
    
    url_goodreads = 'https://www.goodreads.com'
    name_cat = cat_elem[0]
    winner_cat_url = cat_elem[1]
    title, votes, url_book = scrap_winner_page(winner_cat_url)
    time.sleep(0.5) # ralentizar la velocidad de scrapeo
    url_book = f"{url_goodreads}{url_book}"

    dict_book['category'] = name_cat
    dict_book['title'] = title
    dict_book['votes'] = votes    
    
    book_page = requests.get(url_book)
    soup_book = BeautifulSoup(book_page.content, 'html.parser')
    
    # autor
    author_name = soup_book.find(class_ = 'authorName').text
    dict_book['author_name'] = author_name
    
    # book series
    try:
        book_series = soup_book.find('h2', id = "bookSeries").text.strip()
    except: # esto a lo mejor sobra
        # da error si no existe el valor de bookseries. se asigna None
        book_series = None
    # devuelve esto si no tiene serie
    # <h2 id="bookSeries">
    # </h2>
    dict_book['book_series'] = book_series
    
    # rating numerico
    rating_value = soup_book.find(itemprop = "ratingValue").text.strip()
    dict_book['rating_value'] = rating_value
   
    # numero votaciones
    num_ratings = int(soup_book.find('meta' ,
                                     itemprop = 'ratingCount') \
                      .text.strip() \
                      .split('\n')[0] \
                      .replace(',', ''))
    dict_book['num_ratings'] = num_ratings
    
    # numero reviews
    num_reviews = int(soup_book.find('meta' , 
                                     itemprop = 'reviewCount') \
                      .text.strip() \
                      .split('\n')[0] \
                      .replace(',', ''))
    dict_book['num_reviews'] = num_reviews
    
    # generos de goodreads
    list_gen = [soup_tag.text for soup_tag in soup_book.find_all('a' , class_ = 'actionLinkLite bookPageGenreLink')]
    list_gen = '_'.join(list(dict.fromkeys(list_gen)))
    dict_book['list_genres'] = list_gen
    
    # tipo de tapa
    book_format = soup_book.find('span' ,
                                 itemprop = 'bookFormat').text
    dict_book['book_format'] = book_format
   
    # numero de paginas
    num_pages = int(soup_book.find('span' ,
                                   itemprop = 'numberOfPages') \
                    .text.split(' ')[0])
    dict_book['num_pages'] = num_pages
    
    # fecha publicacion
    publish_date = soup_book.find('div' , id = 'details') \
        .find_all('div', class_='row')[1] \
        .text.strip().split('\n')[1] \
        .strip()
    dict_book['publish_date'] = publish_date
    
    # nombre publicador
    publisher = soup_book.find('div' , id = 'details') \
        .find_all('div', class_='row')[1] \
        .text.strip() \
        .split('\n')[2] \
        .replace('by', '') \
        .strip()
    dict_book['publisher'] = publisher
    
    # extraemos la tabla desplegable de informacion del libro
    databox = get_databox(soup_book)
    
    # titulo original
    try:
        original_title = databox['Original Title']
    except:
        original_title = None
    dict_book['original_title'] = original_title
    
    # isbn si viene
    try:
        isbn = databox['ISBN'].split('\n')[0]
    except:
        # no esta en databox
        isbn = None
    dict_book['isbn'] = isbn
    
    # edition language
    try:
        edition_language = databox['Edition Language']
    except:
        edition_language = None
    dict_book['edition_language'] = edition_language
    
    # setting
    try:
        setting = databox['Setting']
        setting = setting.split('\n')[0].strip()
    except:
        setting = None
    dict_book['setting'] = setting
    
    # nº premios
    try:
        num_awards = len(databox['Literary Awards'] \
                         .replace('...more', ', ') \
                         .replace('\n', '') \
                         .replace('...less', '') \
                         .split(', '))
    except:
        num_awards = None
    dict_book['num_awards'] = num_awards
    
    return dict_book
