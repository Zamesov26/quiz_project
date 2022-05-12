# quiz_project
project for Bewise.ai

настройка
  postgres
    Файл - .env.prod настройка базы данных, данные уже заполннеы, но можно измнеить в случае необходимости
      POSTGRES_USER - имя пользователя
      POSTGRES_PASSWORD - пароль
      POSTGRES_DB - название базы данных
  
  app
    файл .env.prod содержит настроки для flask
      DATABASE_URL - Адрес баззые данные в случае изменния настроек для postgres также необходимо изменить
      
Запуск
(на компьютере должен быть установлен Docker)
- скачать все файлы в любую фапку(folder)
- перейти в нужную папку через командрую строку
- выполнить команду "docker-compose up -d --build"(без ковычек)
- перейти по адрессу http://localhost:1337/api/get_questions/1
