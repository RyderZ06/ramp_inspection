import customtkinter as ctk

class ApplicationWindow:
    """Управление главным окном приложения."""

    def __init__(self, title="DATA-SLATE (RAMP INSPECTIONS INFORMATION)", resizable=False):
        self._configure_appearance()
        self.window = ctk.CTk()
        self._setup_window(title, resizable)
        self.root = self._create_root_frame()

        # Конфигурация сетки для расширения вкладок
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

    def _configure_appearance(self):
        # Modes: system (default), light, dark
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme(
            "dark-blue"
        )  # Themes: blue (default), dark-blue, green

    def _setup_window(self, title, resizable):
        self.window.title(title)
        self.window.resizable(resizable, resizable)

    def _create_root_frame(self):
        frame = ctk.CTkFrame(self.window)
        frame.grid(
            row=0, column=0, sticky="nsew"
        )  # Используем grid вместо pack и привязываем ко всем сторонам
        return frame

    def run(self):
        self.window.mainloop()

