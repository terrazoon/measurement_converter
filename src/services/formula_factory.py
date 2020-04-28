class FormulaFactory:
    formula_map = {}

    def __init__(self):
        self.formula_map = {
            'fc': self.f_to_c,
            'fk': self.f_to_k,
            'fr': self.f_to_r,
            'cf': self.c_to_f,
            'ck': self.c_to_k,
            'cr': self.c_to_r,
            'kf': self.k_to_f,
            'kc': self.k_to_c,
            'kr': self.k_to_r,
            'rf': self.r_to_f,
            'rc': self.r_to_c,
            'rk': self.r_to_k
        }

    def get_formula(self, from_unit, to_unit):
        return self.formula_map[from_unit + to_unit]

    @staticmethod
    def f_to_c(my_input):
        return (my_input - 32) * 5 / 9

    @staticmethod
    def f_to_k(my_input):
        return (my_input - 32) * 5 / 9 + 273.15

    @staticmethod
    def f_to_r(my_input):
        return my_input + 459.67

    @staticmethod
    def c_to_f(my_input):
        return (my_input * 9 / 5) + 32

    @staticmethod
    def c_to_k(my_input):
        return my_input + 273.15

    @staticmethod
    def c_to_r(my_input):
        return (my_input * 9 / 5) + 491.67

    @staticmethod
    def k_to_f(my_input):
        return (my_input - 273.15) * 9 / 5 + 32

    @staticmethod
    def k_to_c(my_input):
        return my_input - 273.15

    @staticmethod
    def k_to_r(my_input):
        return my_input * 9 / 5

    @staticmethod
    def r_to_f(my_input):
        return my_input - 459.67

    @staticmethod
    def r_to_c(my_input):
        return (my_input - 491.67) * 5 / 9

    @staticmethod
    def r_to_k(my_input):
        return my_input * 5 / 9
