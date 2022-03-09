# Simple Python CLI application
This shows a simple workflow for containerizing a python CLI program.

## Workflow

Build the container

```bash
docker build --tag py_cli_in_docker .
```

This will install the packages defined in `requirements.txt` into the container. You can then run the container via the command

```bash
docker run -it py_cli_in_docker
```

This will leave you with a bash command line from which you can test your application.

For this specific app, you can execute code via 

```bash
app_user@695c9b296b88:~$ mkdir data_raw
app_user@695c9b296b88:~$ python scripts/get_metadata.py -t "ewy2-6yfk" -o data_raw/
INFO:root:Fetching metadata for Socrata table ewy2-6yfk)
```

and by `cd`ing into `data_raw/`, you'll find the metadata for the socrata table with table_id "ewy2-6yfk", which is the boundary of Chicago.