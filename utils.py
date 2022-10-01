import re
import os
import datetime


def read_payment_file(payment_file_path: str) -> list:
    """
    Returns a list with the payments saved in the file "payment.txt"

    Parameters
    ----------
    payment_file_path (str): Directory where the "payment.txt" file is stored
    """

    with open(payment_file_path, "r") as payment_file:
        # Iteration between lines to obtain the numerical value (payment)
        return [float(re.sub("\n", "", line).split(": ")[1]) for line in payment_file]


def write_payment_file(payment_file_path: str, payment_list: str):
    """
    Returns an updated "payment.txt" file. If there is a new payment to add in
    an existing "payment.txt", it is added and the Total is recalculated

    Parameters
    ----------
    payment_file_path (str): Directory where the payment.txt file is stored.
    payment_list (str): List with the new values (payments) to add in the payment.txt file.
                        The first value is the total payments and the second value is the
                        new payment. Both are the same because only one payment is added.
    """

    with open(payment_file_path, "w") as payment_file:

        # The total of payments is added to the file that is being generated
        payment_file.write(f"Total: {payment_list[0]}\n")

        # Next, all listed payments (existing and new) are added
        for index, payment in enumerate(payment_list[1:]):
            payment_file.write(f"Payment {index + 1}: {payment}\n")


def create_payment_folders(source_file_path: str, root_path: str, project_name: str = "Payments"):
    """
    Generates a directory of folders and distributes payments from the source file in new
    user folders and then by year of payment.

    Parameters
    ----------
    source_file_path (str): Directory where the source file is located
    root_path (str): Directory where you want to create the root folder of the project
    project_name (str): Project root folder name
    """

    with open(source_file_path, "r") as source_file:

        for line in source_file:

            # For each line, it is separated by space and assigned an attribute
            id_user, date, payment = line.split(" ")

            # For each line, the "date" attribute changes from String to Datetime
            # "date" will be a record of type: yyyy-mm-dd hh:mm:ss
            date = datetime.datetime.strptime(date, "%d-%m-%Y")

            # For each line, the "year" value of each record is generated in string format
            # To get the "year" value separated from the date
            year = str(date.year)

            # For each line, a folder path is generated with directory(str) + user(str) + year(str)
            payment_folder_path = os.path.join(root_path, project_name, id_user, year)

            # For each path created on each line, a folder directory is created if one doesn't
            # already exist. Each missing folder in the directory will be generated.
            os.makedirs(payment_folder_path, exist_ok=True)

            # Indicates what the final address should be for storing distributed payments
            # For each line, a new path is created to indicate where the txt file will be located
            payment_file_path = os.path.join(payment_folder_path, "payment.txt")

            # If the directory "payment_file_path" exists:
            if os.path.exists(payment_file_path):

                # If the path 'client/year/payment.txt' already exists, it means that this client
                # already belongs to the database and, therefore, there may be the possibility of
                # new payments.

                # First, a list of payments is obtained from the directory to be analyzed.
                # The "read_payments_file" function returns a list of existing payments
                payment_list = read_payment_file(payment_file_path)

                # In the list of payments obtained, the new payment is added
                payment_list.append(float(payment))

                # And from this list, the first value is the sum of the following ones.
                # Therefore, this value is recalculated
                payment_list[0] = sum(payment_list[1:])

                # The updated list with the first recalculated value is written back to
                # the "payments.txt" file
                write_payment_file(payment_file_path, payment_list)

            # If the "pathment_file_path" directory does not exist:
            else:

                # If the line generates a new "client/year" path, it will be necessary to
                # register this new payment.
                # In new "payment.txt" files the first record (Total) and the second (Payment 1)
                # will be the same
                write_payment_file(payment_file_path, [float(payment), float(payment)])
