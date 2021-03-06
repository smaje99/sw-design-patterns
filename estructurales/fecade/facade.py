from estructurales.fecade.concrete_module import Gold, Black, Silver


class CreditMarket:
    def __init__(self):
        self.gold = Gold()
        self.silver = Silver()
        self.black = Black()
        
    def show_credit_gold(self):
        self.gold.show_credit()
        
    def show_credit_silver(self):
        self.silver.show_credit()

    def show_credit_black(self):
        self.black.show_credit()
