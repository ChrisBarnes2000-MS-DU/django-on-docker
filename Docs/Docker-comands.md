
## To see which environment variables are available to the web service, run:
```bash
$ docker-compose run web env
```

## To make migrations, run:
```bash
$ docker-compose run web / usr/local/bin/python manage.py migrate
```

## To check the security
```bash
$ python manage.py check - -deploy
```

## Build & Run
```bash
$ docker-compose up --build
```

## To view the logs:
```bash
$ docker-compose logs
```

## Stop
```bash
$ docker-compose down
```


<!--
docker volume inspect <FILENAME_postgres_data>

docker-compose -f docker-compose.prod.yml logs -f

docker-compose -f docker-compose.prod.yml up -d --build
-->
