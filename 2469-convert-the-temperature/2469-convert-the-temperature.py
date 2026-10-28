class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        kelvin =0
        Fahrenheit=0

        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        return [round(Kelvin, 2), round(Fahrenheit, 3)]