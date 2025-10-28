import sys

def find_name_by_email(email):
    with open('employees.tsv', 'r') as tsv_file:
        for line in tsv_file:
            if line.strip().endswith(email):
                parts = line.strip().split('\t')
                return parts[0]
    return None

def generate_letter(email):
    name = find_name_by_email(email)
    if name:
        letter = (f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. "
                  f"That’s a precondition for the professionals that our company hires.")
        print(letter)
    else:
        print(f"Email {email} not found in the employees.tsv file.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Too many arguments>")
    else:
        generate_letter(sys.argv[1])