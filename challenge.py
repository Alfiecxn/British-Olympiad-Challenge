import math

ruleset=str(input("""Please input your ruleset starting with x, it should be the same length as the password and in the following format.
             \n\nx means any digit is acceptable in its place\nu means it must be higher than the last one\nd means it must be lower than the last one
             \nIf the password was 5 digits long, the rule input could be xxddu\n\n>>> """))
input_password=str(input("\nNumerical Password (0-9 only)\n>>> "))

split_pass=[]
split_rules=[]
qmarklist=[]
positionbeforelist=[]
filtered_ruleset=[]
elements_removed=0

for i in input_password:
    split_pass.append(i)
print("Split_Pass list created : ", split_pass)
for i in ruleset:
    split_rules.append(i)
    filtered_ruleset.append(i)
print("Split_rules list created : ", split_rules)
for i in range (len(split_rules)):
    if split_rules[i]=='?':
        qmarklist.append(i)
print("Found Questionmark Indexes and created qmarklist : ", qmarklist)

for i in qmarklist:
    positionbeforelist.append(i-1)
print("created positionbeforelist : ", positionbeforelist)
final_position_list = positionbeforelist+qmarklist
print("created final_position_list : ", final_position_list)
final_position_list.sort(reverse=True)
print("sorted final_position_list into descending order : ", final_position_list)
for i in qmarklist: # <-- purify the splitrules list whilst keeping the 'questionmarked' ruletypes
    split_rules.pop(i)
print("purged any qmarks in split_rules for clean usage [compare() does not hold a ? handler] : ", split_rules)
##
##

## the bracketed parts need to be already-combined and ready to remove before the next function runs
##
for i in final_position_list:
    elements_removed=elements_removed+1
    filtered_ruleset.pop(i)
print("removed qmarks and 'qmarked' from filtered_ruleset : ", filtered_ruleset)

#for i in range (elements_removed):
#    filtered_ruleset.append('x')
#print(filtered_ruleset)
#An alternative solution to the new checklist length not matching the password length.

def compare(list_position, list):
    error2='error2'
    error='error'
    ruletype=list[list_position]

    if ruletype=='s': #creating a skippable fill-in so that i can replace lost array length with skippable elements, there could potentially be a more efficient way but this will allow me to keep my lists at their intended lengths reagardless of bracket format
        pass

    elif ruletype=='(' and (len(ruletype)==1):
        if list[list_position+1]==')':
            print("Brackets can't be empty")
            exit()
        try:    
            closerbracket=list.index(')')
        except ValueError:
            print("You opened brackets and didn't close them")
            exit("Ruleset Invalid: Opened Brackets without closing them")
    
        try:
            list.index('?',list_position,closerbracket)==ValueError
            pass
        except ValueError:
            pass
        else:
            print("Can't have ? between brackets")
            exit("Can't have ? between brackets")

        try:
            list.index('*',list_position,closerbracket)==ValueError
            pass
        except ValueError:
            pass
        else:
            print("Can't have * between brackets")
            exit("Can't have * between brackets")

        list[list_position : closerbracket+1] = [''.join(list[list_position : closerbracket+1])] #using list slicing and joining to combine bracketed elements to all be stored under the same list index
        #takes away 1+inneramount from the list
        difference=closerbracket-list_position
        for i in range (difference):
            list.append('s')
        print(list)

    elif ruletype=='x':
        pass

    elif ruletype=='u':

        if split_pass[list_position] > split_pass[list_position-1]:
            pass

        else:
            return error2

    elif ruletype=='d':

        if split_pass[list_position] < split_pass[list_position-1]:
            pass

        else:
            return error
        
    elif str(ruletype).startswith('('):
        print("Found start with (")
        breakdownlist=[]
        currentstring=list[list_position]
        for i in currentstring:
            breakdownlist.append(i)
            print(breakdownlist)
        breakdownlist.remove('(')
        breakdownlist.remove(')')
        print(breakdownlist)
        list.remove(currentstring)
        list.append('s')
        if list==split_rules:       
            for i in breakdownlist:
                list.insert(list_position, i) ## insert the broken down list into the unfiltered list
            print(list)
    else:
        print(ruletype)


if split_rules[0]=='u' or split_rules[0]=='d' or split_rules[0]=='?':
    print("Your ruleset cannot start with u, d, or ? ")
    exit()

for i in range (len(split_rules)):
    x=compare(i, split_rules)
    if x=='error' or x=='error2':
        break

if x=='error' or x=='error2':
    print("Error with first list")
    print("Password Invalid")
    for i in range (len(filtered_ruleset)):
        y=compare(i,filtered_ruleset)
    if y=='error' or y=='error2':
        print("Error with second list")
        print("Password Invalid")
    else:
        print("Passed on second list")
else:
    print("Passed on first list")
    

    

