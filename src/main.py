from lib.db_handler import Handler
from TUI import menu, logo

count = 0

while True:
    if count <= 0:
        logo()
    menu()
    count += 1