class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

    def __add__(self, other):
        proteins = self.proteins+other.proteins
        carbs = self.carbs+other.carbs
        fats = self.fats+other.fats
        return NutritionInfo(proteins, carbs,fats)

    def __mul__(self, number):
        proteins = self.proteins*number
        carbs = self.carbs*number
        fats = self.fats*number
        return NutritionInfo(proteins, carbs,fats)


tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)


breakfast = apple * 2 + tvorog_9
print(breakfast.energy())