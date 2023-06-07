[[PostgreSQL]]

Boolean

Character: char(n), varchar(n), text

Char: If you insert a string that is shorter than the length of the column, PostgreSQL pads spaces. If you insert a string that is longer than the length of the column, PostgreSQL will issue an error.

VarChar: PostgreSQL does not pad spaces when the stored string is shorter than the length of the column.

Text is the variable-length character string. Theoretically, text data is a character string with unlimited length.

Numeric: integer, floating-point

There are three kinds of integers in PostgreSQL:

-   Small integer ( `SMALLINT`) is 2-byte signed integer that has a range from -32,768 to 32,767.
-   Integer ( `INT`) is a 4-byte integer that has a range from -2,147,483,648 to 2,147,483,647.
-   Serial is the same as integer except that PostgreSQL will automatically generate and populate values into the `SERIAL` column. This is similar to AUTO_INCREMENT column in MySQL or AUTOINCREMENT column in SQLite.

There three main types of floating-point numbers:

-   float(n)  is a floating-point number whose precision, at least, n, up to a maximum of 8 bytes.
-   real or float8 is a 4-byte floating-point number.
-   numeric or numeric(p,s) is a real number with p digits with s number after the decimal point. The numeric(p,s) is the exact number.

Temporal: date, time, timestamp, interval

timestamp = date + time
Timestampz is a timezone-aware timestamp data type

UUID

Array

JSON

hstore

Special: network addr, geometric data