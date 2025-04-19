def a(mail):
    domain = []
    for email in mail.split(','):
        parts = email.strip().split('@')
        domain = parts[1].split('.')[0]
        if domain.endswith('.com'):
            domain.append(domain[:-4])  
    return domain


mail = str(input("Enter the email address:"))
b = a(mail)
print(b)
