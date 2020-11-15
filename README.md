# Active-Directory-Users-Generator

     This a Powershell Windows Active Directory script, that will generate  bulk of users from a CSV file that contains usernames and other LDAP attributes 



# Procedure 

1) download both the Users-Generators.ps1 , and bulk_users1.csv files, 
2) Update bulk_users1.csv with your Users (you may use python or bash to generate a big list)
3) Update  Users-Generators.ps1 
     3.1) Change your domain, current value is LAB.LOCAL (do Ctrl+F inside script and change it if required)
     3.2) The script will also at the end, add the group "Users" , you might remove/change that group if you want.
     3.3) Ensure to Update the Location of the bulk_users1.csv file, inside the Users-Generators.ps1 , by changing this value accordingly :
           $ADUsers = Import-csv C:\Users\Administrator\Downloads\powershell_create_bulk_users\bulk_users1.csv
4) Before you Run the script, ensure that your AD does not have any of these new users , and delete any old ones (otherwise the script will just do a warning and do nothing)
5) To run the script, just ensure to be administraor in AD,  and run the ps1 file (right click, run powershell)

Note: script tested successfully on windows AD 2016.


# Note
    If you want to generate a long list CSV file of users,  you may use the python code in the repo : bulk_users_csv_file_generator.py
