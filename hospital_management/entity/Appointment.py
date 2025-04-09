class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate="", description=""):
        self.__appointmentId = appointmentId
        self.__patientId = patientId
        self.__doctorId = doctorId
        self.__appointmentDate = appointmentDate
        self.__description = description

    def get_appointmentId(self): return self.__appointmentId
    def set_appointmentId(self, appointmentId): self.__appointmentId = appointmentId

    def get_patientId(self): return self.__patientId
    def set_patientId(self, patientId): self.__patientId = patientId

    def get_doctorId(self): return self.__doctorId
    def set_doctorId(self, doctorId): self.__doctorId = doctorId

    def get_appointmentDate(self): return self.__appointmentDate
    def set_appointmentDate(self, appointmentDate): self.__appointmentDate = appointmentDate

    def get_description(self): return self.__description
    def set_description(self, description): self.__description = description

    def __str__(self):
        return f"Appointment[ID={self.__appointmentId}, PatientID={self.__patientId}, DoctorID={self.__doctorId}, Date={self.__appointmentDate}, Description={self.__description}]"
