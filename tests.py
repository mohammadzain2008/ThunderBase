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
table.add_record({
    'name': 'Zain',
    'age': 14
})
