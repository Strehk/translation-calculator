STANDARD_LINE = 60
PRICE_PER_LINE = 0.30
SURCHARGE = 15.00
STANDARD_PAGE = 30


class base_values(object):
    def __init__(self, price_per_line, surcharge, standard_line, standard_page) -> None:
        self.base_price_per_line = price_per_line
        self.express_surcharge = surcharge
        self.standard_line = standard_line
        self.standard_page = standard_page

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        self.__dict__.update(state)
