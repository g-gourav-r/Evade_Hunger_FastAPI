# SQLite3 DB Basics


## .tables

List names of all tables in the current database.

**Example:**

.tables

## .schema table\_name

Show the CREATE statement for a specific table.

## .dump

Prints the SQL text for creating tables and data in a format that can be used for backup or migration.

## .quit

Exit the SQLite3 command-line interface.

## .show

Show the current settings or a list of other meta-information.

## .databases

List names and files of attached databases.

## Creating a Table

To create a new table, use the CREATE TABLE statement.

## Deleting a Table

To delete an existing table, use the DROP TABLE statement.

## Adding an Entry

To add a new entry to a table, use the INSERT INTO statement.

**Example:**

</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-sql">INSERT INTO users (name, password, type, email, user_id, phone) VALUES ('John Doe', 'password123', 1, 'john@example.com', 1, '123-456-7890');
</code></div></div></pre>

## Updating an Entry

To update an existing entry in a table, use the UPDATE statement.

## Removing an Entry

To remove an entry from a table, use the DELETE statement.

*Note: Replace table and column names, as well as values, according to your database schema.*
