class bot():
    def __init__(self,bot_cash,bot_actions,name):
        self.bot_cash=bot_cash
        self.bot_actions=bot_actions
        self.name=name
        self.timer=0
    
    def play(self):
        global cena
        if cena<=7:
            cena*=0.8
            possible_actions=self.bot_cash/cena
            possible_actions=int(possible_actions) 
            price=possible_actions*cena
            self.bot_cash-=price
            self.bot_actions+=possible_actions
        
        elif cena>=17:
            possible_price=self.bot_actions*cena
            self.bot_cash+=possible_price
            impediment=possible_price*0.1
            self.bot_cash-=impediment
            self.bot_actions=0
        
        else:
            pass
    
    def hello(self):
        print(f'hello! Nazywam się {self.name} i jestem niezależnym inwestorem!')
        pass
    
    def tax_bot(self):
        self.timer+=1
        if self.timer>=10:
            tax=self.bot_cash*0.3
            self.bot_cash-=tax
            self.timer=0