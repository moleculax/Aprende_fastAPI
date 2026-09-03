-- ============================================================
-- TABLA AUTHOR (AUTORES)
-- ============================================================
-- Base de datos db_blog


CREATE TABLE author
(
    id_author  SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================
-- TABLA BOOK (LIBROS)
-- ============================================================
CREATE TABLE book
(
    id_book          SERIAL PRIMARY KEY,
    title            VARCHAR(100) NOT NULL,
    publication_date DATE,
    pages            INTEGER NOT NULL,
    isbn             VARCHAR(100) NOT NULL,
    price            DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    author_id        INTEGER NOT NULL,
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT book___fk FOREIGN KEY (author_id)
        REFERENCES author (id_author)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- ============================================================
-- TABLA SALE (VENTAS DE LIBROS)
-- ============================================================
CREATE TABLE sale
(
    id_sale      SERIAL PRIMARY KEY,
    id_book      INTEGER NOT NULL,
    quantity     INTEGER NOT NULL CHECK (quantity > 0),
    sale_price   DECIMAL(10, 2) NOT NULL CHECK (sale_price > 0),
    sale_date    DATE NOT NULL DEFAULT CURRENT_DATE,
    total_amount DECIMAL(10, 2) GENERATED ALWAYS AS (quantity * sale_price) STORED,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT sale___fk_book FOREIGN KEY (id_book)
        REFERENCES book (id_book)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- ============================================================
-- ÍNDICES
-- ============================================================
CREATE INDEX idx_sale_book ON sale(id_book);
CREATE INDEX idx_sale_date ON sale(sale_date);
CREATE INDEX idx_book_author ON book(author_id);
CREATE INDEX idx_author_name ON author(name);