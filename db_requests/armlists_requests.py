from db_requests.db_connector import DBConnector
from typing import Literal
from db_requests.class_armlist import Armlist, Techlist


# Получение всех существующих армлистов
def get_all_armlists(db_connector: DBConnector, is_asc: bool = False, is_init: bool = False):
    armlists = []
    request = f'''
    SELECT id,
           name,
           cost,
           rank,
           fraction_id,
           image
    FROM armlists
    ORDER BY cost DESC, fraction_id, rank DESC
    '''
    try:
       db_connector.execute(request)
       armlists = [Armlist(id=item[0],
                            name=item[1],
                            cost=item[2],
                            rank=item[3],
                            fraction_id=item[4],
                            image=item[5])
                     for item in db_connector.fetchall()]
    except Exception as ex:
       print(f"Error: {ex}")
    
    return armlists

# Получение определённого армлиста по id
def get_armlist_by_id(db_connector: DBConnector, armlist_id: int) -> tuple:
    request = f'''
    SELECT id,
           name,
           cost,
           fraction_id,
           image
    FROM armlists
    WHERE id = {armlist_id}
    '''
    return db_connector.get_data(request, 'one')

# Получение всех существующих армлистов
def get_all_techlists(db_connector: DBConnector, is_asc: bool = False, is_init: bool = False):
    techlists = []
    request = f'''
    SELECT id,
           name,
           cost,
           rank,
           fraction_id,
           image
    FROM techlists
    ORDER BY cost DESC, fraction_id, rank DESC
    '''
    try:
       db_connector.execute(request)
       techlists = [Techlist(id=item[0],
                            name=item[1],
                            cost=item[2],
                            rank=item[3],
                            fraction_id=item[4],
                            image=item[5])
                     for item in db_connector.fetchall()]
    except Exception as ex:
       print(f"Error: {ex}")
    
    return techlists