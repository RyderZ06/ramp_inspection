Установка менеджера пакетов Chocolatey.
1. Откройте меню "Пуск", введите cmd, 
затем щёлкните правой кнопкой мыши по "Командная строка"
и выберите "Запуск от имени администратора".

2. Введите команду установки Chocolatey в открывшемся окне:
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

3. Проверьте установку менеджера командой:
choco --version

4. Установить программы через install_programs.bat

5. Обновлять все установленные приложения:
choco upgrade all -y

6. Искать пакеты:
choco search <имя_пакета>