from data.basedao import BaseDao, PersistsDao


class RwiDao(PersistsDao):

    def __init__(self):
        super().__init__('RWI')

    # var = tk.StringVar()
    # var.trace_add('write', callback)
    # @property
    # def work_type(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # @work_type.setter
    # def work_type(self, name):
    #     print("Setter for the name")
    #     self.first_name, self.last_name = name.split()


class WorkTypeDao(BaseDao):

    def __init__(self):
        super().__init__('WORK_TYPE')


class TShirtDao(BaseDao):

    def __init__(self):
        super().__init__('TSHIRT')
