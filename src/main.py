from ui import *

TAB_NAMES = ["MAIN"]
TEXT_TO_DISPLAY = "Some text here"


def main():
    app = ApplicationWindow()

    # Создание вкладок
    tab_main = TabViewMain(app.root, TAB_NAMES[0], TEXT_TO_DISPLAY)
    tab_insp = TabViewCore(app.root, "РУТИНА")

    # Расположение вкладок
    tab_main.tabview.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    tab_insp.tabview.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

    app.run()


if __name__ == "__main__":
    main()
