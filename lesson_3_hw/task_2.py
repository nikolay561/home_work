def my_func(name, surname, year_of_birth, city, email, phone_numb):
    return f'{name} {surname} from {city}, year of birth - {year_of_birth}, email - {email}, ' \
           f'phone number - {phone_numb}.'


print(my_func(name='Guido', surname='van Rossum', year_of_birth='1956', city='USA', email='guido@py.com',
              phone_numb="it's a secret =)"))
