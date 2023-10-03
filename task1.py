from simpleai.search import CspProblem, backtrack
import streamlit as st

# Set the title of your app
st.title("AI task 1 by Michiel Van Loy")

# Get user input and store it in a tuple
input1 = tuple(st.text_input("First word: ").upper())
input2 = tuple(st.text_input("Second word: ").upper())
input3 = tuple(st.text_input("Third word: ").upper())


# Removes all the duplicates in the tuple by looping though the tuple en returning a unique list
def remove_duplicates(variables):
    unique_variables = []
    for letter in variables:
        if letter not in unique_variables:
            # Adds the unique letters to a list
            unique_variables.append(letter)
    return unique_variables



# Function that returns the list of the index of each letter in de list of letters (unique_variables)
def letter_positions_in_order(word, unique_variables):
    # Create a list to store the letter positions
    letter_positions = []
    
    # Iterate through the letters of the word and assign positions based on the order
    for letter in word:
        if letter in unique_variables:
            # Adds index position to the return list
            letter_positions.append(unique_variables.index(letter))
    
    return letter_positions



# Generates the right domain for each letter in the tuple
def generate_domains(unique_variables, input1, input2, input3):
    domain_dict = {}
    for letter in unique_variables:
        # If the letter is in the beginning of a word it can't be 0
        if letter == input1[0] or letter == input2[0] or letter == input3[0]:
            domain_dict[letter] = list(range(1, 10))
        else:
            domain_dict[letter] = list(range(0, 10))
    return domain_dict

def constraint_unique(variables, values):
    return len(values) == len(set(values))  # Remove repeated values and count

def constraint_add(variables, values):
    word1=""
    word2=""
    result=""
    # Loop trough the positionlist of each word to add the right value
    for i in range(0,len(result1)):
        word1 = word1 + str(values[result1[i]])
    for j in range(len(result2)):
        word2 = word2 + str(values[result2[j]])
    for k in range(len(result3)):
        result = result + str(values[result3[k]])
        
    # Place the string in an INT variable to check if the sum is correct
    word1int=int(word1)
    word2int=int(word2)
    resultint=int(result)
    
    return (word1int + word2int) == resultint



button = st.button("Test words")

if button and input3:
    # Make 1 tuple with all letters
    variables = input1+input2+input3

    # Remove all the duplicated by calling the fuction I made earlier
    unique_variables = remove_duplicates(variables)
    
    # Calls the above function "letter_positions_in_order" to
    result1 = letter_positions_in_order(input1, unique_variables)
    result2 = letter_positions_in_order(input2, unique_variables)
    result3 = letter_positions_in_order(input3, unique_variables)

    # Call the function to generate the domains
    domains = generate_domains(unique_variables, input1, input2, input3)
    
    # Make the contraint
    constraints = [
        (unique_variables, constraint_unique),
        (unique_variables, constraint_add),
    ]

    if input3:
        # Print the sum
        print_input1 = ''.join(input1)
        st.markdown(f'<pre>{"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + print_input1}</pre>', unsafe_allow_html=True)
        st.text("+ "+''.join(input2))
        st.text("------")
        print_input3 = ''.join(input3)
        st.markdown(f'<pre>{"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + print_input3}</pre>', unsafe_allow_html=True)

    problem = CspProblem(unique_variables, domains, constraints)

    output = backtrack(problem)
    if input3:
        if output:
            st.write("Solution: "+str(output))
        else:
            st.text("No possible solution")

    # Define the input string
    input_string = ''.join(input1)+" "+''.join(input2)+" "+''.join(input3)

    # Split the input string into words
    words = input_string.split()

    # Initialize three variables to store the values
    variable1_value = ''
    variable2_value = ''
    variable3_value = ''

    # If there is a solution
    if output:
        # Iterate through the words and get their values from the dictionary
        for i, word in enumerate(words):
            for letter in word:
                variable_value = output.get(letter, letter)
                if i == 0:
                    variable1_value += str(variable_value)
                elif i == 1:
                    variable2_value += str(variable_value)
                elif i == 2:
                    variable3_value += str(variable_value)
            
        # Print the solution
        st.markdown(f'<pre>{"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + variable1_value}</pre>', unsafe_allow_html=True)
        st.text("+ "+variable2_value)
        st.text("------")
        st.markdown(f'<pre>{"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + variable3_value}</pre>', unsafe_allow_html=True)
