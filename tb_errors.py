# Defining custom errors for ThuderBase.
class TBError(Exception):
    """Base class for other ThunderBase errors."""
    pass

# ThunderBase database errors.


class ThunderBaseNotFound(TBError):
    """Raised when a given ThunderBase isn't found."""
    pass

# ThunderBase name errors.


class ThunderBaseNameEmpty(TBError):
    """Raised when the name of the ThunderBase is given empty."""
    pass


class ThunderBaseInvalidName(TBError):
    """Raised when the name of the database is not a string."""
    pass

# ThunderBase password errors.


class ThunderBasePasswordEmpty(TBError):
    """Raised when the password of the database is empty."""
    pass


class ThunderBaseInvalidPassword(TBError):
    """Raised when the password of the database is not a string."""
    pass

# Table errors


class TableNotFound(TBError):
    """Raised when a given table is not found."""
    pass


# Table property errors.

class TableNameEmpty(TBError):
    """Raised when the name of a table is null or empty."""
    pass


class TableNameInvalid(TBError):
    """Raised when the name of a table is not a string."""
    pass


class TableSchemaEmpty(TBError):
    """Raised when the schema of the given table is null of empty."""
    pass


class TableSchemaInvalid(TBError):
    """Raised when the schema of the given table is not a dict."""
    pass

# Table record errors.


class TableRecordEmpty(TBError):
    """Raised when the given record is empty."""
    pass


# Errors while adding a record to the table.
class TableRecordInvalid(TBError):
    """Raised when the type of the given record is not a dictionary."""
    pass


class RecordFieldsIncorrect(TBError):
    """Raised when the record schema doesn't match the table schema."""
    pass


class RecordFieldNotOfSpecifiedType(TBError):
    """Raised when the record schema value doesn't match the schema value datatype."""
    pass
