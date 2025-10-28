from db_requests.db_connector import DBConnector
from typing import Literal


# Получение всех существующих армлистов
def get_all_armlists(db_connector: DBConnector, order_by: Literal['name', 'cost', 'fraction_id'], is_asc: bool = False, is_init: bool = False):
    request = f'''
    SELECT id,
           name,
           cost,
           rank,
           fraction_id,
           image
    FROM armlists
    ORDER BY {order_by} {'ASC' if is_asc else 'DESC'} {', fraction_id' if is_init else ''}
    '''
    return db_connector.get_data(request, 'all')

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
