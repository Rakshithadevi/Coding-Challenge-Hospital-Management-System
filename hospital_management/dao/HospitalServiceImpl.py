# dao/HospitalServiceImpl.py

import mysql.connector
from entity.Appointment import Appointment
from dao.IHospitalService import IHospitalService
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException
from util.DBConnUtil import DBConnUtil


class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()
        self.cursor = self.conn.cursor()

    def getAppointmentById(self, appointmentId: int) -> Appointment:
        query = "SELECT * FROM Appointment WHERE appointmentId = %s"
        self.cursor.execute(query, (appointmentId,))
        row = self.cursor.fetchone()
        if row:
            return Appointment(*row)
        else:
            return None

    def getAppointmentsForPatient(self, patientId: int) -> list:
        query = "SELECT * FROM Appointment WHERE patientId = %s"
        self.cursor.execute(query, (patientId,))
        rows = self.cursor.fetchall()
        if not rows:
            raise PatientNumberNotFoundException(f"Patient with ID {patientId} not found.")
        return [Appointment(*row) for row in rows]

    def getAppointmentsForDoctor(self, doctorId: int) -> list:
        query = "SELECT * FROM Appointment WHERE doctorId = %s"
        self.cursor.execute(query, (doctorId,))
        rows = self.cursor.fetchall()
        return [Appointment(*row) for row in rows]

    def scheduleAppointment(self, appointment: Appointment) -> bool:
        query = """
        INSERT INTO Appointment (patientId, doctorId, appointmentDate, description)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (
            appointment.get_patientId(),
            appointment.get_doctorId(),
            appointment.get_appointmentDate(),
            appointment.get_description()
        ))
        self.conn.commit()
        return True

    def updateAppointment(self, appointment: Appointment) -> bool:
        query = """
        UPDATE Appointment
        SET patientId=%s, doctorId=%s, appointmentDate=%s, description=%s
        WHERE appointmentId=%s
        """
        self.cursor.execute(query, (
            appointment.get_patientId(),
            appointment.get_doctorId(),
            appointment.get_appointmentDate(),
            appointment.get_description(),
            appointment.get_appointmentId()
        ))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def cancelAppointment(self, appointmentId: int) -> bool:
        query = "DELETE FROM Appointment WHERE appointmentId = %s"
        self.cursor.execute(query, (appointmentId,))
        self.conn.commit()
        return self.cursor.rowcount > 0
