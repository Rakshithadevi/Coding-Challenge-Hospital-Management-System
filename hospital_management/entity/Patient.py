

class Patient:
    def __init__(self, patientId=None, firstName="", lastName="", dateOfBirth="", gender="", contactNumber="", address=""):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    # Getters and Setters
    def get_patientId(self): return self.__patientId
    def set_patientId(self, patientId): self.__patientId = patientId

    def get_firstName(self): return self.__firstName
    def set_firstName(self, firstName): self.__firstName = firstName

    def get_lastName(self): return self.__lastName
    def set_lastName(self, lastName): self.__lastName = lastName

    def get_dateOfBirth(self): return self.__dateOfBirth
    def set_dateOfBirth(self, dob): self.__dateOfBirth = dob

    def get_gender(self): return self.__gender
    def set_gender(self, gender): self.__gender = gender

    def get_contactNumber(self): return self.__contactNumber
    def set_contactNumber(self, contact): self.__contactNumber = contact

    def get_address(self): return self.__address
    def set_address(self, address): self.__address = address

    def __str__(self):
        return f"Patient[ID={self.__patientId}, Name={self.__firstName} {self.__lastName}, DOB={self.__dateOfBirth}, Gender={self.__gender}, Contact={self.__contactNumber}, Address={self.__address}]"
