Запуск тестов: python3 -m pytest tests/test_films.py --no-header --no-summary -q  
Запуск с покрытием: coverage run -m pytest tests/test_films.py --no-header --no-summary -q  
Сформировать отчет: coverage html  
Просмотреть отчет: открыть htmlcov/index.html, на локалке http://localhost:63342/films_api/htmlcov/index.html  
heroku: https://dashboard.heroku.com/apps/films-apiapp/deploy/heroku-container  
travis: https://travis-ci.com/github/Wrelin/films_api
