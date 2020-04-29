class VolumeFactory:
    formula_map = {}

    def __init__(self):
        self.formula_map = {
            # liters to cups, cubic feet, gallons, cubic inches, and tablespoons
            'lc': self.liters_to_cups,
            'lf': self.liters_to_cubic_feet,
            'lg': self.liters_to_gallons,
            'li': self.liters_to_cubic_inches,
            'lt': self.liters_to_tablespoons,

            # cups
            'cf': self.cups_to_cubic_feet,
            'cg': self.cups_to_gallons,
            'ci': self.cups_to_cubic_inches,
            'cl': self.cups_to_liters,
            'ct': self.cups_to_tablespoons,

            # tablespoons
            'tc': self.tablespoons_to_cups,
            'tf': self.tablespoons_to_cubic_feet,
            'tg': self.tablespoons_to_gallons,
            'ti': self.tablespoons_to_cubic_inches,
            'tl': self.tablespoons_to_liters,

            # gallons
            'gc': self.gallons_to_cups,
            'gf': self.gallons_to_cubic_feet,
            'gi': self.gallons_to_cubic_inches,
            'gl': self.gallons_to_liters,
            'gt': self.gallons_to_tablespoons,

            # cubic feet
            'fc': self.cubic_feet_to_cups,
            'fg': self.cubic_feet_to_gallons,
            'fi': self.cubic_feet_to_cubic_inches,
            'fl': self.cubic_feet_to_liters,
            'ft': self.cubic_feet_to_tablespoons,

            #  inches
            'ic': self.cubic_inches_to_cups,
            'if': self.cubic_inches_to_cubic_feet,
            'ig': self.cubic_inches_to_gallons,
            'il': self.cubic_inches_to_liters,
            'it': self.cubic_inches_to_tablespoons

        }

    def get_formula(self, from_unit, to_unit):
        return self.formula_map[from_unit + to_unit]

    @staticmethod
    def liters_to_tablespoons(my_input):
        return my_input * 67.628

    @staticmethod
    def tablespoons_to_liters(my_input):
        return my_input / 67.628

    @staticmethod
    def liters_to_cubic_inches(my_input):
        return my_input * 61.028

    @staticmethod
    def cubic_inches_to_liters(my_input):
        return my_input / 61.028

    @staticmethod
    def liters_to_cups(my_input):
        return my_input * 4.22675

    @staticmethod
    def cups_to_liters(my_input):
        return my_input / 4.22675

    @staticmethod
    def liters_to_cubic_feet(my_input):
        return my_input * 0.0353147

    @staticmethod
    def cubic_feet_to_liters(my_input):
        return my_input / 0.0353147

    @staticmethod
    def gallons_to_liters(my_input):
        return my_input * 3.78541

    @staticmethod
    def liters_to_gallons(my_input):
        return my_input / 3.78541

    @staticmethod
    def gallons_to_cups(my_input):
        x = VolumeFactory.gallons_to_liters(my_input)
        y = VolumeFactory.liters_to_cups(x)
        return y

    @staticmethod
    def cups_to_gallons(my_input):
        x = VolumeFactory.cups_to_liters(my_input)
        y = VolumeFactory.liters_to_gallons(x)
        return y

    @staticmethod
    def cubic_feet_to_cubic_inches(my_input):
        return my_input * 12 * 12 * 12

    @staticmethod
    def cubic_inches_to_cubic_feet(my_input):
        return my_input / (12 * 12 * 12)

    @staticmethod
    def cups_to_tablespoons(my_input):
        return my_input * 16

    @staticmethod
    def tablespoons_to_cups(my_input):
        return my_input / 16

    @staticmethod
    def cups_to_cubic_feet(my_input):
        return my_input / 119.688

    @staticmethod
    def cubic_feet_to_cups(my_input):
        return my_input * 119.688

    @staticmethod
    def cups_to_cubic_inches(my_input):
        return my_input * 14.438

    @staticmethod
    def cubic_inches_to_cups(my_input):
        return my_input / 14.438

    @staticmethod
    def gallons_to_tablespoons(my_input):
        return my_input * 256

    @staticmethod
    def tablespoons_to_gallons(my_input):
        return my_input / 256

    @staticmethod
    def tablespoons_to_cubic_feet(my_input):
        return my_input / 1915.01

    @staticmethod
    def cubic_feet_to_tablespoons(my_input):
        return my_input * 1915.01

    @staticmethod
    def tablespoons_to_cubic_inches(my_input):
        return my_input / 1.10823

    @staticmethod
    def cubic_inches_to_tablespoons(my_input):
        return my_input * 1.10823

    @staticmethod
    def gallons_to_cubic_inches(my_input):
        return my_input * 231

    @staticmethod
    def cubic_inches_to_gallons(my_input):
        return my_input / 231

    @staticmethod
    def gallons_to_cubic_feet(my_input):
        return my_input / 7.48052

    @staticmethod
    def cubic_feet_to_gallons(my_input):
        return my_input * 7.48052
