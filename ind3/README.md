# Як протестувати завдання

## 1) sys_tool.py
- Прямий запуск:
    python ind3/sys_tool.py
- Імпорт:
    python -c "import src.sys_tool"

## 2) click_tool.py
    python ind3/click_tool.py say --name Alice
    python ind3/click_tool.py say --name peter

## 3) fire_expose.py
    python ind3/fire_expose.py greet Alice
    python ind3/fire_expose.py goodbye Bob
