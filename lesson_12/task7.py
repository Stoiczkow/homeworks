

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def ze_stringa(cls, input: str):
        splitted_input = input.split(sep="-")
        return cls(int(splitted_input[0]), int(splitted_input[1]), int(splitted_input[2]))

example = Data.ze_stringa("12-10-1990")
print(example.year)