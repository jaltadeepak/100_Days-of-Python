with open(r"24_files+directories+paths\Mail Merge Project\Input\Names\invited_names.txt") as names:
    name_list = names.read().split("\n")

with open(r"24_files+directories+paths\Mail Merge Project\Input\Letters\starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in name_list:
        with open(f"24_files+directories+paths\Mail Merge Project\Output\ReadyToSend\letter_for_{name}", "w") as output:
            output.write(letter_content.replace("[name]", f"{name}"))

    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
