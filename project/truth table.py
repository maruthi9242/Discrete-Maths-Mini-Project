from ai import *
from Evaluation import Converstion
class truth_table:

    def print_truth_table(self):
        ans=Converstion().convert()
        print("----------------------------------------------------\n")
        print("    Truth Table\n")
        print("P  |    Q  |    R  | output")
        print("______________________________")
        print("\n0  |   0   |  0    | "+str(ans[0]))
        print("\n0  |   0   |  1    | "+str(ans[1]))
        print("\n0  |   1   |  0    | "+str(ans[2]))
        print("\n0  |   1   |  1    | "+str(ans[3]))

        print("\n1  |   0   |  0    | "+str(ans[4]))
        print("\n1  |   0   |  1    | "+str(ans[5]))
        print("\n1  |   1   |  0    | "+str(ans[6]))
        print("\n1  |   1   |  1    | "+str(ans[7]))

        counter=0;
        for i in ans:
            if(i==True):
                counter=counter+1
        print("\n----------------------------------------------------\n")
        if(counter==0):
            print("\nType: Contradiction\n "
                  "Reason: The expression evaluates to false for all possible combinations of truth values.\n")
        elif(counter>=1 and counter<8):
            print("\nType: Satisfiable\n"
                  "Reason: The expression evaluates to both true and false for different inputs.\n")
        else:
            print("\nType: Tautology \n"
                  "Reason: The expression evaluates to true for all possible combinations of truth values.\n")



truth_table().print_truth_table()