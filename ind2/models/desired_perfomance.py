from ind2.models.perfomance import Performance


class DesiredPerformance(Performance):
    def __init__(self, subjects: list[str], desired_grades: list[int]):
        super().__init__(subjects, desired_grades)

    def average_grade(self):
        return sum(self.get_grades()) / len(self.get_grades()) if self.get_grades() else 0