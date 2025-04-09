from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException

def main():
    service = HospitalServiceImpl()

    while True:
        print("\n------ Hospital Management System -------")
        print("1. Get appointment by ID")
        print("2. Get appointments for patient")
        print("3. Get appointments for doctor")
        print("4. Schedule appointment")
        print("5. Update appointment")
        print("6. Cancel appointment")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                aid = int(input("Enter Appointment ID: "))
                appt = service.getAppointmentById(aid)
                print(appt if appt else "Appointment not found.")

            elif choice == '2':
                pid = int(input("Enter Patient ID: "))
                appts = service.getAppointmentsForPatient(pid)
                for appt in appts:
                    print(appt)

            elif choice == '3':
                did = int(input("Enter Doctor ID: "))
                appts = service.getAppointmentsForDoctor(did)
                for appt in appts:
                    print(appt)

            elif choice == '4':
                pid = int(input("Enter Patient ID: "))
                did = int(input("Enter Doctor ID: "))
                date = input("Enter Appointment Date (YYYY-MM-DD): ")
                desc = input("Enter Description: ")
                appt = Appointment(None, pid, did, date, desc)
                success = service.scheduleAppointment(appt)
                print("Appointment Scheduled!" if success else "Failed to schedule.")

            elif choice == '5':
                aid = int(input("Enter Appointment ID to Update: "))
                pid = int(input("Enter new Patient ID: "))
                did = int(input("Enter new Doctor ID: "))
                date = input("Enter new Date (YYYY-MM-DD): ")
                desc = input("Enter new Description: ")
                appt = Appointment(aid, pid, did, date, desc)
                success = service.updateAppointment(appt)
                print("Appointment Updated!" if success else "Update failed.")

            elif choice == '6':
                aid = int(input("Enter Appointment ID to Cancel: "))
                success = service.cancelAppointment(aid)
                print("Appointment Cancelled!" if success else "Cancellation failed.")

            elif choice == '7':
                print("Exiting. Goodbye!")
                break

            else:
                print("Invalid choice. Please select again.")

        except PatientNumberNotFoundException as e:
            print("Error:", e)

        except Exception as e:
            print("Unexpected Error:", e)

if __name__ == "__main__":
    main()
