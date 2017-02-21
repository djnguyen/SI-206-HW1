import operator

# SI 206 Winter 2017
# Homework 1 - Code
# Name: David Nguyen

##COMMENT YOUR CODE WITH:
# Section Day/Time: Thursdays 3-4 PM
# People you worked with: 

#########

# For each task, fill in the code for the function we describe.

## Our provided code will call the functions with a few different inputs, check the results, and print 'OK' when each function's output is correct.

## The starter code for each function includes a placeholder for your code. You need to fill in code for the function that returns the correct result as specified.

## Task A. String manipulation (function 'string_manip')
##   This function accepts any string as input. It should return a string that is manipulated in a variety of ways:
##   First, remove any leading and trailing spaces from the input string.
##   Convert the input string to upper case.
##   Replace any remaining spaces in the string with the pound sign '#'.
##   Remove any occurrences of the string "UMSI" from the string.
##   If the remaining string is a single character just return that string.
##  Otherwise, return the string in reverse.

def string_manip(s):
    string = s
    remove_spaces = string.split()
    convert_to_string = ' '.join(remove_spaces)
    convert_to_upper = convert_to_string.upper()

    new_string = convert_to_upper

    add_pound = new_string.replace(' ', "#")

    new_string_2 = add_pound

    remove_UMSI = new_string_2.replace("UMSI","")

    almost_final_string = remove_UMSI

    final_string = almost_final_string[::-1]

    return final_string

## Task B. Dictionaries and sorting (function 'name_counts')

## The function name_counts takes as input a list of strings. It should return a list of tuples, where each tuple contains a UNIQUE string from the list and the count of that string's occurrences in the list. 
## The list that is returned from your function should be in decreasing order (beginning with a tuple of the word that occurs the most times with its count, and ending with a tuple of the word that occurs the fewest times). In case of ties of counts, break the tie by string value in increasing order, e.g. B comes before C.

## Examples:
## This invocation of name_counts:
##   name_counts(['Becca', 'Catherine', 'Catherine', 'Catherine', 'Christopher', 'Christopher'])
## should return [('Catherine', 3), ('Christopher', 2), ('Becca', 1)]
## This invocation of name_counts:
##   name_counts(['Christopher', 'Mike', 'Becca', 'Christopher', 'Bacon', 'Catherine', 'Christopher', 'Becca'])
## should return [('Christopher', 3), ('Becca', 2), ('Bacon', 1), ('Catherine', 1), ('Mike', 1)])
##

def name_counts(names):
    a_list = []
    record_of_names = []

    for x in names:
        if x in record_of_names:
            pass
        else:
            counter = names.count(x)
            tuple_1 = (x,counter)
            a_list.append(tuple_1)
            record_of_names.append(x)

    a_list = sorted(a_list, key = lambda x: x[0])

    final_list = []
    final_list = sorted(a_list, key = lambda x: x[1], reverse = True)

    return final_list



## TASK C. Iteration and accumulation

## Complete the definition of the function build_acronym. This function should accept a list of strings as input. It should return a string that contains the uppercase versions of the first character of each of the strings in the input list.
## For example, given the list ["Alabama","Cats","Brussels sprouts"], the function should return "ABC".
## Given the list ["thank","goodness","it's","friday"], the function should return "TGIF".

def build_acronym(ls):
    word = ""
    for x in ls:
        word += x[0]
    return word.upper()


## TASK D. Python user-defined types

## Below we've provided a Python class definition representing a house. Add a method to the class called determine_size that returns a string that describes the house's size. If a house's color is "blue", its size should be "big". If a house's color is "red", its size should be "small". Otherwise, its size should be "medium".

class House(object):
    def __init__(self,color,street,number):
        self.house_color = color
        self.street_name = street
        self.address_number = number

    def __str__(self):
        return "This is a {} house, located at {} {}.".format(self.house_color,self.address_number,self.street_name)

    def determine_size(self):
        if self.house_color is "blue":
            return "big"
        elif self.house_color is "red":
            return "small"
        else:
            return "medium"


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected):
  score = 0;
  if got == expected:
    score = 25
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
    total = 0
    print()
    print ('Task A: string manipulation'
    """\nEach OK is worth 25 points.""")
    total += test(string_manip(' Colleen van Lent'), 'TNEL#NAV#NEELLOC')
    total += test(string_manip('  276 876'), '678#672')
    total += test(string_manip('!UMSI!'), '!!')
    total += test(string_manip('UMSI'), '')
    total += test(string_manip(''), '')

    print("\n\n")
    print('Task B: name_counts'
    """ \nEach OK is worth 25 points.""")
    total += test(name_counts([]), [])
    total += test(name_counts(['Christopher']), [('Christopher', 1)])
    total += test(name_counts(['Christopher', 'Christopher', 'Christopher']), [('Christopher', 3)])
    total += test(name_counts(['Eddie', 'Bacon', 'Christopher', 'Christopher', 'Christopher', 'Bacon', 'Bacon']), [('Bacon', 3), ('Christopher', 3), ('Eddie', 1)])
    total += test(name_counts(['Bacon', 'Catherine', 'Eddie', 'Bacon', 'Becca', 'Christopher', 'Bacon', 'Eddie', 'Mike']), [('Bacon', 3), ('Eddie', 2), ('Becca', 1), ('Catherine', 1), ('Christopher', 1), ('Mike', 1)])
    total += test(name_counts(["Cai","Cai","Bette","Ferdinand","Ferdinand","Emmett","Bette","Cai","Bette","Emmett",]),[("Bette",3),("Cai",3),("Emmett",2),("Ferdinand",2)])

    print("\n\n")
    print('Task C: build_acronym'
    """ \nEach OK is worth 25 points.""")
    total += test(build_acronym(["thank","goodness","ice","freezes"]),"TGIF")
    total += test(build_acronym(["pretty","yurts","tumble","hard","on","northerly slopes"]),"PYTHON")
    total += test(build_acronym(["yay"]),"Y")
    total += test(build_acronym([]),"")
    total += test(build_acronym(["Hooray","Ice cream"]),"HI")

    print("\n\n")
    print('Task D: determine_size'
    """ \nEach OK is worth 25 points.""")
    nh = House("blue","State",206)
    nh2 = House("red","Main",506)
    nh3 = House("purple","Liberty",281)
    nh4 = House("brick","Kingsley",110)
    
    total += test(nh.determine_size(),"big")
    total += test(nh2.determine_size(),"small")
    total += test(nh3.determine_size(),"medium")
    total += test(nh4.determine_size(),"medium")

    print("\n\n")
    print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
