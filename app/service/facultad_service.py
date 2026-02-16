from repository.facultad_repo import FacultadRepo
from models.facultad import Facultad

class FacultadService:
    def __init__(self):
        self.facultad_repo = FacultadRepo()
 