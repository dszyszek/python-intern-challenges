import datetime
from json import dumps

def make_report(url, results, dir, mode, dic=''):
    """This function will handle report-making process"""
    report_decision = input('Would you like to make report? (y/n)\n')

    if report_decision == 'y':                      # Check if user wants to create a report
        exec(url, results, dir, mode, dic)
    elif report_decision == 'n':
        pass
    else:
        print('Unknown command')


def exec(url, results, dir, mode, dic=''):
    """This function will make report"""
    now = datetime.datetime.now()

    with open(f'./reports/{dir}/report_{now.strftime("%Y-%m-%d")}_{now.strftime("%H;%M")}', 'w+') as file:

        file.write(f'================= Report {now.strftime("%Y-%m-%d %H:%M")} =================\n')    # Header of report file
        file.write(f'Domain: {url}')

        if mode == 'discover':
            file.write(f'\nDict used: {dic}\n')
            file.write('\nSubdomains:\n')
            for i,x in enumerate(results):          # Write all the results to the file
                file.write(f'{i+1}) {x}\n')
        elif mode == 'crawl':
            for val in results.values():            # Change type of links to string (so it could be dumped with json)
                val['links'] = str(val['links'])

            results = dumps(results, indent=4, sort_keys=False)         # Write results with nice formatting

            file.write('\nMap of the page:\n')
            file.write(results)