"""
CISC-121 2023W
Name: Anneth Sivakumar 
Student Number: 20320973
Email: 21as221@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""
import functions3

def main():
  """
  This function implements the interface for the program.
  Parameters: None.
  Return: None.
  """
  # Read .csv file and create list of dictionaries.
  election_records = functions3.read_data()
  # Create a boolean variable to keep track of when to end the program.
  run_function = True
  # Keep asking user to input a number from menu.
  while (run_function == True):
    # Display title and menu.
    print("-----------------------------------")
    print("Canadian Elections Analysis Tool")
    print("-----------------------------------")
    print("-----------------------------------")
    print("MENU:")
    print("1. Display information for an electoral district")
    print("2. Show unique districts by the given province/territory")
    print("3. Find Maximum value among a header")
    print("4. Find Minimum value among a header")
    print("5. Find total number of ballots cast in every Canadian province/territory")
    print("6. Selection Sort by a given header")
    print("7. Binary Search by electoral district number, to find percentage of voter turnout in that district")
    print("8. Quit" + "\n")
    print("Valid Keys for option 3/4: "
          "{Electors, Population, Polling Stations, Valid Ballots, Rejected Ballots, Total Ballots Cast}")
    print("-----------------------------------")
    # Ask user to choose one menu option
    option = input("Please choose an option from 1-8: ")
    # Execute chosen menu option
    if(option == "1"):
      try:
        print("Option Chosen: 1")
        district_num = int(input("Please enter electoral district number: "))
        print()
        functions3.displayInfo(district_num)
        print("\n" + "\n")
      except ValueError:
        print("ERROR: MUST ENTER INTEGER!")
        print("\n" + "\n")
    elif(option == "2"):
      print("Option Chosen: 2")
      province = input("Please enter a province or territory: ")
      print()
      print(functions3.uniqueDistricts(province))
      print("\n" + "\n")
    elif(option == "3"):
      print("Option Chosen: 3")
      key = input("Please enter one of the supplied keys: ")
      print()
      print("Max " + str(key) + ": " + str(functions3.findMax(key)[1]) + " " + str(functions3.findMax(key)[0]))
      print("\n" + "\n")
    elif(option == "4"):
      print("Option Chosen: 4")
      key = input("Please enter one of the supplied keys: ")
      print()
      print("Min " + str(key) + ": " + str(functions3.findMin(key)[1]) + " " + str(functions3.findMin(key)[0]))
      print("\n" + "\n")
    elif(option == "5"):
      print("Option Chosen: 5")
      print()
      data = functions3.totalVotes(election_records)
      print("Total Votes:")
      for i in data:
        key = list(i.keys())[0]
        value = i[key]
        print(str(key) + ": " + str(value))
      print("\n" + "\n")
    elif(option == "6"):
      print("Option Chosen: 6")
      key = input("Please enter one of the supplied keys: ")
      print()
      print("Sorted by " + str(key))
      print(functions3.selectionSort(key, election_records))
      print("\n" + "\n")
    elif(option == "7"):
      print("Option Chosen: 7")
      try:
        district_num = int(input("Please enter electoral district number: "))
        print()
        if functions3.binarySearch(district_num) == None:
          print("Item Was Not Found")
        else:
          print("Found: " + str(functions3.binarySearch(district_num)) + "%")
        print("\n" + "\n")
      except ValueError:
        print("ERROR: MUST ENTER INTEGER!")
        print("\n" + "\n")
    elif(option == "8"):
      print("Option Chosen: 8")
      print("Ending program...")
      run_function = False
    else:
      print("ERROR: INVALID NUMBER CHOSEN!")
      print("PLEASE CHOOSE A NUMBER BETWEEN 1-8")
      print("\n" + "\n")
      

main()
