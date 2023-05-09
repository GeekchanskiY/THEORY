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

UNIQUE(field)

create table CRYPTO_FAVOURITE(
	user_id INT not null,
	crypto_id INT not null,
	UNIQUE(user_id, crypto_id), -- UNIQUE Together
	constraint FK_USER foreign key(user_id) references USERS(user_id) on delete cascade,
	constraint FK_CRYPTO foreign key(crypto_id) references CRYPTO(crypto_id) on delete cascade
) tablespace TS_USER;