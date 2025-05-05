# AngelBox-OS-Русская версия
Описание   СИСТЕМА СДЕЛАНА НА DEEPSEEK!  СИСТЕМА СДЕЛАНА НА DEEPSEEK!
AngelBox OS - это легковесная операционная система на Python, предназначенная для образовательных целей и экспериментов. Система предоставляет:

Файловые операции (ls, cd, mkdir, rm и др.)

Управление процессами

Пакетный менеджер

Мультипользовательский режим

Разграничение прав (пользователь/root)

Установка
Клонируйте репозиторий:

bash
git clone https://github.com/yourusername/angelbox.git
cd angelbox
Установите зависимости:

bash
pip install -r requirements.txt
Запустите систему:

bash
python main.py
Первый запуск
При первом запуске система предложит создать администратора:

First run! Create admin user:
Username: admin
Password: ********
Admin user created successfully!
Основные команды
Файловые операции
Команда	Описание	Пример
ls	Список файлов	ls
cd	Сменить директорию	cd /path
mkdir	Создать директорию	mkdir new_dir
rm	Удалить файл	rm file.txt
cp	Копировать	cp src.txt dst.txt
mv	Переместить/переименовать	mv old.txt new.txt
Системные команды
Команда	Описание	Пример
date	Дата и время	date
ps	Список процессов	ps
kill	Завершить процесс	kill 1234
Администрирование
Команда	Описание	Пример
su	Стать root	su
useradd	Добавить пользователя	useradd newuser
passwd	Сменить пароль	passwd
Лицензия
MIT License

English Version    
THE SYSTEM IS MADE ON DEEPSEEK!          
THE SYSTEM IS MADE ON DEEPSEEK!          
THE SYSTEM IS MADE ON DEEPSEEK!
THE SYSTEM IS MADE ON DEEPSEEK!
Description
AngelBox OS is a lightweight Python-based operating system designed for educational purposes and experiments. The system provides:

File operations (ls, cd, mkdir, rm etc.)

Process management

Package manager

Multi-user mode

Permission system (user/root)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/angelbox.git
cd angelbox
Install dependencies:

bash
pip install -r requirements.txt
Run the system:

bash
python main.py
First Run
On first launch the system will prompt to create an admin:

First run! Create admin user:
Username: admin
Password: ********
Admin user created successfully!
Basic Commands
File Operations
Command	Description	Example
ls	List files	ls
cd	Change directory	cd /path
mkdir	Create directory	mkdir new_dir
rm	Remove file	rm file.txt
cp	Copy file	cp src.txt dst.txt
mv	Move/rename	mv old.txt new.txt
System Commands
Command	Description	Example
date	Show date/time	date
ps	List processes	ps
kill	Kill process	kill 1234
Administration
Command	Description	Example
su	Become root	su
useradd	Add user	useradd newuser
passwd	Change password	passwd
License
MIT License

Дополнительные материалы
Структура проекта
angelbox/
├── core/           # Ядро системы
├── commands/       # Команды shell
├── data/           # Данные системы
├── docs/           # Документация
├── tests/          # Тесты
├── main.py         # Точка входа
├── README.md       # Этот файл
└── requirements.txt
Для разработчиков
Добавление новых команд:

Создайте файл в commands/

Реализуйте функцию команды

Добавьте в shell.py в словарь commands

Запуск тестов:

bash
python -m pytest tests/
Сборка:

bash
python setup.py sdist bdist_wheel
