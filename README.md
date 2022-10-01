# process, distribute and store files

## Description

This is a solution to organize a data file in a local directory.

Let's see an example of how the data is distributed when the code is working.


Original data sample:

```
customer_id, date, payment

C0124 24-04-2018 441.74
C1335 30-12-2018 958.44
0124 07-10-2018 39.36
C1335 01-01-2019 635.55
C9853 09-10-2019 281.69
C0124 12-07-2020 897.66
C9853 09-06-2020 301.17
```

And... After executing the code... a directory of folders is obtained.

    +-------------+
    | Root folder |
    +-------------+

      Payments

        +----------------------------------+
        | Customer folders (into Payments) |
        +----------------------------------+

          C0124
          C1335
          C9853

            +---------------------------+
            | Year folders (into C0124) |
            +---------------------------+

              2018
              2020

                +--------------------------+
                | payment file (into 2018) |
                +--------------------------+

                  payment.txt


The payment.txt file will contain:

    +-------------------+
    |                   |
    | Total: 1339.40    |
    | Payment 1: 441.74 |
    | Payment 2: 897.66 |
    |                   |
    +-------------------+
              
                  
## Step by step installation and program execution process

### Prerequisites

- python
- pip

### Get code

A zip file with the code is attached. It must be saved and unzipped in the working path with the desired name (for example: process_distribute_store)

### Create a virtualenv for the project

```sh
$ pip install virtualenv
$ cd process_distribute_store
$ virtualenv venv
$ source venv/bin/activate
```

## Execute project

```
$ python3 main.py arg1 arg2
```

IMPORTANT:

- arg1 is the directory where the source txt file is located
- arg2 is the directory where you want to generate the root folder of the project

Example: 

```
$ python3 main.py /user/process_distribute_store/original_payments.txt/ /user/desktop/
```

## Output program

In the case of the example, a "Payments" folder appears on the desktop with all the internal folders generated
