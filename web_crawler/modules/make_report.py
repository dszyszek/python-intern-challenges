import datetime
from json import dumps

def make_report(url, results, dir, mode, dic=''):
    report_decision = input('Would you like to make report? (y/n)\n')

    if report_decision == 'y':
        exec(url, results, dir, mode, dic)
    elif report_decision == 'n':
        pass
    else:
        print('Unknown command')


def exec(url, results, dir, mode, dic=''):
    now = datetime.datetime.now()

    with open(f'./reports/{dir}/report_{now.strftime("%Y-%m-%d")}_{now.strftime("%H;%M")}', 'w+') as file:

        file.write(f'================= Report {now.strftime("%Y-%m-%d %H:%M")} =================\n')
        file.write(f'Domain: {url}')

        if mode == 'discover':
            file.write(f'\nDict used: {dic}\n')
            file.write('\nSubdomains:\n')
            for i,x in enumerate(results):
                file.write(f'{i+1}) {x}\n')
        elif mode == 'crawl':
            for val in results.values():  # Change type of links to string (so it could be dumped with json)
                val['links'] = str(val['links'])

            results = dumps(results, indent=4, sort_keys=False)

            file.write('\nMap of the page:\n')
            file.write(results)