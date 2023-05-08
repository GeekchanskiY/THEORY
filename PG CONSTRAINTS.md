[[PostgreSQL]]

CHECK (expression)

examples:

CREATE TABLE products (
    product_no integer,
    name text,
    price numeric **CHECK (price > 0)**
);

or 

CREATE TABLE products (
    product_no integer,
    name text,
    price numeric **CONSTRAINT positive_price** CHECK (price > 0)
);