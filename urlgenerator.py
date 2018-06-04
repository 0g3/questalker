'''
talk with:
http://www.fe-siken.com/
https://www.ap-siken.com/
'''
import requests
import csv
import os
import webbrowser


class URLGenerator(object):
  FE = 'http://www.fe-siken.com/kakomon/{}_{}/' 
  AP = 'https://www.ap-siken.com/kakomon/{}_{}/'
  AM = 'q{}.html'
  PM = 'pm{:02}.html'

  def __init__(self, typ='feam'):
    if typ == 'feam':
      url_fmt = self.FE + self.AM
    if typ == 'fepm':
      url_fmt = self.FE + self.PM
    if typ == 'apam':
      url_fmt = self.AP + self.AM
    if typ == 'appm':
      url_fmt = self.AP + self.PM

    self.url_fmt = url_fmt

  def gen(self, year, season, n_question):
    year -= 1988
    if season in ('h', 'H'):
      season = 'haru'
    if season in ('a', 'A'):
      season = 'aki'
    # H23のとき処理
    if year == 23:
      season = 'toku'
    return self.url_fmt.format(year, season, n_question)
