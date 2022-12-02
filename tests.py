from database import ThunderBase
from table import Table

# Creating a ThunderBase.
TB = ThunderBase('quantum', 'quantum@123')

# Creating a table and defining the schema.
table = Table(TB, {
    'name': str,
    'age': int,
})

# Inserting a record into the table.
rec = table.add_record({
    'name': 'Zain',
    'age': 15
})

# Deleting a record using it's id. Returns true and false on suitable results.
table.delete_record_by_id('b38cefd8062a3b0064fc1a3dfb062f0e')

# Returns the list of deleted records. If none, returns an empty list.
table.delete_records_by_fields({
    'name': 'Zain',
    'age': 15,
})

# Searching a record based on id.
rec = table.add_record({
    'name': 'John Doe',
    'age': 14,
})

table.search_record_by_id('b38cefd8062a3b0064fc1a3dfb062f0e')

# Searching multiple records based on a given criteria.
table.search_records_by_fields({
    'name': 'Zain',
    'age': 14
})
