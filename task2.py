from pathlib import Path

def get_cats_info(path):
  
  # checking for existing file and early return if not exist
  file = Path(path)
  if not file.exists():
    return None

  with open(path, mode='r', encoding="utf-8", errors="strict") as fh:
    formatted_list = []
    # checking case if lines have \n
    cats = [el.strip() for el in fh.readlines()]

    for cat in cats:
      id, name, age = cat.split(",")
      formatted_list.append({"id": id, "name": name, "age": age})

    return formatted_list


cats_info = get_cats_info("goit-pycore-hw-04/cats_file.txt") 
print(cats_info)
