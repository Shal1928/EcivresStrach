from model.base import Base


class RWI(Base):

    def __init__(self, title, comment, is_plan, work_type, tshirt, rowid=None):
        self.__init__(title, rowid)
        self.comment = comment
        self.is_plan = is_plan
        self.work_type = work_type
        self.tshirt = tshirt

    # @property
    # def work_type(self):
    #     return f"{self.first_name} {self.last_name}"
    #
    # @work_type.setter
    # def work_type(self, name):
    #     print("Setter for the name")
    #     self.first_name, self.last_name = name.split()
