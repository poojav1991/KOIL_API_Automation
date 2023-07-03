from utilities.config import *
import bcrypt
import secrets


def verify_password(inputted_password, hashed_password):
    return bcrypt.checkpw(inputted_password.encode('utf-8'), hashed_password.encode('utf-8'))
def querypayload(query):
    addbody={}
    qry= getQuery(query)
    # Usage example
    inputted_password = "pooja@123"  # Replace with the password provided by the user
    hashed_password_from_database = qry[4]  # Replace with the hashed password retrieved from the database

    passwords_match = verify_password(inputted_password, hashed_password_from_database)
    if passwords_match:
        print("Password is correct.")
        addbody['mobile'] = qry[3]
        addbody['password'] = 'pooja@123'
        return addbody
    else:
        print("Password is incorrect.")

    #print(addbody)
