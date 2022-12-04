"""A module which contains all the errrors raised by ThunderBase."""
# pylint score: 10/10

# Defining custom errors for ThuderBase.


class TBError(Exception):
    """Base class for other ThunderBase errors."""


# ThunderBase database errors.


class ThunderBaseNotFound(TBError):
    """Raised when a given ThunderBase isn't found."""


# ThunderBase name errors.


class ThunderBaseNameEmpty(TBError):
    """Raised when the name of the ThunderBase is given empty."""


class ThunderBaseInvalidName(TBError):
    """Raised when the name of the database is not a string."""


# ThunderBase password errors.


class ThunderBasePasswordEmpty(TBError):
    """Raised when the password of the database is empty."""


class ThunderBaseInvalidPassword(TBError):
    """Raised when the password of the database is not a string."""


# Table errors


class TableNotFound(TBError):
    """Raised when a given table is not found."""


# Table property errors.

class TableNameEmpty(TBError):
    """Raised when the name of a table is null or empty."""


class TableNameInvalid(TBError):
    """Raised when the name of a table is not a string."""


class TableSchemaEmpty(TBError):
    """Raised when the schema of the given table is null of empty."""


class TableSchemaInvalid(TBError):
    """Raised when the schema of the given table is not a dict."""


# Table record errors.


class TableRecordEmpty(TBError):
    """Raised when the given record is empty."""


# Errors while adding a record to the table.
class TableRecordInvalid(TBError):
    """Raised when the type of the given record is not a dictionary."""


class RecordFieldsIncorrect(TBError):
    """Raised when the record schema doesn't match the table schema."""


class RecordFieldNotOfSpecifiedType(TBError):
    """Raised when the record schema value doesn't match the schema value datatype."""
