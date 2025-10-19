from db_requests.db_connector import DBConnector


# Получение всех существующих фракций
def get_all_fractions(db_connector: DBConnector):
    request = f'''
    SELECT id,
           name,
           color
    FROM fractions
    ORDER BY id
    '''
    return db_connector.get_data(request, 'all')

# Получение определённой фракции по id
def get_armlist_by_id(db_connector: DBConnector, fraction_id: int) -> tuple:
    request = f'''
    SELECT id,
           name,
           color
    FROM fractions
    WHERE id = {fraction_id}
    '''
    return db_connector.get_data(request, 'one')
