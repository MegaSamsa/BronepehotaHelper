-- Создание таблицы армлистов
CREATE TABLE armlists
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    cost INTEGER NOT NULL,
    fraction_id INTEGER NOT NULL,
    image BLOB,
    FOREIGN KEY ( fraction_id ) REFERENCES fractions( id )
)

-- Добавление нового армлиста
INSERT INTO armlists
(
    name,
    cost,
    fraction_id,
    image
)
VALUES
(
    :name,
    :cost,
    :fraction_id,
    :image
)

-- Получение армлиста 
SELECT id,
       name,
       cost,
       fraction_id,
       image
FROM armlists
WHERE id = :id

-- Получение списка армлистов
SELECT id,
       name,
       cost,
       fraction,
       image
FROM armlists
ORDER BY cost

-- Создание таблицы фракций
CREATE TABLE fractions
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    color TEXT NOT NULL
)

-- Добавление новой фракции
INSERT INTO fractions
(
    name,
    color
)
VALUES
(
    :name
    :color
)

-- Создание таблицы техлистов
CREATE TABLE techlists
(
    id INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    cost INTEGER NOT NULL,
    rank INTEGER
)