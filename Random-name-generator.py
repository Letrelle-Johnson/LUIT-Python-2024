import random
import string

# Number of EC2 Instances 
num_of_ec2_instances = int(input("Enter number of EC2 Instances"))

# Name of the Departments 
departments = input("Input name of department")

# Departments allowed to use name generator 
allowed_departments = ("Accounting", "FinOps", "Marketing")

# Confirm department inputed is included in the allowed departments list
if departments in allowed_departments:
    for _ in range(num_of_ec2_instances):

        # Generate a random three-letter string
        random_char = "".join(random.choices(string.ascii_letters, k=3))

        # Create a new generated name by combining department, random characters, and a random number
        new_generated_names = departments + "-" + random_char + str(random.randrange(0, 50))

        # Print the generated name
        for name in new_generated_names:
            print(new_generated_names)
else:
    # Print error message if the department is not valid
    print("Sorry to inform you but you cannot use the name generator.")
