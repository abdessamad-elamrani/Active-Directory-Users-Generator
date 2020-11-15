# Active-Directory-Users-Generator

This a Powershell Windows Active Directory script, that will generate  bulk of users from a CSV file that contains usernames and other LDAP attributes 

Notes :

+ To run the script

1) download both the Users-Generators.ps1 , and bulk_users1.csv files, 
2) Update bulk_users1.csv with your users (you may use python or bash to generate a big list)
3) Update  Users-Generators.ps1 
    >> change your domain, current value is LAB.LOCAL (do Ctrl+F inside script and change it if required)
    >> the script will also at the end, add the group "Users" , you might remove/change that group if you want.
4) To run the script, just ensure to be administraor in AD,  and run the ps1 file (right click, run powershell)

Note: script tested successfully on windows AD 2016.

