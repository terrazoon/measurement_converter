class VolumeFactory:
    formula_map = {}


    def __init__(self):
        self.formula_map = {
            # liters to cups, cubic feet, gallons, cubic inches, and tablespoons
            'lc': self.l_to_c,
            'lf': self.l_to_f,
            'lg': self.l_to_g,
            'li': self.l_to_i,
            'lt': self.l_to_t,

            # cups
            'cf': self.c_to_f,
            'cg': self.c_to_g,
            'ci': self.c_to_i,
            'cl': self.c_to_l,
            'ct': self.c_to_t,

            # tablespoons
            'tc': self.t_to_c,
            'tf': self.t_to_f,
            'tg': self.t_to_g,
            'ti': self.t_to_i,
            'tl': self.t_to_l,

            # gallons
            'gc': self.g_to_c,
            'gf': self.g_to_f,
            'gi': self.g_to_i,
            'gl': self.g_to_l,
            'gt': self.g_to_t,

            # cubic feet
            'fc': self.f_to_c,
            'fg': self.f_to_g,
            'fi': self.f_to_i,
            'fl': self.f_to_l,
            'ft': self.f_to_t,

            #cubic inches
            'ic': self.i_to_c,
            'if': self.i_to_f,
            'ig': self.i_to_g,
            'il': self.i_to_l,
            'it': self.i_to_t

        }

    def get_formula(self, from_unit, to_unit):
        return self.formula_map[from_unit + to_unit]

    @staticmethod
    def l_to_t(my_input):
        return my_input * 67.628

    @staticmethod
    def t_to_l(my_input):
        return my_input / 67.628

    @staticmethod
    def l_to_i(my_input):
        return my_input * 61.028

    @staticmethod
    def i_to_l(my_input):
        return my_input / 61.028

    @staticmethod
    def l_to_c(my_input):
        return my_input * 4.22675

    @staticmethod
    def c_to_l(my_input):
        return my_input / 4.22675

    @staticmethod
    def l_to_f(my_input):
        return my_input * 0.0353147

    @staticmethod
    def f_to_l(my_input):
        return my_input / 0.0353147

    @staticmethod
    def g_to_l(my_input):
        return my_input * 3.78541

    @staticmethod
    def l_to_g(my_input):
        return my_input / 3.78541

    @staticmethod
    def g_to_c(my_input):
        print(f'g to c: my_input= {my_input}')
        x = VolumeFactory.g_to_l(my_input)
        print(f'g to l: x= {x}')
        y = VolumeFactory.l_to_c(x)
        print(f'l to c: y= {y}')
        return y

    @staticmethod
    def c_to_g(my_input):
        print(f"c to g my_input={my_input}")
        x = VolumeFactory.c_to_l(my_input)
        print(f"c to l x= {x}")
        y = VolumeFactory.l_to_g(x)
        print(f"l_to_g y= {y}")
        return y

    @staticmethod
    def f_to_i(my_input):
        return my_input * 12 * 12 * 12

    @staticmethod
    def i_to_f(my_input):
        return my_input / (12 * 12 * 12)

    @staticmethod
    def c_to_t(my_input):
        return my_input * 16

    @staticmethod
    def t_to_c(my_input):
        return my_input / 16

    @staticmethod
    def c_to_f(my_input):
        return my_input / 119.688

    @staticmethod
    def f_to_c(my_input):
        return my_input * 119.688

    @staticmethod
    def c_to_i(my_input):
        return my_input * 14.438

    @staticmethod
    def i_to_c(my_input):
        return my_input / 14.438

    @staticmethod
    def g_to_t(my_input):
        return my_input * 256

    @staticmethod
    def t_to_g(my_input):
        return my_input / 256

    @staticmethod
    def t_to_f(my_input):
        return my_input / 1915.01

    @staticmethod
    def f_to_t(my_input):
        return my_input * 1915.01

    @staticmethod
    def t_to_i(my_input):
        return my_input / 1.10823

    @staticmethod
    def i_to_t(my_input):
        return my_input * 1.10823

    @staticmethod
    def g_to_i(my_input):
        return my_input * 231

    @staticmethod
    def i_to_g(my_input):
        return my_input / 231

    @staticmethod
    def g_to_f(my_input):
        return my_input / 7.48052

    @staticmethod
    def f_to_g(my_input):
        return my_input * 7.48052
