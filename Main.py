from dashboard import run_dashboard
from file_manager import create_data_files


def main():
    print("=" * 45)
    print("       WELCOME TO STUDENT STUDY PLANNER")
    print("=" * 45)

    create_data_files()
    run_dashboard()


if __name__ == "__main__":
    main()
