# AI that finds objects in images

## How to run?

Install everything from `requirements.txt`
```shell
sh get_weights.sh 
```

```shell
python manage.py runserver
```

Or with docker

```shell
sudo docker build --tag objai .
sudo docker run -it -p 8000:8000 objai 0.0.0.0:8000
```