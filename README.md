# aq-hot-swap-db
A python script for swapping SQL databases in a Dockerized Aquarium instance

## Usage
**This script is intended to be used on local installations for testing code. DO NOT try to use this script on your production database!**

Copy the file `hot_swap_db.py` into the top level of your Aquarium directory. Assuming that you haven't changed the default SQL credentials, the username will be set correctly in the script. When running the script, you will be prompted for the SQL password, which is `aSecretAquarium`. (If you have changed the credentials, then you're probably using a database you care about and this script might not be what you're looking for.)

To create a dump of the database, run:

```
python hot_swap_db.py -d
```
By default, this will save to a file called `hot_swap.sql` in the top level of your Aquarium directory. If you would like to save it somewhere else, add the `-f` option:

```
python hot_swap_db.py -d -f myfile.sql
```

To load the database, run:

```
python hot_swap_db.py -l
```

The script will display a warning and request confirmation before overwriting your database:

```
WARNING: This will overwrite the current database with the file hot_swap.sql.
Would you like to proceed? (y/n)
```

You can add the same `-f` option to specify which file to load from.
