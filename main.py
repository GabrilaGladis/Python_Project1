from attack_simulation.brute_force import brute_force_attack
from attack_simulation.sql_injection import sql_injection_simulation
from attack_simulation.xss_attack import xss_attack_simulation
from defense.brute_force_defense import brute_force_defense
from defense.sql_injection_defense import sql_injection_defense
from defense.xss_defense import xss_defense
from reports.report_generator import generate_report

def menu():
    print("Cybersecurity Attack Simulation and Prevention System")
    print("1. Simulate Brute Force Attack")
    print("2. Simulate SQL Injection Attack")
    print("3. Simulate XSS Attack")
    print("4. Defend Against Brute Force Attack")
    print("5. Defend Against SQL Injection")
    print("6. Defend Against XSS Attack")
    print("7. Generate Report")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        brute_force_attack()
    elif choice == '2':
        sql_injection_simulation()
    elif choice == '3':
        xss_attack_simulation()
    elif choice == '4':
        brute_force_defense()
    elif choice == '5':
        sql_injection_defense()
    elif choice == '6':
        xss_defense()
    elif choice == '7':
        generate_report()
    elif choice == '8':
        exit()
    else:
        print("Invalid choice! Please select again.")
        menu()

if __name__ == "__main__":
    menu()
