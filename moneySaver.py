import colorama
from colorama import Fore, Style

# Define a color palette
palette = {
  "red": Fore.RED,
  "yellow": Fore.YELLOW,
  "green": Fore.GREEN,
  "reset": Style.RESET_ALL
}

Tool = """ 
                                     __                          
  /\/\    ___   _ __    ___  _   _  / _\  __ _ __   __ ___  _ __ 
 /    \  / _ \ | '_ \  / _ \| | | | \ \  / _` |\ \ / // _ \| '__|
/ /\/\ \| (_) || | | ||  __/| |_| | _\ \| (_| | \ V /|  __/| |   
\/    \/ \___/ |_| |_| \___| \__, | \__/ \__,_|  \_/  \___||_|   
                             |___/              Creator: Greaser                      

        """

print(Tool)


def calculate_savings(salary):
  savings = salary * 0.1
  print(palette["green"] + "Based on your salary, you should save: $" + str(savings))
  print(palette["reset"])

# Used a while loop to keep asking for a salary until the user enters a valid number
while True:
  try:
    salary = float(input(palette["yellow"] + "Please enter your salary: $"))
    print(palette["reset"])
    calculate_savings(salary)
    break
  except ValueError:
    print(palette["red"] + "Invalid input. Please enter a valid number.")
    print(palette["reset"])
