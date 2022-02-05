import datetime

string1 = "a month ago"
string2 = "2 months ago"
string3 = "a year ago"
string4 = "2 days ago"
string5 = "yesterday"

def daysAgo(date):
  tod = datetime.datetime.now()
  date = date.split()
  daysAgo = 0
  if date[0] == "yesterday":
    daysAgo = 1
  elif date[1] == "days" or date[1] == "day":
    daysAgo = int(date[0])
  elif date[1] == "months" or date[1] == "month":
    if date[0] == "a":
      daysAgo = 30
    else:
      daysAgo = 30 * int(date[0])
  elif date[1] == "years" or date[1] == "year":
    if date[0] == "a":
      daysAgo = 365
    else:
      daysAgo = 365 * int(date[0])
  d = datetime.timedelta(days=daysAgo)
  return tod - d