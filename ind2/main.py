from _pydatetime import date

from ind2.savers.csv_saver import CSVSaver
from ind2.models.desired_perfomance import DesiredPerformance
from ind2.models.real_perfomance import RealPerformance
from ind2.models.student import Student
from ind2.models.student_data import StudentData
from ind2.savers.json_saver import JsonSaver
from ind2.savers.xml_saver import XMLSaver

BASE_PATH = "Yemelyanov_PDM51_IND5"

student = Student("Ємельянов Владислав Богданович", "ПДМ-51", date(2004, 8, 23))
real_perf = RealPerformance(["DevOps", "Python"], [85, 90])
desired_perf = DesiredPerformance(["DevOps", "Python"], [95, 100])
data = StudentData(student, real_perf, desired_perf)

student1 = Student("Дикало Андрій Юрійович", "ПДМ-51", date(2004, 10, 17))
real_perf1 = RealPerformance(["DevOps", "Python"], [90, 90])
desired_perf1 = DesiredPerformance(["DevOps", "Python"], [98, 100])
data1 = StudentData(student1, real_perf1, desired_perf1)

students_data = [
    data.to_dictionary(),
    data1.to_dictionary(),
]

JsonSaver().save(students_data, BASE_PATH + ".json")
XMLSaver().save(students_data, BASE_PATH + ".xml")
CSVSaver().save(students_data, BASE_PATH + ".csv")