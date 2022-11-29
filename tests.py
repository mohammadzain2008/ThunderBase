from database import ThunderBase
from table import Table

TB = ThunderBase('quantum', 'quantum@123')
table = Table(TB, {
    'name': int,
    'database': ThunderBase,
    'age': int,
})
