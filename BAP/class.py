class Student:
    def set_student_id(self, id):
        self.student_id = id

    def set_telephone_no(self, tel_no):
        self.telephone_no = tel_no

    def get_student_id(self):
        return self.student_id

    def get_telephone_no(self):
        return self.telephone_no


student_obj = Student()
student_obj.set_student_id(1001)
student_obj.set_telephone_no(9201861311)

print("Student ID:", student_obj.get_student_id())
print("Telephone No:", student_obj.get_telephone_no())