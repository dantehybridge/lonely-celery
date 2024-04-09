import lib.confs as confs, lib.slugs as slugs, lib.tools as tools

menu = {
    'header': "+{}+\n".format("-" * 90) + "\n+{:^90}+\n".format("Post-Game Stats Menu") + "\n+{}+".format("-" * 90),
    'options': ('1. Search', '2. Update', '3. Average', '4. Exit'),
    'suboptions': (('1. By Team', '2. By Random', '3. By Division', '4. By Conference')),
    'footer': "+{}+\n".format("-" * 90) + "\n+{:^90}+\n".format("by Dante Fernández, @dantehybridge") + "\n+{}+".format("-" * 90)
}

def view_menu(options):
    print(menu['header'] + "\n")

    for option in options:
        print("+{:^90}+".format(option))

    print("\n" + menu['footer'])

def app():
    # Here we print the menu. The user will choose an option. We will then call the function that corresponds to the chosen option.

    view_menu(menu['options'])

    opt = int(input('\nWrite the number of the action you want to perform: '))

    if opt == 1:
        view_menu(menu['suboptions'])

        sub = int(input('\nWrite the number of the action you want to perform: '))

        if sub == 4:
            cnf = input('\nWrite the conference you want to search for: ').lower()

            return tools.Search(4, cnf)
        
        if sub == 3:
            cnf = input('\nWrite the conference you want to search for: ').lower()

            div = input('\nWrite the division you want to search for: ').lower()

            return tools.Search(3, (cnf, div))
        
        if sub == 2:
            flt = input('\nWould you like to set some filters? (y/n) ').lower()

            if flt == 'y':
                cnf = input('\nWrite the conference name you want to search for: ').lower()

                flt = input('\nWould you like to add more filters? (y/n) ').lower()

                if flt == 'y':
                    div = input('\nWrite the division name you want to search for: ').lower()

                    return tools.Search(2, (True, [cnf, div]))
                
                if flt == 'n':
                    return tools.Search(2, (True, [cnf]))
            
            if flt == 'n':
                return tools.Search(2, (False, []))
    
if __name__ == "__main__":
    app()
