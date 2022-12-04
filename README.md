# ThunderBase
![GitHub contributors](https://img.shields.io/github/contributors/mohammadzain2008/ThunderBase)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/mohammadzain2008/ThunderBase)
![GitHub last commit](https://img.shields.io/github/last-commit/mohammadzain2008/ThunderBase)
![GitHub language count](https://img.shields.io/github/languages/count/mohammadzain2008/ThunderBase)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
![GitHub](https://img.shields.io/github/license/mohammadzain2008/ThunderBase)
![GitHub Repo stars](https://img.shields.io/github/stars/mohammadzain2008/ThunderBase?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/mohammadzain2008/ThunderBase?style=social)

<b>ThunderBase</b> is a new age database system which is an advanced software which can be used to do almost anything which other database management systems like SQL, MongoDB etc. can do. What makes it different from other systems is it's sole principle that, <i>"Every user has it's own database"</i>. This means that every user stores his/her data on his/her own device rather than storing it onto a common database used by millions of users. This principle has the following benefits:

 - A company won't need to set up their own database which prevents them from paying for the database management and overall database fee.
 - Hackers won't be able to steal data from the companies as they don't have a single database.

<i>As of <b>12<sup>th</sup> December, 2022</b>; ThunderBase operates only for Python programming language and is under development by it's only contributor which is me; Mohammad Zain.</i>

## Quick Links
- [<b>Getting Started</b>](#getting-started)
	- [Exploring ThunderBase](#exploring-thunderbase)
		- [Creating a Database](#creating-a-database)
		- [Creating a Table](#creating-a-table)
			- [<i>Adding a Record</i>](#adding-a-record)
			- [<i>Deleting a Record</i>](#deleting-a-record)
			- [<i>Searching a Record</i>](#searching-a-record)
- [<b>Critical Operations</b>](#critical-operations)
    - [Truncating a ThunderBase](#truncating-a-thunderbase)
    - [Deleting a ThunderBase](#deleting-a-thunderbase)
    - [Truncating a Table](#truncating-a-table)
    - [Deleting a Table](#deleting-a-table)
- [<b>Errors and Exceptions</b>](#errors-and-exceptions)
	- [Database Errors](#database-errors)
	- [Table Errors](#table-errors)
	- [Table I/O Errors](#table-io-errors)

#  Getting Started
<b>As of 2022, ThunderBase doesn't have it's own <i>pip</i> package.</b> In order to use it in your Python projects by downloading the files from the GitHub repository and placing the files in your project folder.

## Exploring ThunderBase
Let us now see how can we use ThunderBase in our own python projects by calling a few simple lines of code.
### Creating a Database
To import the main <code>ThunderBase</code> class, write these lines to the top of your Python file,

    from database import ThunderBase
This will import the `ThunderBase` class and can be used by calling,

    TB = ThunderBase()
This is a very basic example of creating a database. The correct syntax of creating an instance of the class is:

    ThunderBase(name:str='root', password:str='local')
The name or password of a database must not be empty or of any other type except the string. 
On executing the program, a sub directory will be created by the name of `ThunderBase` and in it will be created another folder with the following path:

    /ThunderBase/<database_name>+<password_hash>/
Tampering with the `ThunderBase` folder will result in the malfunctioning of the code and will affect the output.

### Creating a Table
To create a table in a database, first import the <code>Table</code> class to your source code as:

    from table import Table
This will import the class and all the methods associated with the class. To create a table in a database, write the following:

    TB = ThunderBase()
    table = Table(TB, {
	    'name': str,
	    'age': int,
    })
The first argument is the `ThunderBase` in which the table needs to be created. The second argument is the table schema where each key is the name of the field and the value is the datatype of the field. The `Table` class follows the following syntax:

    Table(thunderbase: ThunderBase, schema: dict, name: str='table')
When this is executed, the table is created as a folder with the path:

    /ThunderBase/<database_name>+<password_hash>/<table_name>+<hash>/
Make sure not to tamper the contents of `ThunderBase` folder as it can result in breaking the program. Whenever a new record is added to the table, the record will be given a unique <i>id</i> which is a 16-character long hexadecimal string and will be stored in the following location:

    /ThunderBase/<database_name>+<password_hash>/<table_name>+<hash>/<record_id>.tbr
<code>.tbr</code> stands for <i>ThunderBase Record</i>. The data inside the <code>.tbr</code> file will be of the following format:

    {
	    'field_1': 'value_1',
	    'field_2': 'value_2',
	    'id': <id>
    }
#### Adding a Record
You can add a record by using the following method of the <code>Table</code>class:

    Table.add_record(record: dict)
The following code displays the ability of ThunderBase to add records to a database:

    TB = ThunderBase()
    table = Table(TB, {'name': str, 'age': int,})
    table.add_record({'name': 'Zain', 'age': 14,})
The method will return the id of the record and can be stored as any other value; in a list, variable etc.
#### Deleting a Record
There are primarily two methods of the <code>Table</code> class to delete a single record or multiple records:

 1. `Table.delete_record_by_id(id: str)` for deleting a single record.
 2. `Table.delete_records_by_fields(field: dict)` for deleting multiple records.

##### <code>Table.delete_record_by_id()</code>
To delete a single record using the record's unique id, this method can be used. Note that the id is a string and can't take other types of values.

##### <code>Table.delete_records_by_fields()</code>
In this method, you pass a dictionary which specifies the criteria based on which the records will be deleted. For example:

    Table.delete_records_by_fields({'name': 'Zain'})
The above code will delete all the records with the property `'name': 'Zain'`. This method can also take multiple criteria.
#### Searching a Record
To search a record, there are primarily two ways to achieve that (as of 2022):

 1. `Table.search_record_by_id(id: str)` for searching a single record.
 2. `Table.search_records_by_fields(fields: dict)` for searching multiple records fulfilling a given criteria.
##### <code>Table.search_record_by_id()</code>
To search a single record using the record's unique id, this method can be used. Note that the id is a string and can't take other types of values.

##### <code>Table.search_records_by_fields()</code>
In this method, you pass a dictionary which specifies the criteria based on which the records will be searched and returned. For example:

    Table.search_records_by_fields({'name': 'Zain'})
The above code will search and return all the records with the property `'name': 'Zain'`. This method can also take multiple criteria. Note that this method returns a list. If no record was found; it returns and empty list which evaluates to `false`.

# Critical Operations
These include operations such as truncating a ThunderBase, Table or deleting them. Let us go through each one of them.

## Truncating a ThunderBase
We use the method `ThunderBase.truncate()` to truncate a ThunderBase. If a ThunderBase exists such that:

    TB = ThunderBase()
Then, to truncate the ThunderBase, we write the following:

    TB.truncate()
This will truncate the ThunderBase meaning that all the tables which it contains except the `INFO.tbdbinfo` file.

## Deleting a ThunderBase
We use the method `ThunderBase.delete()` to delete a ThunderBase. If a ThunderBase exists such that:

    TB = ThunderBase()
Then, to delete the ThunderBase, we write the following:

    TB.delete()
This will delete the ThunderBase meaning that all the tables which it contains including itself.

## Truncating a Table
We use the method `Table.truncate()` to truncate a Table. If a Table exists such that:

    table = Table(TB)
Then, to truncate the Table, we write the following:

    table.truncate()
This will truncate the Table meaning that all the records which it contains except the `INFO.tbtableinfo` file.

## Deleting a Table
We use the method `Table.delete()` to delete a Table. If a Table exists such that:

    table = Table(TB)
Then, to delete the Table, we write the following:

    table.delete()
This will delete the Table meaning that all the records which it contains including itself.

# Errors and Exceptions
Not only does ThunderBase use Python's in-built exceptions and errors but it also has it's own custom built exceptions. Each of these exceptions is based on a base class of errors called `TBError`. Every new exception inherits the property of this class.

## Database Errors
The below given errors are related to the main database. Whenever an exception is raised while working with the database, the following errors might pop-up:

 - `ThunderBaseNotFound()`
 - `ThunderBaseNameEmpty()`
 - `ThunderBaseInvalidName()`
 - `ThunderBasePasswordEmpty()`
 - `ThunderBaseInvalidPassword()`

Let us go through each error and understand when are they raised.
### <code>ThunderBaseNotFound()</code>
This error is raised when a given ThunderBase is not found. This can mainly happen while connecting a table to a ThunderBase. 

### <code>ThunderBaseNameEmpty()</code>
The default name of any ThunderBase is <code>root</code>. If an empty string or any other value which evaluates to <code>false</code> is given; this exception is raised. 

### <code>ThunderBaseInvalidName()</code>
The only type which ThunderBase supports for a name is of type <code>str</code>. If any other type of data is given, the exception is raised.

### <code>ThunderBasePasswordEmpty()</code>
The default password of a ThunderBase is <code>local</code>. If by force, the password is set to an empty string or any other value which evaluates to <code>false</code>; this exception is raised. 

### <code>ThunderBaseInvalidPassword()</code>
The only type which ThunderBase supports for a password is of type <code>str</code>. If any other type of data is given, the exception is raised.

## Table Errors
The below given errors are related to the table. Whenever an exception is raised while working with a table, the following errors might pop-up:

 - `TableNotFound()`
 - `TableNameEmpty()`
 - `TableNameInvalid()`
 - `TableSchemaEmpty()`
 - `TableSchemaInvalid()`

Let us go through each error and understand when are they raised.

### <code>TableNotFound()</code>
This error is raised when a given Table is not found. This can mainly happen while adding records or doing any type of I/O with the table. 

### <code>TableNameEmpty()</code>
The default name of any Table is <code>table</code>. If an empty string or any other value which evaluates to <code>false</code> is given; this exception is raised. 

### <code>TableNameInvalid()</code>
The only type which a table supports for a name is of type <code>str</code>. If any other type of data is given, the exception is raised.

### <code>TableSchemaEmpty()</code>
A schema is a structure which defines the main skeleton of a table. If an empty <code>dict</code> is passed or any value evaluating to <code>false</code> is passed; the exception is raised.

### <code>TableSchemaInvalid()</code>
The only type which a table supports for a schema is of type <code>dict</code>. If any other type of data is given, the exception is raised.

## Table I/O Errors
The below given errors are raised when doing some wrong table I/O:

 - `TableRecordEmpty()`
 - `TableRecordInvalid()`
 - `RecordFieldsIncorrect()`
 - `RecordFieldNotOfSpecifiedType()`

Let us go through each error and understand when are they raised.

### <code>TableRecordEmpty()</code>
This error is raised when an empty record is appended to the table. Since a table schema cannot be empty, therefore a table record cannot also be empty. Therefore, the exception is raised.

### <code>TableRecordInvalid()</code>
The default datatype of any record is <code>dict</code>. If any other type of value is given, the exception is raised.

### <code>RecordFieldsIncorrect()</code>
When a record is sent to the table, the keys of the record should match every key of the table schema. If not, the exception is raised.

### <code>RecordFieldNotOfSpecifiedType()</code>
A schema not only contains the name of the fields of a table, but also the type of value it will hold. When passing a record, if a type of value in the record doesn't match the corresponding type of value inside the table schema, the exception is raised.

### <code>TableSchemaInvalid()</code>
The only type which a table supports for a schema is of type <code>dict</code>. If any other type of data is given, the exception is raised.