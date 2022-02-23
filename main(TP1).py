
import sys
import voiture as myVoiture
def main():
    myCar = myVoiture.Voiture("Mercedes","Classe␣A", 340,"noire")
    myCar2 = myVoiture.Voiture()
    myCar.add_option("toit")
    print(myCar.is_option_present("toit"))
    myCar.remove_option("toit")
    print(myCar.get_option())
    print(myCar)
    return(0)

if __name__ == "__main__":
    sys.exit(main())