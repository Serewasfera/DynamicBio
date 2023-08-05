# DynamicBio
Set yourself a dynamic status in Scratch!

Запустите программу, закройте программу и откройте созданный в папке с программой файл config.ini.
Настройте программу через config.ini.

#### Обозначения конфига:
**BIOs** - укажите здесь текст для динамического статуса. Пример:
```
[BIOs]
bio1 = Привет! Это поле постоянно меняется!
bio2 = Статус: В сети!
bio3 = *работает над проектом*
```
**User** - укажите здесь имя пользователя и пароль от твоего Scratch аккаунта. Пример:
```
[User]
name = CaT_cRuSh
password = pwdpwd123
```
**Options** - укажите здесь дополнительные параметры.

cooldown - время в секундах, через которое будет меняться текст.
mode - режим работы. Имеет 2 значения: bio и wiwo. bio - менять поле "Обо мне". wiwo - менять поле "над чем я работаю"

Пример:
```
[Options]
cooldown = 10
mode = bio
```
