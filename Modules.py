import Circle
import ReverseNaming

def CurrentModule():
    Circle.Area()
    ReverseNaming.ReverseNaming()
    ThisModule()

def ThisModule():
    print("Hello, You are using present file’s module. ")

def main():
    CurrentModule()

main()