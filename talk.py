#! /usr/bin/env python3
import argparse
import sys
import webbrowser

import urlgenerator

def main(typ='feam'):
  ug = urlgenerator.URLGenerator(typ=typ)
  while 1:
    dat = input('[{}]問題を入力してください: '.format(typ))
    if dat == 'exit':
      quit()
    try:
      year = dat[:4]
      season = dat[4]
      n_question = dat[5:]
      url = ug.gen(int(year), season, int(n_question))
      webbrowser.open(url)
    except:
      print('not open.')

if __name__ == '__main__':
  p = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
  p.add_argument('someone', help='問題の種類(feam/fepm/apam/appm)を指定する。')
  args = p.parse_args()
  if args.someone not in ('feam', 'fepm', 'apam', 'appm'):
    print('問題の種類は「feam(基本情報午前), fepm(基本情報午後), apam(応用情報午前), appm(応用情報午後)」から指定してください。')
    sys.exit(1)

  main(typ=args.someone)
