from ai import Ai
import re
from sympy import symbols,sympify
class Converstion:
    def __init__(self):
        ai=Ai()
        self.expr=ai.createExpression()
    def convert(self):
        self.expr=self.expr.replace(" ","")

        P, Q, R=symbols('P Q R')
        symbols_dict= {'P': P, 'Q': Q, 'R': R}
        self.expr=sympify(self.expr,locals=symbols_dict)

        if(self.expr.subs({P: False, Q: False, R: False})and
        self.expr.subs({P: False, Q: False, R: True})and
        self.expr.subs({P: False, Q:True , R: False})and
        self.expr.subs({P: False, Q: True, R: True})and
        self.expr.subs({P: True, Q: False, R: False}) and
        self.expr.subs({P: True, Q: False, R: True}) and
        self.expr.subs({P: True, Q: True, R: False}) and
        self.expr.subs({P: True, Q: True, R: True})):
            print("Its a tautology!!!\n")
        else:
            print("Its  not a tautology\n")
obj=Converstion()
obj.convert()





