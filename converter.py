class NumberConverter:

    def __init__(self):
        self.units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

    def convert(self, number: int) -> str:

        answer = "[None]"

        if 0 <= number < 11:
            answer = self.units[number]

        return answer