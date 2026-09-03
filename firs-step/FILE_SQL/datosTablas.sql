-- ============================================================
-- INSERTAR AUTORES
-- ============================================================
INSERT INTO author (name, birth_date) VALUES
                                          ('Gabriel García Márquez', '1927-03-06'),
                                          ('Jorge Luis Borges', '1899-08-24'),
                                          ('Julio Cortázar', '1914-08-26'),
                                          ('Mario Vargas Llosa', '1936-03-28'),
                                          ('Isabel Allende', '1942-08-02'),
                                          ('Pablo Neruda', '1904-07-12'),
                                          ('Octavio Paz', '1914-03-31');

-- ============================================================
-- INSERTAR LIBROS
-- ============================================================
INSERT INTO book (title, publication_date, pages, isbn, price, author_id) VALUES
                                                                              ('Cien años de soledad', '1967-05-30', 432, '978-84-376-0494-7', 29.99, 1),
                                                                              ('El amor en los tiempos del cólera', '1985-01-01', 368, '978-84-376-0495-4', 24.50, 1),
                                                                              ('Crónica de una muerte anunciada', '1981-01-01', 128, '978-84-376-0496-1', 18.75, 1),
                                                                              ('Ficciones', '1944-01-01', 224, '978-84-376-0497-8', 19.75, 2),
                                                                              ('El Aleph', '1949-01-01', 192, '978-84-376-0498-5', 17.50, 2),
                                                                              ('Rayuela', '1963-06-28', 640, '978-84-376-0500-5', 32.00, 3),
                                                                              ('Historias de cronopios y de famas', '1962-01-01', 176, '978-84-376-0501-2', 15.99, 3),
                                                                              ('La ciudad y los perros', '1963-01-01', 448, '978-84-376-0503-6', 26.50, 4),
                                                                              ('La casa verde', '1966-01-01', 400, '978-84-376-0504-3', 22.75, 4),
                                                                              ('La casa de los espíritus', '1982-01-01', 448, '978-84-376-0506-7', 28.99, 5),
                                                                              ('De amor y de sombra', '1984-01-01', 304, '978-84-376-0507-4', 21.50, 5),
                                                                              ('Veinte poemas de amor', '1924-01-01', 96, '978-84-376-0513-5', 12.99, 6),
                                                                              ('El laberinto de la soledad', '1950-01-01', 208, '978-84-376-0514-2', 16.99, 7);

-- ============================================================
-- INSERTAR VENTAS
-- ============================================================
INSERT INTO sale (id_book, quantity, sale_price, sale_date) VALUES
                                                                (1, 5, 29.99, '2024-01-15'),
                                                                (1, 3, 29.99, '2024-01-20'),
                                                                (2, 2, 24.50, '2024-01-18'),
                                                                (3, 4, 18.75, '2024-01-22'),
                                                                (4, 10, 19.75, '2024-01-25'),
                                                                (5, 3, 17.50, '2024-02-01'),
                                                                (6, 2, 32.00, '2024-02-05'),
                                                                (7, 6, 15.99, '2024-02-10'),
                                                                (8, 4, 26.50, '2024-02-15'),
                                                                (9, 2, 22.75, '2024-02-20'),
                                                                (10, 8, 28.99, '2024-03-01'),
                                                                (11, 3, 21.50, '2024-03-05'),
                                                                (12, 15, 12.99, '2024-03-10'),
                                                                (13, 5, 16.99, '2024-03-15');

-- ============================================================
-- CONSULTAS DE VERIFICACIÓN
-- ============================================================

-- Ver todos los autores
SELECT * FROM author;

-- Ver todos los libros con su autor
SELECT
    b.id_book,
    b.title,
    b.price,
    a.name AS author,
    b.pages
FROM book b
         JOIN author a ON b.author_id = a.id_author
ORDER BY b.title;

-- Ver todas las ventas con detalles
SELECT
    s.id_sale,
    b.title,
    a.name AS author,
    s.quantity,
    s.sale_price,
    s.total_amount,
    s.sale_date
FROM sale s
         JOIN book b ON s.id_book = b.id_book
         JOIN author a ON b.author_id = a.id_author
ORDER BY s.sale_date DESC;

-- Resumen de ventas por libro
SELECT
    b.title,
    a.name AS author,
    SUM(s.quantity) AS total_copias_vendidas,
    SUM(s.total_amount) AS total_recaudado
FROM sale s
         JOIN book b ON s.id_book = b.id_book
         JOIN author a ON b.author_id = a.id_author
GROUP BY b.id_book, b.title, a.name
ORDER BY total_recaudado DESC;