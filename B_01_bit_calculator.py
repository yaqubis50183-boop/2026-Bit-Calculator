def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Display instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1  
    ''')

# ask users for file type (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

         # check for an image...
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text...
        elif response in ['text', 'txt', 't']:
            return "text"

        # if the response is invalid output an error
        else:
            print("Please enter a valid file type")


def int_check(question, low):
    error = f"Please enter a number with no decimal points (not letters or anything else) that is more than or equal to {low}\n"
    while True:
        try:
            # Ask for a number with the custom prompt
            response = int(input(question))

            # Check if the number is valid
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Calculates how many bits are needed to represent an image
def integer_calc():
    # Ask    the user to type an integer that's more than or equal to 0.
    integer = int_check("Integer: ", 0)

    #Works out and converts integer to binary, then represents it in binary digits
    raw_binary = bin(integer)

    #removes the "0b" at the beginning from the raw binary conversion
    binary = raw_binary[2:]
    num_bits = len(binary)

    # Set up answer and return it
    answer = (f"{integer} in binary is {binary}"
              f"\nWe need {num_bits} bits to represent it.")
    return answer


def calc_text_bits():

    # Get text from user
    response = input("Enter some text: ")

    # Calculate bits if needed
    num_chars = len(response)
    num_bits = num_chars * 8

    # Set up answer and return it
    answer = (f"{response} has {num_chars} characters."
              f"\nWe need {num_chars} x 8 bits to represent it"
              f"\nwhich is {num_bits} bits")

    return answer


def image_cal():
    # Get the image dimension
    width = int_check("Width: ", 1 )
    height = int_check("Height: ", 1)

    # calculate number of pixels and multiply by 24 to get he number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels:  {width} x {height} = {num_pixels} "
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer

# Main routine goes here
statement_generator("Bit Calculator", "*")

want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()



while True:
    file_type = get_filetype()

    # if user chose 'i', ask if they want an image / integer
    if file_type == 'i':

        want_image = input("Press <enter> for an integer or any key for an image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"


    if file_type == "xxx":
        break

    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)

    elif file_type == "text":
        text_ans = calc_text_bits()
        print(text_ans)

    else:
        image_ans = image_cal()
        print(image_ans)