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


```bash
python scripts/get_metadata.py -t "ewy2-6yfk" -o data_raw/
```


I'm having a bit of trouble with this last step, in that the container's `app_user` doesn't seem to have permission to write to the volume. I still have to debug that. I suspect I'll have to do some permission-granting host-side.