# exception/PatientNumberNotFoundException.py

class PatientNumberNotFoundException(Exception):
    def __init__(self, message="Patient ID not found in the database."):
        super().__init__(message)
