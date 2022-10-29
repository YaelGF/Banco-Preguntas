# Config Ubuntu 20.04 and Python with FastAPI

## 1. Dockefile 

## 2. Build Docker image
```
docker build -t fastapi:v1 .
```

## 3. Create docker container
nota:regresar a la carpeta principal
```
cd ..
```

```
docker run -it -v $(pwd)/backend:/Api-Rest --net host --name fastapi -h python fastapi:v1
```

## 4. Run Web Page

```
$ uvicorn Api-Rest.main:app --reload
```

## 5. Start docker

```bash
    $ docker start -i name
```

## 6. Delete docker

```bash
    $ docker rm id-docker
```
## 7. Delete imagen

```bash
    $ docker rmi id-imagen
```
## 8. Show images

```bash
    $ docker images
```
## 9. Show Dockers

```bash
    $ docker ps -a
```