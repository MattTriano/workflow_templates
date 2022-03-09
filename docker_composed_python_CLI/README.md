# More Robust Simple Python CLI Application 

This builds on the simple workflow for containerizing a python CLI program by 
* adding in a volume to hold persistant storage of data developed in the container, and 
* packaging logic into a `docker-compose.yml` file 

## Usage
From the directory containing the `docker-compose.yml` file, first build the application

```bash
user@host:.../docker_composed_python_CLI$ ls
docker-compose.yml  images  README.md
user@host:.../docker_composed_python_CLI$ docker-compose build
```

Then spin it up (include the `-d` flag if you want to `detach` the container from the terminal) 

```bash
user@host:.../docker_composed_python_CLI$ docker-compose up
```

and from another terminal screen, you can see that it's running via

```bash
docker_composed_python_CLI$ docker ps
CONTAINER ID   IMAGE                COMMAND   CREATED          STATUS          PORTS     NAMES
4a88c6159cdf   socrata/python_cli   "bash"    40 seconds ago   Up 39 seconds             docker_composed_python_cli
```

and to get an interactivate bash terminal in the container, you can enter either of the commands below (you can use either the container ID or the container name).

```bash
docker exec -it docker_composed_python_cli bash
docker exec -it 4a88c6159cdf bash
```

This will give you a bash terminal within the container, and using the command below, you can get data and persist it to the volume specified in the `docker-compose.yml` file.

```bash
python scripts/get_metadata.py -t "ewy2-6yfk" -o data_raw/
```

## Security

At present, this is for non-prod use only.