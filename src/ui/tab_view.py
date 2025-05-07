import customtkinter as ctk
from frames import *

class BaseTabView:
    """Базовый класс для управления вкладками интерфейса."""
    def __init__(
        self,
        root: object,
        tab_name: str,
        text_to_display: str = None,
        buttons: list = None
    ):
        self.root = root
        self.tab_name = tab_name
        self.text_to_display = text_to_display
        self.buttons = buttons
        # Основной виджет вкладок
        self.tabview = self._create_tab_view()
        # Размещаем tabview в сетке
        self.tabview.grid(row=0, column=0, sticky='nsew')
        self._add_content()

    def _create_tab_view(self) -> ctk.CTkTabview:
        raise NotImplementedError("Метод должен быть реализован в дочернем классе")

    def add_tab(self, tab_name: str, content_function=None):
        # Добавление новой вкладки в tabview
        self.tabview.add(tab_name)
        tab_frame = self._get_tab(tab_name)

        if content_function:
            # Вызываем функцию для добавления контента
            content_function(tab_frame)

    def _get_tab(self, tab_name: str):
        """Получение фрейма вкладки по имени."""
        return self.tabview.tab(tab_name)

    def _add_content(self) -> None:
        if self.buttons:
            self._create_buttons(self.tabview, self.buttons)

    def _create_text_label(self, tab_frame, text_to_display: str) -> None:
        label_font = ctk.CTkFont(family="Arial", size=12)
        ctk.CTkLabel(
            tab_frame,
            text=text_to_display,
            wraplength=180,
            font=label_font,
        ).pack(pady=5, padx=5, fill="both", expand=True)

    def _create_buttons(self, tab_frame, buttons: list) -> None:
        button_font = ctk.CTkFont(family="Arial", size=17, weight="bold")

        for idx, button in enumerate(buttons):
            button_obj = ctk.CTkButton(
                tab_frame,
                text=button["text"],
                command=button["command"],
                height=45,
                width=180,
                font=button_font,
                hover_color="red",
                corner_radius=8,
                cursor="hand2",
            )
            button_obj.grid(row=idx, column=0, sticky="ew", padx=10, pady=8)

    def get_tab_view(self):
        """Возвращает виджет tabview."""
        return self.tabview

class TabViewMain(BaseTabView):
    """Вкладка с основными настройками."""

    def _create_tab_view(self) -> ctk.CTkTabview:
        tabview = ctk.CTkTabview(
            self.root,
            width=1000,
            height=500,
            corner_radius=8,
            anchor="n",
        )
#        tabview.grid_columnconfigure(0, weight=1)  # Конфигурация расширения для вкладки
        return tabview

    def __init__(
        self,
        root: object,
        tab_name: str,
        text_to_display: str = None,
        buttons: list = None,
    ):
        super().__init__(root, tab_name, text_to_display, buttons)
        self.add_tab("STAFF RECORDS", content_function=self.create_staff_frame)
#        self.add_tab("AUDIT VIEWS", content_function=self.create_run_excel_viewer)

    def create_staff_frame(self, tab_frame):
        create_staff_frame(tab_frame)  # Вызов функции

#    def create_run_excel_viewer(self, tab_frame):
#        run_excel_viewer(tab_frame)

class TabViewCore(BaseTabView):
    """Вкладка с базовыми настройками."""
    def _create_tab_view(self) -> ctk.CTkTabview:
        tabview = ctk.CTkTabview(
            self.root,
            width=200,
            height=378,
            corner_radius=8,
            anchor="n"
        )
        return tabview

#    def __init__(self, root: object, tab_name: str = "LEAD", text_to_display: str = None, buttons: list = None):
#        super().__init__(root, tab_name, text_to_display, buttons)
#        self.add_tab("LINKS", content_function=self.create_links)
        
#    def create_links(self, tab_frame):
#        create_links(tab_frame)