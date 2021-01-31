from tkinter import ttk


class Advcombobox(ttk.Combobox):

    def __init__(self, master=None, cnf={}, **options):
        self.dict = None

        if 'values' in options:
            if isinstance(options.get('values'), dict):
                self.dict = options.get('values')
                options['values'] = sorted(self.dict.values())

        # combobox constructor with list of keys
        super().__init__(master, **options)

        # assign some function
        self.bind('<<ComboboxSelected>>', self.on_select)

    def on_select(self, event):
        print(self.get(), self.get_value())

    def get(self):
        if self.dict:
            for key in self.dict.keys():
                if self.dict[key] == super().get():
                    return key
            else:
                return super().get()
        else:
            return super().get()

    def get_value(self):
        return super().get()
