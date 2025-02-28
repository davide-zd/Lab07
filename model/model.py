from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def get_misure(self, mese):
        return DAO.get_misure(mese)
