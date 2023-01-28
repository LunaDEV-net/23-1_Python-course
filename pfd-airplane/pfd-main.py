import turtle as t
import fakeSky

# for logging
file_name = "{./pfd-main.py}:"


def configureWindow():
    """sets the Window Size, change BG color and the Title"""
    t.screensize(1024, 966, bg="black")
    print(f"{file_name} set Window Size")
    print(f"{file_name} set Window BG Color")
    t.title("LUNA: Airplane PFD")
    print(f"{file_name} set Window Title")

def clear():
    t.home()
    t.clear()
    t.reset()

def main():
    clear()
    configureWindow()
    fakeSky.makeSquare(0, 0, 0, "blue")
    t.mainloop()


if __name__ == '__main__':
    main()
