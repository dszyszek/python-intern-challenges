import datetime

def make_report(url, results, dir):
    now = datetime.datetime.now()
    with open(f'./reports/{dir}/report_{now.strftime("%Y-%m-%d")}_{now.strftime("%H;%M")}', 'w+') as file:
        file.write(f'================= Report {now.strftime("%Y-%m-%d %H:%M")} =================\n')
        file.write(f'Domain: http://{url}')
        file.write('\nSubdomains:\n')
        for i,x in enumerate(results):
            file.write(f'{i+1}) {x}\n')