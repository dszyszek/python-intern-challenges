# CSV REPORT PROCESSING
This program is made for processing given .csv file.
The main feature is to read .csv file (standard input), convert date, 
write three-letter shortcut of a country (from given city) and write it to new file, created in ./processed_files directory 
(user inputs name of newly created file).

# Usage
The program is very simple. To upload file just input (absolute!) path to the .csv file which is going to be processed and hit enter. Then write name of file, which is going to be created (the one with processed data). Remember to input ONLY name (no .csv format). 

# General info
The program will finish in one of the following situations:
1) Input file was not .csv
2) Input file was empty
3) Everything went well

The program will print warning message, if:
1) Name of new file is already in use (the program will then generate name in the following format: random_XXXXXX.csv, where X is randomly generated letter/number)
2) Wrong date format in input file (correct: MM/DD/YYYY) -> program will not do anything with given date
3) Cannot find requested city in DB

Hope you enjoy using that program!