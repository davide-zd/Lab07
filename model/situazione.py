#import datetime
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Situazione:
    Localita: str
    Data: datetime.date
    Umidita: int


    def __hash__(self):
        return hash((self.Localita, self.Data))

    def __str__(self):
        return f"[{self.Localita} - {self.Data}] Umidità = {self.Umidita}"