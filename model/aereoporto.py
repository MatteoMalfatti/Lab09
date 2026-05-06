from dataclasses import dataclass
@dataclass
class Aereoporto:

   ID:int
   AIRPORT:str


   def __hash__(self):
       return hash(self.ID)


   def __eq__(self, other):
       return self.ID==other.ID


   def __str__(self):
       return f"{self.ID} {self.AIRPORT}"

