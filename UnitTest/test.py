import re
import unittest






def getString_removeNumeric(myString):
    number=re.findall('[0-9]',myString);
    if number:
        removed_string =''.join(i for i in myString if not i.isdigit());
    else:
        removed_string = myString;
    
    return removed_string

def menu(choice,myString):
    if choice == 1:
        y = getString_removeNumeric(myString);
        U = y.upper()
        return U
    if choice == 2:
        x = getString_removeNumeric(myString);
        L = x.lower()
        return L
    
def test_sum():
    assert menu(2,"ABCD123")  == "abd", "Should be abcd"
    

if __name__ == "__main__":
    print("Enter a string");
    myString=input()     
    print("select what you want to do");
    print("1.Convert to Upper case");
    print("2.convert to Lower case");
    z = int(input())
    print(menu(z,myString))
    test_sum()
    print("Test passed")
