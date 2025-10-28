import sys

#клиенты которые не видели письмо
def get_clients_not_seen_ad(clients, recipients):
    clients_set = set(clients)
    recipients_set = set(recipients)
    return list(clients_set - recipients_set)

#участники которые не клиенты
def get_non_client_participants(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)
    return list(participants_set - clients_set)

#клиенты которые не участники
def get_clients_not_attended_event(clients, participants):
    clients_set = set(clients)
    participants_set = set(participants)
    return list(clients_set - participants_set)

def main(task_name):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', #участники
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is'] #получатели письма

    if task_name == 'call_center':
        result = get_clients_not_seen_ad(clients, recipients)
    elif task_name == 'potential_clients':
        result = get_non_client_participants(clients, participants)
    elif task_name == 'loly_program':
        result = get_clients_not_attended_event(clients, participants)
    else:
        raise ValueError("Неизвестный аргумент")

    print(result)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Слишком много аргументов")
    task_name = sys.argv[1]
    main(task_name)