from quiz_console import run_quiz_console
from quiz_app import run_quiz_app

def main():
    print("=" * 50)
    print("Welcome to GeoTrivia!".center(50))
    print("=" * 50)
    print("To begin, please choose a mode:")
    print("[1] Console\n[2] App")

    choice = input()
    if choice == '1':
        run_quiz_console()
    elif choice == '2':
        run_quiz_app()
    else:
        print("Please choose a valid option. Exiting now...")

if __name__ == "__main__":
    main()