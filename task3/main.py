import sys
from pathlib import Path
from colorama import Fore

def main(path, spaces=""):
  #checking if the path is exist and this one is a directory
  if not (path.exists() and path.is_dir()):
    print("Please enter correct path")
    return

  # Print here directory to avoid dublicates in for in loop
  print(Fore.BLUE + f"{spaces}{path.name}/")

  for el in path.iterdir():
    if el.is_dir():
      main(el, spaces + "    ")
    else:
      print(Fore.GREEN +f"{spaces}    {el.name}")


if __name__ == "__main__":
    #Checking if path is correct
    if len(sys.argv) < 2:
      print('Please enter correct path')
      sys.exit()

    #Resolving path(not sure, but works with absolute path as python3 main.py /ROOT/goit-pycore-hw-04/task3/picture)
    path = Path(sys.argv[1]).resolve()
    main(path)