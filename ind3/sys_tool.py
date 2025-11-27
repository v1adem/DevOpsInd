import sys

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Використання: python sys_tool.py")
        print("Друкує: 'командна строка' при прямому запуску.")
        return

    print("командна строка")


if __name__ == "__main__":
    main()
