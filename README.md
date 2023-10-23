# API-CRUD-user-automated-tests  
![](/project_logo.jpg "")  
[Demo video Jenkins](https://youtu.be/4JOUfq_fvq0)  
[Demo video Local](https://youtu.be/WBD1lMeQXAY)  
API автотесты проекта CRUD User Fastapi с использованием pytest + requests  
Подготовка тестового окружения под Windows:
1. Установить Docker Desktop  
2. Склонировать проект https://github.com/underoath2013/Fast-API-user-example.git
3. Выполнить команду  
```docker-compose up -d```  
4. Убедиться в успешном запуске всех контейнеров, ознакомиться с документацией по API http://127.0.0.1:8000/docs  
Дополнительная информация:  
Остановить сервисы можно командой ```docker-compose down```  
Для удаленного подключения к базе данных можно использовать Adminer http://127.0.0.1:8888/

Для локального запуска тестов:  
1. Cоздать виртуальное окружение
2. Установить зависимости командой  
```pip install -r requirements.txt```
3. Выполнить команду ```pytest```
4. Дождаться окончания выполнения тестов  
Дополнительная информация:  
Для локального запуска использовать psycopg2==2.9.9, для запуска тестов через docker psycopg2-binary==2.9.9  
При наличии ошибок на шаге 2, проверить какой psycopg2 вы устанавливаете

Для генерации и просмотра отчетности через Allure:  
1. Установить и настроить согласно официальной документации: https://allurereport.org/docs/gettingstarted/installation/  
2. После прохождения тестов выполнить команду ```allure generate allure-results -c```  
3. Для просмотра отчета выполнить команду ```allure open .\allure-report\```  

Для запуска тестов с использованием Docker:  
1. Проверить, что установлен Docker Desktop
2. Проверить, что запущен сервис API
3. Убедиться, что запускаемый контейнер с тестами и контейнеры с API находятся в одной network
4. Выполнить команду ```docker-compose up```  

Для запуска тестов с использованием Jenkins:
1. Проверить, что установлен Docker Desktop
2. Проверить, что запущен сервис API
3. Выполнить команду  
```docker run -d -p 8082:8080 -p 50000:50000 --restart=on-failure --name jenkins --network=fast-api-user-example_default/jenkins:lts-jdk17```  
4. Дополнительно установить необходимые пакеты в контейнер jenkins, выполнив последовательно команды  
```
docker exec -it -u 0 jenkins /bin/bash
apt-get update
apt-get install -y docker-compose
apt-get install python3
apt-get install python3-venv
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install allure
```  
5. В UI Jenkins (http://localhost:8082/) создать и настроить Pipeline, скопировав в Script содержимое из Jenkinsfile  
6. Запустить Pipeline, при этом отчетность Allure сгенерируется автоматически  
