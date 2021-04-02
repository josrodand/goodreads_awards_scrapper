from goodReadsScrapper import *

def test_scrapper(year):
    """
    Funcion testeo: introduce un año e imprime por pantalla la informacion 
    obtenida de scraping
    Inputs:
        year: año de los premios
    """
    
    print(f"[INFO] Reading awards data from year {year}...", '\n')
    
    list_cat = get_categories(year)

    for cat_elem in list_cat:
        print(f"[INFO] loading info from category: {cat_elem[0]}")
        dict_book_result = load_data_category(cat_elem)
        time.sleep(0.5)
        
        print(pd.Series(dict_book_result))
#         for key, value in dict_book_result.items():
#             print(f'{key}:\t\t{value}')
        print('\n')
        

if __name__ == '__main__':
    
    year = 2020
    test_scrapper(year)