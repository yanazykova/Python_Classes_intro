class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        

    def has_name(self):
        return self.name

    def student_can_update_name(self, new_name):
        self.name = new_name
        return self.name

    def has_cohort(self):
        return self.cohort

    def student_can_update_cohort(self, new_cohort):
        self.cohort = new_cohort
        return self.cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return "I love " + favourite_language
