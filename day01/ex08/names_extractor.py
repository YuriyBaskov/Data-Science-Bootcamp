import sys

# Достаем имя и фамилию
def extract_names(email):
    local_part, domain = email.split('@')
    first_name, last_name = local_part.split('.')
    return first_name.capitalize(), last_name.capitalize()

def process_emails(file_path):
    with open(file_path, 'r') as email_file:
        emails = email_file.readlines()

# Записываем имя, фамилию и почту
    with open('employees.tsv', 'w') as tsv_file:
        tsv_file.write('Имя\tФамилия\tE-mail\n')
        for email in emails:
            email = email.strip()
            first_name, last_name = extract_names(email)
            tsv_file.write(f'{first_name}\t{last_name}\t{email}\n')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Too many arguments")
    else:
        process_emails(sys.argv[1])