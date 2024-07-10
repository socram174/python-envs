from dotenv import  load_dotenv
import os

load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(os.environ["MESSAGE"])
    if os.environ["MESSAGE"] == "HOLA":
        print("Si es")
    else:
        print("No es igual :(")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
