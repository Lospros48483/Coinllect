import json
import shutil
import os
import cv2
from PIL import Image

def delete_coin(num) -> None:
    try:
        with open("info.json", "r") as f:
            data_info = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No coins to delete.")
        return

    coin_to_delete = None
    for key, value in data_info.items():
        if value.get("num") == str(num):
            coin_to_delete = key
            break

    if coin_to_delete:
        img_name = data_info[coin_to_delete].get("image")
        img_path = os.path.join("Images", img_name) if img_name else None
        if img_path and os.path.exists(img_path):
            os.remove(img_path)
        del data_info[coin_to_delete]
        with open("info.json", "w") as f:
            json.dump(data_info, f, indent=4)
        print(f"Coin {num} deleted.")
    else:
        print(f"No coin found with number {num}.")

def add_coin() -> None:
    number = 0
    openfile = open('num.txt', 'w')
    with open("num.txt", "r") as fileread:
        content = fileread.read().strip()

    if content == "":  
        number = 1 
    else:
        number = int(content) + 1
    openfile.write(str(number))
    
    data_info = {}
    clear()
    name = input("What name do you put to the coin: ")
    description = input("Put a description: ")
    price = input("Put the price: ")  
    date = price = input("Put the date: ")        
        
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow("Camera", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(" "):
            img = f"coin_{name}.png"
            save_path = os.path.join("Images", img)
            cv2.imwrite(save_path, frame)
            break
    data_info[name] = {
    "name": name,
    "description": description,
    "price": price,
    "image": img,
    "date": date,
    "num": str(number)
    }
    with open("info.json", "w") as f:
        json.dump(data_info, f, indent=4)

    cap.release()
    cv2.destroyAllWindows()


def splash_screen():
    clear()
    with open('info.json', 'r') as openfile:
        data = json.load(openfile)

    print("coinllet".center(columns))
    try:
        for coin_id, coin_data in data.items():
            print(f"{coin_data['num']})  {coin_data['name']}".center(width_text))
    except:
        print("")
    print(" ")

def clear() -> None:
    with open('os.txt', 'r') as openfile:
        file = openfile.read()
        if file == "W" or file == "w":
            os.system("powershell clear")
        else:
            os.system("clear")

columns = shutil.get_terminal_size().columns
width_text = int(columns / 1.5)
with open('info.json', 'r') as openfile:
    data = json.load(openfile)

while True:
    splash_screen()
    ask = input("Add a coin (A), Delet a coin (D), View a photo of coin (V), View info (I) or Quit (Q) : ".center(columns))
    if ask == "q" or ask == "Q":
        quit()
    elif ask == "a" or ask == "A":
        add_coin()
    elif ask == "d" or ask == "D":
        splash_screen()
        ask1 = input("What number do you want to delete: ")
        delete_coin(ask1)
    elif ask == "v" or ask == "V":
        ask2 = input("What number do you want to view the photo: ")
        with open('info.json', 'r') as openfile:
            data = json.load(openfile)
        for coin_id, coin_data in data.items():
            if coin_data["num"] == ask2:
                img_path = os.path.join("Images", coin_data["image"])
                if os.path.exists(img_path):
                    Image.open(img_path).show()
                else:
                    print("Image not found.")
                break
    elif ask == "i" or ask == "I":
        splash_screen()
        ask3 = input("What number do you want to view the information: ")
        clear()
        for coin_id, coin_data in data.items():
            if coin_data["num"] == ask3:
                print(f"Name: {coin_data["name"]}".center(columns))
                print(f"Description: {coin_data["description"]}".center(columns))
                print(f"Price: {coin_data["price"]}".center(columns))
                print(f"Date: {coin_data["date"]}".center(columns))
                wait = input(" ")
                