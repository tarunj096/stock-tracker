

import pandas as pd
import pandas_datareader as pdr 
from time import sleep

companies = "SBUX NKE DMART.NS RELIANCE.NS GOOG 532648.BO".split()
menu= " Track List, Show List, Add to List, Edit List, Add New List, Quit".split(",")
    
def show_list(companies):
    companies.sort()
    return companies

def add_list(companies):
    print("Enter the Code/Symbol of the Company")
    company=input().upper()
    while company!='':
        companies.append(company)
        company = input("Enter symbol to add: Hit ENTER to quit:")

def edit(companies):
    print("Select Symbol/Code of the company to delete:")
    for i in range(1, len(companies)+1):
        print("{} - {}".format(i, companies[i-1]))
    delete = companies.pop(int(input())-1)
    print("{} removed/deleted.".format(delete))    

def add_new_list():
    new=[]
    print("Enter Symbol/Code to add:")
    company = input().upper()
    while company!='':
        new.append(company)
        company=input("Enter Symbol/Code to add or tap ENTER to quit:")
    while True:
        print(prices(new))
        print("CONTROL+C to exit.")


def prices(companies):
    companies.sort()
    return pdr.get_quote_yahoo(companies)['price']

    
def main():
    r_prog=True
    while r_prog:
        print("Choose your Option:")
        for i in range(1, len(menu)+1):
            print("{} - {}".format(i, menu[i-1]))
        choice = int(input())
        if choice == 1:
            while True:
                print("")  
                print(prices(companies))
                print("")
                print("Type CONTROL+C to quit.")
            sleep(2)
        elif choice== 2:
            print(show_list(companies))
            
        elif choice == 3:
           add_list(companies)
            
        elif choice == 4:
            edit(companies)
        
        elif choice == 5:
            add_new_list()
            
        elif choice == 6:
            r_prog = False

        

if __name__=="__main__":        
    main()

