#Get user email address
email = input('What is your email address?: ').strip()
print(email)

#slice out user name
user = email[:email.index('@')]
print('user = ',user)

#slice domain name
domain = email[email.index('@') + 1:email.index('.')]
print('domain = ', domain)
        

#format message
output = 'Your username is {} and your domain name is {}.'.format(user, domain)

#display output message
print(output)
