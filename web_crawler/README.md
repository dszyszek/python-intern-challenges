# WEB CRAWLER
Ever wanted to gather some info about site you are browserling?
Then this is right place.

# Start
To start program:
1. Install required packages (-> requirements.txt)
2. Write 'python3 main.py' in console (working dir in main folder)

# What can it do?
There are two basic modes: 
1) Crawl
2) Search for subdomains

Crawl mode:
This one gonna be straight-forward: crawl mode makes map of site you enter. You can type address of the page with or without 'http://' prefix.
Result of the search will be printed to the console in nice, pretty-printed format. Result will contain url of the current site, links to other sites (one the same domain) and title of the page.

Search for subdomains:
Here program will try to find subdomains of the page you give. Searching-engine requires base of subdomain names (e.g mail, video).
The program supports adding your own dictionary (info about proper way to add dictionary below), but you can use one of pre made ones: pre-min.log and pre-max.log.
Pre-min.log- base with a few subdomain names. This one is good for simple and fast research.
Pre-max.log- this base contains much more subdomain names. Searching will last longer, but it gives greater chance to find hidden subdomains.

The best thing in this program is that it can make report with results of the search. 
After successful search program will ask you if you want to make report.
If yes, report is going to be saved in one of two possible paths (depends which mode you selected):
./reports/subdomains or ./reports/maps_of_sites.
Format of report names: report_YYYY-MM-DD_HH;MM (e.g report_2019-02-02_05:32)
Map of site report will be pretty printed so you can exactly see map of page. 

# How to add a dictionary
Adding dictionary is all about uploading dictionary you have so you can use it for searching subdomains.
To add dictionary: 
1. Enter name of the dictionary
2. Enter path to the file (notice it must be absolute path e.g: /Users/<user_name>/Desktop/dictionary.log)

Few words about dictionaries:
It MUST contain only names used to search e.g:

mail
video
main

And nothing else! White spaces will be stripped for you.
Format of dictionary file: .log -> please stick to that!
When you are going to use your own dict, just type its name, without .log

And that's it, good luck with searching!