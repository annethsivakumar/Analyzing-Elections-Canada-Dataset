"""
CISC-121 2023W
Name: Anneth Sivakumar 
Student Number: 20320973
Email: 21as221@queensu.ca
Date: 2023-03-07
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity.
"""

def read_data():
  """
  This function is used to convert csv files into a list of dictionaries.
  Parameters: None.
  Returns: list - a list of dictionaries.
  """
  infile = open("electionsData.csv", "r")
  # Get the column headers.
  headers = infile.readline().strip().split(",")
  # Create the list of dictionaries.
  election_records = []
  for line in infile:
    # Split each line into a list of values.
    values = line.strip().split(",")
    # Create a dictionary with the column headers as keys and the values as values.
    record = {}
    for i in range(len(headers)):
      record[headers[i]] = values[i]
    # Add the dictionary to the list.
    election_records.append(record)
  # Close the file.
  infile.close()
  return election_records


def displayInfo(district_num):
  """
  This function is used to print the information given an electoral district number.
  Parameters: district_num - an integer representing the electoral district number.
              lst - a list of dictionary.
  Returns: None.
  """
  # Create list of dictionaries to tranverse.
  lst = read_data()
  # Go through each dictionary in the list.
  for data in range(len(lst)):
    # If electoral district number found, print its information.
    # Otherwise print nothing.
    if (lst[data]["Electoral District Number"] == str(district_num)):
      print("Polling Stations:", lst[data]["Polling Stations"] + ", " +
            "Valid Ballots:", lst[data]["Valid Ballots"] + ", " +
            "Total Ballots Cast:", lst[data]["Total Ballots Cast"] + ", " +
            "Voter Turnout:", lst[data]["Percentage of Voter Turnout"] + "%")
      return
  print("ERROR: DISTRICT NUMBER NOT FOUND!")


def uniqueDistricts(province):
  """
  This function is used to return a list of the names of the electoral districts in a given province.
  Parameters: province - a string representing the province of election.
  Returns: list - a list of electoral district names.
  """
  # Create list of dictionaries to tranverse.
  lst = read_data()
  # Create an empty list to store electoral districts.
  districtlst = []
  # Go through each dictionary in the list.
  for data in range(len(lst)):
    # If province found, append electoral district name into empty list.
    if (lst[data]["Province"] == province):
      districtlst.append(lst[data]["Electoral District Name"])
  # If invalid province or territory is entered, return error message.
  if len(districtlst) == 0:
    return "ERROR: INVALID PROVINCE/TERRITORY!" + "\n" + "PLEASE CHECK SPELLING AND/OR CAPITALIZATION!"
  # Else return list.
  else:
    return districtlst


def findMax(search_key):
  """
  This function is used to return the maximum supplied key value.
  Parameters: search_key - a string representing the key value.
  Returns: integer - the max number in given key value.
           string - the location of the max number.
  """
  # Create list of dictionaries to tranverse.
  lst = read_data()
  # Check if search_key was a valid input for the function.
  if (search_key == "Electors" or
     search_key == "Population" or
     search_key == "Polling Stations" or
     search_key == "Valid Ballots" or
     search_key == "Rejected Ballots" or
     search_key == "Total Ballots Cast"):
    # Create a variable to track maximum number.
    max_num = 0
    # Go through each dictionary in list.
    for data in range(len(lst)):
      # If value of key is greater than max_num, set value to new max_num.
      if (int(lst[data][search_key]) > max_num):
        max_num = int(lst[data][search_key])
        # Create a max_location variable to keep track of Electoral District Name for the max_num.
        max_location = lst[data]["Electoral District Name"]
    return max_num, max_location
  # Return error if invalid search_key is entered.
  else:
    return -1, "ERROR:INVALID SUPPLIED KEY!"


def findMin(search_key):
  """
  This function is used to return the minimum supplied key value.
  Parameters: search_key - a string representing the key value.
  Returns: integer - the min number in given key value.
           string - the location of the max number.
  """
  # Create list of dictionaries to tranverse.
  lst = read_data()
  # Check if search_key was a valid input for the function.
  if (search_key == "Electors" or
      search_key == "Population" or
      search_key == "Polling Stations" or
      search_key == "Valid Ballots" or
      search_key == "Rejected Ballots" or
      search_key == "Total Ballots Cast"):
    # Create a variable to track minimum number.
    min_num = findMax(search_key)[0]
    # Go through each dictionary in list.
    for data in range(len(lst)):
      # If value of key is less than min_num, set value to new min_num.
      if (int(lst[data][search_key]) < min_num):
        min_num = int(lst[data][search_key])
        # Create a max_location variable to keep track of Electoral District Name for the min_num.
        max_location = lst[data]["Electoral District Name"]
    return min_num, max_location
  # Return error if invalid search_key is entered.
  else:
    return -1, "ERROR:INVALID SUPPLIED KEY!"


def totalVotes(lst):
  """
  This function is used to return a list of dictionaries which consists of the total number of ballots cast in every
  Canadian province and territory.
  Parameters: lst - a list of dictionaries.
  Returns: list - a list of dictionaries.
  """
  # Create an empty list for the new list of dictionaries.
  list_of_dicts = []
  # Create an empty dictionary for storing all province and total ballots cast.
  dict = {}
  # Go through each dictionary.
  for data in range(len(lst)):
    # Get each province and total ballot cast.
    each_province = lst[data]["Province"]
    total_ballots_cast = lst[data]["Total Ballots Cast"]
    # Create key and value if province does not exist in dictionary.
    if each_province not in dict:
      dict[each_province] = int(total_ballots_cast)
    # Otherwise, add the other total_ballots_cast to the province.
    else:
      dict[each_province] += int(total_ballots_cast)
  # Split each key and value into seperate dictionaries.
  for key, value in dict.items():
    new_dict = {key: value}
    # Append the dictionary to the list.
    list_of_dicts.append(new_dict)
  # Sort the list of dictionaries in ascending order based on the keys
  # Simple selection sort
  for i in range(len(list_of_dicts)):
    min_index = i
    for j in range(i + 1, len(list_of_dicts)):
      if list(list_of_dicts[j].keys())[0] < list(list_of_dicts[min_index].keys())[0]:
        min_index = j
    list_of_dicts[i], list_of_dicts[min_index] = list_of_dicts[min_index], list_of_dicts[i]
  return list_of_dicts


def selectionSort(key, lst):
  """
  This function is used to sort the supplied list of dictionaries into increasing order based on the specified key.
  Parameters: key - specified column to sort by.
              lst - a list of dictionaries.
  Return: list - a list of dictionaries. 
  """
  try:
    # Go through all elements.
    for i in range(len(lst)):
      # Find the minimum element in remaining.
      current_index = i
      for j in range(i + 1, len(lst)):
        if lst[current_index][key] > lst[j][key]:
          current_index = j
      # Swap items.
      lst[i], lst[current_index] = lst[current_index], lst[i]
    return lst
  except:
    # Return error if invalid key is entered.
    return "ERROR: INVALID SUPPLIED KEY!" + "\n" + "PLEASE ENTER ONE OF THE FOLLOWING:" + "\n" + \
           "{Province, Electoral District Name, Electoral District Number, Electors, Population, Polling Stations, " \
           "Valid Ballots, Percentage of Valid Ballots, Rejected Ballots, Percentage of Rejected Ballots," \
           "Total Ballots Cast, Percentage of Voter Turnout}"


def binarySearch(district_num):
  """
  This function is used to search for an electoral district based on its electoral district number and returns the
  percentage of voter turnout in that district.
  Parameters: district_num - an integer representing.
  Return: integer - percentage of voter turnout in that district.
  """
  # Create list of dictionaries.
  lst = read_data()
  # Create list of dictionaries that has been sorted by electoral district number.
  new_lst = selectionSort("Electoral District Number", lst)
  start = 0
  end = len(new_lst) - 1
  while start <= end:
    mid = (start + end) // 2
    # If element is present at the middle itself.
    if int(new_lst[mid]["Electoral District Number"]) == district_num:
      return new_lst[mid]["Percentage of Voter Turnout"]
    # If element is smaller than mid, then it can only be present in left of array.
    elif district_num < int(new_lst[mid]["Electoral District Number"]):
      end = mid - 1
    # Else the element can only be present in right subarray.
    else:
      start = mid + 1
  return None