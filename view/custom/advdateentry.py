from tkinter import END

from tkcalendar import DateEntry


class AdvDateEntry(DateEntry):
    def __init__(self, master=None, **options):
        super().__init__(master, **options)
        self.textvariable = None

        if 'textvar' in options:
            self.textvariable = options.get('textvar')
            if self.textvariable is not None:
                self._set_text(self.textvariable.get())

        self.bind("<<DateEntrySelected>>", self.on_select)

    def on_select(self, event):
        print('!!!')
        self.textvariable.set(str(self.get()))
