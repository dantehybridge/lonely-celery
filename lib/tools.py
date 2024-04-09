import os, json, random as rnd, requests as rqs

# https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team}/roster
# https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{team}/roster?enable=roster,projection,stats

# site.api.espn.com/apis/site/v2/sports/football/nfl/teams -> gets all teams with id, logo, and name

urls = ('https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams', '', '')

def gets(url):
    try:
        data = rqs.get(url)
        data = data.json()

        return data
    except Exception as error:
        print(error)

def saves(name, data):
    try:
        os.remove(f'{name}-data.json') if os.path.exists(f'{name}-data.json') else None

        with open(f'{name}.json', 'w') as file:
            json.dump(data, file)
    except Exception as error:
        print(error)

def Search(opt, input):
    if not input or not opt:
        return

    def by_team(input):
        # input: it is an integer; the integer is the team id

        try:
            assert isinstance(input, int), 'The input should be an integer. Try again.'

            return input
        except Exception as error:
            print(error)

    def by_random(input):
        # input: it is a tuple comprised of filters

        def handleGets(url):
            return gets(url)
        
        def handleSaves(data):
            name = data['team']['slug']
            saves(name, data)

        try:
            assert isinstance(input, tuple), 'The input should be a tuple. Try again.'

            if input[0] == False:
                random = rnd.randint(1, 34)
                data = handleGets(f'{urls[0]}/{random}')
                handleSaves(data)
            else:
                choices = {
                    'afc': {
                        1: [33, 4, 5, 23],      # North
                        2: [2, 15, 17, 20],     # East
                        3: [34, 11, 30, 10],    # South 
                        4: [7, 12, 13, 24]      # West
                    },
                    'nfc': {
                        1: [3, 8, 9, 16],       # North
                        2: [6, 19, 21, 28],     # East
                        3: [1, 29, 18, 27],     # South
                        4: [22, 14, 25, 26]     # West
                    }
                }

                if len(input[1]) == 2:
                    divs = ['north', 'east', 'south', 'west']

                    if input[1][0] == 'afc':
                        if input[1][1] == divs[0]:
                            random = rnd.choice(choices['afc'][1])
                            data = handleGets(f'{urls[0]}/{random}')
                        
                        if input[1][1] == divs[1]:
                            random = rnd.choice(choices['afc'][2])
                            data = handleGets(f'{urls[0]}/{random}')
                        
                        if input[1][1] == divs[2]:
                            random = rnd.choice(choices['afc'][3])
                            data = handleGets(f'{urls[0]}/{random}')

                        if input[1][1] == divs[3]:
                            random = rnd.choice(choices['afc'][4])
                            data = handleGets(f'{urls[0]}/{random}')

                    if input[1][0] == 'nfc':
                        if input[1][1] == divs[0]:
                            random = rnd.choice(choices['nfc'][1])
                            data = handleGets(f'{urls[0]}/{random}')
                        
                        if input[1][1] == divs[1]:
                            random = rnd.choice(choices['nfc'][2])
                            data = handleGets(f'{urls[0]}/{random}')
                        
                        if input[1][1] == divs[2]:
                            random = rnd.choice(choices['nfc'][3])
                            data = handleGets(f'{urls[0]}/{random}')

                        if input[1][1] == divs[3]:
                            random = rnd.choice(choices['nfc'][4])
                            data = handleGets(f'{urls[0]}/{random}')

                if len(input[1]) == 1:
                    if input[1][0] == 'afc':
                        random = rnd.choice(choices['afc'][rnd.randint(1, 4)])
                        data = handleGets(f'{urls[0]}/{random}')
                    
                    if input[1][0] == 'nfc':
                        random = rnd.choice(choices['nfc'][rnd.randint(1, 4)])
                        data = handleGets(f'{urls[0]}/{random}')

                handleSaves(data)

        except Exception as error:
            print(error)

    def by_division(input):
        # input: it is a duplet; the first element is the conference name as a string, e.g. "afc", and second element is the division name as a string, e.g. "north"

        def handleGets(url):
            return gets(url)
        
        def handleSaves(cnf, div, data):
            name = f'{cnf}-{div}'
            data = data['sports'][0]['leagues'][0]['teams']

            dump = []

            if cnf == 'afc':
                if div == 'north':
                    for team in data:
                        if team['team']['slug'] in ['baltimore-ravens', 'cincinnati-bengals', 'cleveland-browns', 'pittsburgh-steelers']:
                            dump.append(team)
            
                if div == 'east':
                    for team in data:
                        if team['team']['slug'] in ['buffalo-bills', 'miami-dolphins', 'new-england-patriots', 'new-york-jets']:
                            dump.append(team)
            
                if div == 'south':
                    for team in data:
                        if team['team']['slug'] in ['houston-texans', 'indianapolis-colts', 'jacksonville-jaguars', 'tennessee-titans']:
                            dump.append(team)
            
                if div == 'west':
                    for team in data:
                        if team['team']['slug'] in ['denver-broncos', 'kansas-city-chiefs', 'las-vegas-raiders', 'los-angeles-chargers']:
                            dump.append(team)
            
            if cnf == 'nfc':
                if div == 'north':
                    for team in data:
                        if team['team']['slug'] in ['chicago-bears', 'detroit-lions', 'green-bay-packers', 'minnesota-vikings']:
                            dump.append(team)
                
                if div == 'east':
                    for team in data:
                        if team['team']['slug'] in ['dallas-cowboys', 'new-york-giants', 'philadelphia-eagles', 'washington-commanders']:
                            dump.append(team)
                
                if div == 'south':
                    for team in data:
                        if team['team']['slug'] in ['atlanta-falcons', 'carolina-panthers', 'new-orleans-saints', 'tampa-bay-buccaneers']:
                            dump.append(team)
                
                if div == 'west':
                    for team in data:
                        if team['team']['slug'] in ['arizona-cardinals', 'los-angeles-rams', 'san-francisco-49ers', 'seattle-seahawks']:
                            dump.append(team)

            saves(name, dump)

        try:
            assert isinstance(input, tuple), 'The input should be a tuple. Try again.'

            data = handleGets(urls[0])
            handleSaves(input[0], input[1], data)
        except Exception as error:
            print(error)

    def by_conference(input):
        # input: it is a string; it should match the conference name in lowercase or uppercase

        def handleGets(url):
            return gets(url)
        
        def handleSaves(cnf, data):
            name = cnf
            data = data['sports'][0]['leagues'][0]['teams']

            dump = {
                'North': [],
                'East': [],
                'South': [],
                'West': []
            }

            if cnf == 'afc':
                for team in data:
                    if team['team']['slug'] in ['baltimore-ravens', 'cincinnati-bengals', 'cleveland-browns', 'pittsburgh-steelers']:
                        dump['North'].append(team)
                    
                    if team['team']['slug'] in ['buffalo-bills', 'miami-dolphins', 'new-england-patriots', 'new-york-jets']:
                        dump['East'].append(team)
                    
                    if team['team']['slug'] in ['houston-texans', 'indianapolis-colts', 'jacksonville-jaguars', 'tennessee-titans']:
                        dump['South'].append(team)

                    if team['team']['slug'] in ['denver-broncos', 'kansas-city-chiefs', 'las-vegas-raiders', 'los-angeles-chargers']:
                        dump['West'].append(team)
                    
            if cnf == 'nfc':
                for team in data:
                    if team['team']['slug'] in ['chicago-bears', 'detroit-lions', 'green-bay-packers', 'minnesota-vikings']:
                        dump['North'].append(team)
                    
                    if team['team']['slug'] in ['dallas-cowboys', 'new-york-giants', 'philadelphia-eagles', 'washington-commanders']:
                        dump['East'].append(team)
                    
                    if team['team']['slug'] in ['atlanta-falcons', 'carolina-panthers', 'new-orleans-saints', 'tampa-bay-buccaneers']:
                        dump['South'].append(team)

                    if team['team']['slug'] in ['arizona-cardinals', 'los-angeles-rams', 'san-francisco-49ers', 'seattle-seahawks']:
                        dump['West'].append(team)

            saves(name, dump)
        
        try:
            assert isinstance(input, str) and input in ['afc', 'nfc'], f'The conference name you entered is not valid. Try again.'

            data = handleGets(urls[0])
            handleSaves(input, data)
        except Exception as error:
            print(error)
        
    menu = {
        1: by_team,
        2: by_random,
        3: by_division,
        4: by_conference
    }

    return menu[opt](input)

tools = {
    1: Search,
    #2: Update,
    #3: Average
}