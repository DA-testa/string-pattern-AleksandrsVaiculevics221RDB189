# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_name = input()#.rstrip() # after input type choice
    if input_name=="I":# read two lines
        first_input_pattern = input().rstrip()  # first line is pattern 
        second_input_text = input().rstrip() # second line is text in which to look for pattern
        
    elif input_name=="F":
        file_num = input()
        with open ("tests/"+file_num, 'r') as testa_file:
            first_input_pattern = testa_file.readline().rstrip()
            second_input_text = testa_file.readline().rstrip()
             # return both lines in one return
             
    else :
        print("Wrong input, must be I or F")
        
    return (first_input_pattern,second_input_text)# this is the sample return, notice the rstrip function

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(first_input_pattern, second_input_text):
    # this function should find the occurances using Rabin Karp alghoritm 
    first_input_pattern_length = len(first_input_pattern) #find length of pattern
    first_input_pattern_hash = hash(first_input_pattern) #pattern is being hased using build in function -> gives hashed value of pattern
    
    second_input_text_length = len(second_input_text) # find length of text
    second_input_text_hash = hash(second_input_text[:first_input_pattern_length]) # calculates the hash value for the first substring of length first_input_pattern_length in the second_input_text string. 
    
    output = [] #creates a list called output
    
    for num in range(second_input_text_length - first_input_pattern_length + 1): #is a for loop that iterates over a range of values from 0 up to and including second_input_text_length - first_input_pattern_length.
        if second_input_text_hash == first_input_pattern_hash and second_input_text[num:num+first_input_pattern_length]==first_input_pattern: # if they are even
            output.append(num)  # adds index num to the list -> output                                                                        # and if p len starting from index num is even with p 
        elif num + first_input_pattern_length<second_input_text_length: # if idex+p_length is smaller than second inp_length
            second_input_text_hash = hash(second_input_text[num+1:num+first_input_pattern_length+1]) #This line calculates the hash value of the substring string that starts at index num+1 and ends at index num+first_input_pattern_length+1.
              
    # and return an iterable variable
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

