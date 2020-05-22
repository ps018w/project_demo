import os, time
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename,'r'):
    pass
  timestamp = os.stat(filename)
  print(timestamp.st_mtime)
  # Convert the timestamp into a readable format, then into a string

  print(time.ctime(os.path.getmtime(filename)))
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return 0

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd