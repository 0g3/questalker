#! /usr/bin/env python3
import urlgenerator

def main(typ='feam'):
  ug = urlgenerator.URLGenerator(typ=typ)
  while 1:
    dat = input('>> ')
    if dat == 'exit':
      quit()
    try:
      year = dat[:4]
      season = dat[4]
      n_question = dat[5:]
      webbrowser.open(ug.gen(int(year), season, int(n_question)))
    except:
      print('not open.')

if __name__ == '__main__':
  main()
