# dH 5/14/2023
# Mar2023Midterm.py
print("Final Program, Minh Nguyen 0920131")

#########################################

import datetime

class Animal:
    def __init__(self, species, name, age, birth_season, color, gender, weight, origin):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.gender = gender
        self.weight = weight
        self.origin = origin
        self.arrival_date = datetime.date.today()

        self.generate_id()

    def generate_id(self):
        if self.species == "hyena":
            prefix = "Hy"
        elif self.species == "lion":
            prefix = "Li"
        elif self.species == "tiger":
            prefix = "Ti"
        elif self.species == "bear":
            prefix = "Be"
        else:
            prefix = "Un"

        id_num = len(animals[self.species]) + 1
        self.id = f"{prefix}{id_num:02d}"

    def get_birth_date(self):
        if self.birth_season == "spring":
            birth_month = 3
        elif self.birth_season == "fall":
            birth_month = 9
        elif self.birth_season == "winter":
            birth_month = 12
        else:
            birth_month = 6

        birth_year = datetime.date.today().year - self.age
        return datetime.date(birth_year, birth_month, 21)

    def __str__(self):
        birth_date = self.get_birth_date().strftime("%Y-%m-%d")
        arrival_date = self.arrival_date.strftime("%Y-%m-%d")
        return f"{self.id}; {self.name}; {self.age} years old; birth date {birth_date}; {self.color} color; {self.gender}; {self.weight} pounds; from {self.origin}; arrived {arrival_date}"

# Define animals list with empty dictionaries for each species
animals = {
    "hyena": [],
    "lion": [],
    "tiger": [],
    "bear": [],
}
#########################################
# Get animal names into four lists...

# Open animalNames.txt
# Open the input file
my_file = open("E:/myFinal/pythonfinalprogramspr23-Minhnguyen253/animalNames.txt", "r", encoding="utf-8")

# Read the file line by line into a data structure called 'Lines_names'
Lines_names = my_file.readlines()

# Close the input file (if you open a file, be sure to close it)
my_file.close()

# Output each line in Lines
line_count = 0;
for line in Lines_names:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1

# Read the file into a Python list
list_of_lines = []
for line in Lines_names:
    list_of_lines.append(line)

# Demonstrate the list
print("\n\n Here is a list of the lines in the animal names file...\n\n")
print("line 0 is: " + str(list_of_lines[0]))

hyena_names_list = list_of_lines[2].replace(',',"").split()
lion_names_list = list_of_lines[6].replace(',',"").split()
tigers_names_list = list_of_lines[10].replace(',',"").split()
bears_names_list = list_of_lines[14].replace(',',"").split()
# end of getting animal names
###################################################

################ User-defined Functions #########################
# the birthday function
def the_birthday_function(years_old, season_of_birth):
    birth_year = 2023 - int(years_old.strip())
    birth_year = birth_year - 1

    if season_of_birth == "spring":
        birthday_date = "03-21"
    elif season_of_birth == "summer":
        birthday_date = "06-21"
    elif season_of_birth == "fall":
        birthday_date = "09-21"
    elif season_of_birth == "winter":
        birthday_date = "12-21"
    else:
        birthday_date = "01-01"

    animal_birthday = str(birth_year) + "-" + birthday_date

    return animal_birthday

# uniqueID function
def uniqueID(species_name, num_of_animals_in_species):
    match species_name:
        case "hyena":
            prefix = "Hy"
        case "lion":
            prefix = "Li"
        case "tiger":
            prefix = "Ti"
        case "bear":
            prefix = "Be"
        case default:
            prefix = "Xx"

    return prefix + "0" + str(num_of_animals_in_species)
##################################################################

# Global variables needed for some user-defined functions
num_of_hyenas = 0
num_of_lions = 0
num_of_tigers = 0
num_of_bears = 0

# Global lists needed for organizing animals into a single-species habitats
hyena_list = []
lion_list = []
tiger_list = []
bear_list = []

print("\n\n Welcome to Minh's Digital Zoo \n\n")

#################### Input File IO ###########################################
# Open the input file
# You can use with when creating a file object as well, this syntax was easier for me
my_file = open("E:/myFinal/pythonfinalprogramspr23-Minhnguyen253/arrivingAnimals.txt", "r", encoding="utf-8")

# Read the file line by line into a data structure called 'Lines'
Lines = my_file.readlines()

# Close the input file (if you open a file, be sure to close it)
my_file.close()

# Output each line in Lines
line_count = 0;
for line in Lines:
    print("Line " + str(line_count+1) + ":  " + line)
    line_count += 1

# Read the file into a Python list
list_of_lines = []
for line in Lines:
    list_of_lines.append(line)

# Demonstrate the list
print("\n\n Here is a list of the lines in the text file...\n\n")
print("line 0 is: " + str(list_of_lines[0]))


# Get the file contents into an array
# Talk about the difference between list and array
my_array = np.asarray(list_of_lines)

# Find how many elements are in our new array
num_of_array_elements = my_array.size

# Output the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))
    array_line += 1

# Process each element of the new array
array_line = 0
for element in my_array:
    print("\n" + str(my_array[array_line]))

    # get the data elements needed from this one line for the birthday
    #
    ########################## Split on blank space to get words in the line
    split_on_space = my_array[array_line].split(" ")
    print(split_on_space)

    years_old = split_on_space[0]
    print("years_old: " + years_old)

    # next is sex, which will always be the fourth word (element number 3 because list element numbering starts at 0)
    sex = split_on_space[3]
    print("sex: " + sex)

    # we can get species here
    species = split_on_space[4]
    print("species: " + species)

    # we have a comma at the end of this word, so we must remove it
    species = re.sub(",", "", species)

    # test with a print()
    print(" species without a comma: " + species)

    # season of birth
    season = split_on_space[7]
    print("season: " + season)

    # we have a comma at the end of this word, so we must remove it
    season = re.sub(",","",season)

    # test with a print()
    print(" season without a comma: " + season)

    # we got a couple of our needed data elements. now let's calculate what we can using the functions we wrote
    birth_date = the_birthday_function(years_old, season)
    print("birthdate: " + birth_date)

    # generate a uniqueID and get a name!
    if (species == "hyena"):
        num_of_hyenas += 1
        unique_id = uniqueID(species, num_of_hyenas)
        name = hyena_names_list[num_of_hyenas]
    elif (species == "lion"):
        num_of_lions += 1
        unique_id = uniqueID(species, num_of_lions)
        name = lion_names_list[num_of_lions]
    elif (species == "tiger"):
        num_of_tigers += 1
        unique_id = uniqueID(species, num_of_tigers)
        name = tigers_names_list[num_of_tigers]
    elif (species == "bear"):
        num_of_bears += 1
        unique_id = uniqueID(species, num_of_bears)
        name = bears_names_list[num_of_bears]
    else:
        print("\n error in incrementing species")

    print("unique_id: " + unique_id)
    print("name is: " + name)
    ##########################################

    ##################### Split on comma because some data elements (like color, wright, and origin)
    ########################### have a varied number of words
    after_split_on_comma =  my_array[array_line].split(", ")

    print(after_split_on_comma)

    color = after_split_on_comma[2]
    print("color = " + color)

    weight = after_split_on_comma[3]
    print("weight is: " + weight)

    origin = after_split_on_comma[4] + " " + after_split_on_comma[5]
    print("origin = " + origin)

    origin = origin.strip()

    split_on_dash = birth_date.split("-")
    my_year = split_on_dash[0]
    my_month = split_on_dash[1]
    my_day = split_on_dash[2]

    # test our split()
    print("my_year = " + my_year)
    print("my_month = " + my_month)
    print("my_day = " + my_day)

    # cast strings to ints because that's what our date object needs
    birth_date_object = date(int(my_year), int(my_month), int(my_day))

    # pass our new date object to our calc_age_in_years() function
    animal_age_in_years = calc_age_in_years(birth_date_object)

    # validate our function
    print("animal_age_in_years is: " + str(animal_age_in_years))

    # arrival date is easy (after all that date() processing!
    arrival_date = date.today()
    print("arrival_date = " + str(arrival_date))

    # That should be it. Let's see....
    str01 = unique_id + "; " + name + "; " + str(animal_age_in_years) + " years old; " + "birth date: " + birth_date + "; "
    str02 = color + "; " + sex + "; " + weight + "; " + origin + "; arrived: " + str(arrival_date)

    output_line = str01 + str02

    print("\noutput_line = " + output_line)

    # get this output line into the proper list()
    if (species == "hyena"):
        hyena_list.append(output_line)
    elif (species == "tiger"):
        tiger_list.append(output_line)
    elif (species == "lion"):
        lion_list.append(output_line)
    else:
        bear_list.append(output_line)

    array_line += 1
    ############################################### End of processing each line with the two splits()
    # Write our species list to our output file.

    print("Hyena Habitat: \n\n")
    for line in hyena_list:
      print(line + "\n")

    my_file = open("E:/myFinal/pythonfinalprogramspr23-Minhnguyen253/FinalOutput.txt", "w", encoding="utf-8")

    my_file.write("Final Program Output: Minh Nguyen, Spring 2023, Fresno, CA\n\n")

    my_file.write("Hyena Habitat: \n\n")
    for i in hyena_list:
      my_file.write(i)
      my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Lion Habitat: \n\n")
    for i in lion_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Tiger Habitat: \n\n")
    for i in tiger_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.write("Bear Habitat: \n\n")
    for i in bear_list:
        my_file.write(i)
        my_file.write("\n")
    my_file.write("\n\n")

    my_file.close()
