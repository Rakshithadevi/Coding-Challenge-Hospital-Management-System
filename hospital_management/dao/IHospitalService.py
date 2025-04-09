# dao/IHospitalService.py

from abc import ABC, abstractmethod
from entity.Appointment import Appointment

class IHospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointmentId: int) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId: int) -> list:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId: int) -> list:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId: int) -> bool:
        pass
