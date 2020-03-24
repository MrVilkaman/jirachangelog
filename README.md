# Описание
Заточено под Jira Workflow команды Skyeng Mobile Platform

Утилита для создания форматирование release notes из git истории
* Находит все jira задачи из истории git
* Группирует задачи по типам
* Считает diff по строкам
* Добавлеяет дополнительную информацию об билде\ветке\заинтересованных лицах
* Собирает jira задачи в удобнов виде для просмотра в web

# Настройка
Note: Проверено для Windows

Шаг первый
```
cp ./env.sh.example ./env.sh
```
Шаг втрой
Отредактироват
`./env.sh`

Шаг третий
```
source ./env.sh
```

Шаг четверный

запустить `./install.sh`


# Пример использования

Посчитать diff между ветками origin/platform/develop и HEAD с название версии Skyeng 5.40.0 и записать его в файл build.txt
```
 jiralog.sh -v 5.40.0 -s -p HEAD..origin/platform/develop   > build.txt
```

Посмотреть все возможные аргументы

```
 jiralog.sh -h
```