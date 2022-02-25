# pysecuresql
## A Python package for easy and secure mysql interaction.

## Installation Instructions.
1. Clone the repo: `git clone git@github.com:Ujjawal-K-Panchal/pysecuresql.git`
2. Create a Virtual Environment: (Optional but Recommended).
  - `pip install virtualenv`.
  - `python -m venv <any-name>`.
  - Linux, Mac: `source <any-name>/bin/activate`. Windows: `<any-name>\Scripts\activate`.
3. Install the repo: `pip install ./pysecuresql`

## Usage Example:

```python
from ssql.connector import Connection

Connection(creds = (user, password, host, db)) #credentials for connecting to mysql server.

#sample 1. With Dictionary and Named Parameters.
user = connection.query("SELECT * FROM Mytable WHERE Name = %(username)s;", {"username": "XYZ"})

#sample 2. With List.
user = connection.query("SELECT * FROM Mytable WHERE Name = %s;", ["XYZ",])

#sample 3. With Tuple.
user = connection.query("SELECT * FROM Mytable WHERE Name = %s;", ("XYZ",))
```

