with open('../README.md', 'w') as fh:
    fh.write('''\t\t\tTELECOM SERVICE SIMULATION
    
This Python script simulates a simple telecom service where users can register their phone numbers, recharge their airtime balance, 
and interact with the service through a basic menu. The script performs various operations including generating phone numbers, 
handling user input for registration, and storing user data in a MySQL database.

Features

1. Phone Number Generation:
    - The script generates a random Nigerian phone number starting with one of the common prefixes (080, 070, 090, 081).

2. User Registration:
    -First-time users are prompted to register their phone numbers.
    -Users enter their first and last names, and an initial airtime balance.
    -The entered data is validated to ensure correctness (e.g., names must contain only alphabetic characters).
    -Successful registration stores user details in a MySQL database.
    
3. Airtime Recharge:
    -Users can enter an amount to recharge their airtime balance and also buy data.
    -The input is validated to ensure it is numeric.
    
4. Existing User Verification:
    -The script checks if a user's phone number is already registered in the database.
    -If the number exists, the user can continue to interact with the service.
    
5. User Interaction:
    - Users interact with the service through a simple menu system.
    - The script uses functions to display messages slowly for a better user experience.
    
    
Setup

Prerequisites
- Python 3.x
- MySQL Server
- Required Python packages: pymysql, random, time,datetime,os,sys,decimal,pyttsx3
    
Installation
1. Clone the repository or download the script file.
2. Install the required Python packages:
            -pip install pymysql
3. Set up your MySQL database and create a table named telecom_tbl with the following structure:\n

                            CREATE TABLE telecom_tbl (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first_name VARCHAR(255),
                            last_name VARCHAR(255),
                            phone_number VARCHAR(20),
                            airtime_balance DECIMAL 
                        );
                        
4. Update the database connection details in the script:\n
                            db = pymysql.connect(
                            user='your_db_user',
                            password='your_db_password',
                            host='your_db_host',
                            database='Telecom_db'
                        )

Usage

1. Run the script
2. Follow the on-screen prompts to register a new number or verify an existing one.
3. Enter your details as requested to complete the registration or access the service.

Code Overview


Main Functions

- gen_number(): Generates a random phone number.
- print_slowly(text): Prints text to the console with a slight delay between characters.
- re_charge(): Prompts the user to enter an amount to recharge and validates the input.
- register_num(): Handles the registration process for new users, including data input and validation, and storing the data in the database.
- already_user(): Checks if a user's phone number is already registered and allows them to continue using the service.
- option(): Main menu that prompts the user to either register a new number or verify an existing one.

Error Handling

The script includes basic error handling to manage invalid inputs and database connection issues.

Conclusion
 
This script provides a basic simulation of a telecom service's registration and airtime recharge functionality. 
It demonstrates handling user input, generating random phone numbers, interacting with a MySQL database, and
creating a simple user interface through the console.    
    
''')