import QNAPControl

def main():
    lcd = QNAPControl.QnapLCD(None)
    lcd.backlight(True)
    lcd.write("test")

if __name__ == "__main__":
    main()