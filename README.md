# anonbot

Бот для анонимного общения

## Инструкция по деплою на heroku.com

1. создай бота через бота @BotFather в телеграме
2. создай канал в телеграме
3. добавь бота в канал и датй ему право писать туда
4. сделай форк этого репозитория
5. зарегайся на heroku.com
6. New -> Create new app
7. придумываешь название и выбиираешь регион
8. тык на кнопку Create app
9. во вкладке Settings тыкнуть на Add buildpack
10. выбрать python
11. тык на Save changes
12. тык на Reveal Config Vars
13. в поле KEY введи TOKEN, а в поле VALUE вставь сам токен бота, после чего тыкни Add
14. в поле KEY введи CHANNEL, а в поле VALUE вставь @username канала, после чего тыкни Add
15. далее перейди во вкладку Deploy
16. где Deployment method тыкни GitHub
17. ща не могу проверить, полагаю заставит в гитхаб войти
18. выбери свой форк
19. тыкни на Deploy Branch
20. теперь всё должно работать

## Переменные среды необходимые для работы

TOKEN — токен бота

CHANNEL — юзернэйм канала с @

## С терминала запускается как-то так

```env TOKEN="YUOR_TOKEN" CHANNEL="@YOUR_CHANNEL_USERNAME" python main.py```