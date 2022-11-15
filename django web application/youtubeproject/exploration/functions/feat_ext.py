import pandas as pd
from datetime import date


def copy_df(df):
    return df.copy()

def feature_extraction(df):
    def categorize(title):

        Basketball = ['NBA','Boston Celtics','Brooklyn Nets','Philadelphia 76ers','Toronto Raptors','Chicago Bulls','New York Knicks',
                  'Cleveland Cavaliers','Detroit Pistons','Indiana Pacers','Milwaukee Bucks','Atlanta Hawks','Charlotte Hornets',
                  'Miami Heat','Orlando Magic','Washington Wizards','Denver Nuggets','Minnesota Timberwolves','Oklahoma City Thunder',
                  'Portland Trail Blazers','Utah Jazz','Golden State Warriors','LA Clippers','Los Angeles Lakers','Phoenix Suns',
                  'Sacramento Kings','Dallas Mavericks','Houston Rockets','Memphis Grizzlies','New Orleans Pelicans','San Antonio Spurs',
                  'All Star',

                  'EuroCup','FIBA','EuroLeague',

                 'Cedi Osman','Kobe Bryant','Smaç','Blok','Curry','LeBron James','Durant','Harden',
                'Doncic','Virtus Bologna','Virtus Pallacanestro Bologna','Kyrie Irving','Fenerbahçe Beko','euroleague']

        Soccer = ['LaLiga','Athletic Club','Athletico','Osasuna','Cadiz','Elche','Barcelona','Getafe','Girona','Vallecona',
              'Celta','Espanyol','Mallorca',
             'Betis','Real Madrid','Sociedad','Valladolid','Sevilla','Almeria','Valencia','Villarreal',
             'SERIE A','#SerieA','SerieA','Atalanta','Bologna','Cremonese','Empoli','Fiorentina','Verona','Inter',

              'Juventus','Lazio','Lecce','Milan','Monza',
           'Napoli','Roma','Salernitana','Sampdoria','Sassuolo','Spezia','Torino','Udinese',

             'EURO 2020','UEFA Nations League','#NationsLeague','2022 Dünya Kupası Avrupa Elemeleri',
             'Copa America 2021','Finalissima','Fenerbahçe',
              'Türkiye','Fransa','Arjantin','İspanya','İtalya','Portekiz','Almanya','Belçika','Galler','Hollanda','İngiltere',
              'Hazırlık Maçı',

             'Gol','Frikik','Karim Benzema','Robert Lewandowski','FRİKİK',
            'Vedat Muruqi','Burak Yilmaz','Skor','Haaland','Messi','Ronaldo','Hakan Çalhanoğlu','Jürgen Klopp','Ibrahimovic',
             'Zlatan Ibrahimović','Burak Yilmaz','Gareth Bale','De Gea','GOLÜ','Gol',
             'İlkay Gündoğan','Pep Guardiola','Jose Mourinho','Kevin De Bruyne','Paulo Dybala','Angel Di Maria',
             'Riyad Mahrez','Vinicius Junior']

        Tennis = ['Wimbledon','ATP','Djokovic','Federer','Nadal','Barcelona Open']

        Fighting = ['UFC','WWE',
                'Khabib','Conor McGregor','Gökhan Saki',
              'Rey Mysterio','Alexa','The Fiend','Randy','Undertaker','Cena','Roman Reigns','Goldberg','Anthony Joshua','Boks']

        Racing = ['MotoGP','Formula 2','Formula 1','Son Viraj','Cem Bölükbaşı','Hamilton','Verstappen','Perez','Valencia Grand Prix']

        for cat in Basketball:
            if cat.lower() in str(title).lower():
                return 'Basketball'

        for cat in Tennis:
            if cat.lower() in str(title).lower():
                return 'Tennis'

        for cat in Fighting:
            if cat.lower() in str(title).lower():
                return 'Fighting'

        for cat in Racing:
            if cat.lower() in str(title).lower():
                return 'Racing'

        if 'Altın Oran' in str(title):
            return 'Betting'

        for cat in Soccer:
            if cat.lower() in str(title).lower():
                return 'Soccer'

        if 'GP' in str(title):
            return 'Racing'


    df['Categories'] = df['Title'].apply(categorize)



    def subcategorize(title):

        LaLiga = ['LaLiga','Athletic Club','Athletico','Osasuna','Cadiz','Elche','Barcelona',
              'Getafe','Girona','Vallecona','Celta','Espanyol','Mallorca',
             'Betis','Real Madrid','Sociedad','Valladolid','Sevilla','Almeria','Valencia','Villarreal']

        SerieA=['SERIE A','#SerieA','SerieA','Atalanta','Bologna','Cremonese','Empoli','Fiorentina',
            'Verona','Inter','Juventus','Lazio','Lecce','Milan','Monza',
           'Napoli','Roma','Salernitana','Sampdoria','Sassuolo','Spezia','Torino','Udinese']

        International = ['EURO 2020','UEFA Nations League','#NationsLeague','2022 Dünya Kupası Avrupa Elemeleri',
                     'Copa America 2021','Finalissima','Fenerbahçe',
                    'Türkiye','Fransa','Arjantin','İspanya','İtalya','Portekiz','Almanya','Belçika','Galler','Hollanda','İngiltere',
                    'Hazırlık Maçı']

        Soccer_Highlights = ['Gol','Frikik','Karim Benzema','Robert Lewandowski','Burak Yilmaz','FRİKİK',
                         'Vedat Muruqi','Burak Yilmaz','Skor','Haaland','Messi','Ronaldo','Hakan Çalhanoğlu',
                        'Jürgen Klopp','Ibrahimovic','Zlatan Ibrahimović','Gareth Bale','De Gea','GOLÜ','Gol',
                        'İlkay Gündoğan','Pep Guardiola','Jose Mourinho','Kevin De Bruyne','Paulo Dybala','Angel Di Maria',
                        'Riyad Mahrez','Vinicius Junior']

        NBA = ['NBA','Boston Celtics','Brooklyn Nets','Philadelphia 76ers','Toronto Raptors','Chicago Bulls','New York Knicks',
                  'Cleveland Cavaliers','Detroit Pistons','Indiana Pacers','Milwaukee Bucks','Atlanta Hawks','Charlotte Hornets',
                  'Miami Heat','Orlando Magic','Washington Wizards','Denver Nuggets','Minnesota Timberwolves','Oklahoma City Thunder',
                  'Portland Trail Blazers','Utah Jazz','Golden State Warriors','LA Clippers','Los Angeles Lakers','Phoenix Suns',
                  'Sacramento Kings','Dallas Mavericks','Houston Rockets','Memphis Grizzlies','New Orleans Pelicans','San Antonio Spurs',
          'All Star']

        European_Basketball = ['EuroCup','FIBA','EuroLeague']

        Basketball_Highlights = ['Cedi Osman','Kobe Bryant','Smaç','Blok','Curry','LeBron James','Durant','Harden',
                             'Doncic','Virtus Bologna','Virtus Pallacanestro Bologna','Kyrie Irving','Fenerbahçe Beko']


        Racing_Highlights = ['Cem Bölükbaşı','Hamilton','Verstappen','Perez','Valencia Grand Prix']

        Tennis_Highlights = ['Djokovic','Federer','Nadal','Barcelona Open']

        Fighting_Highlights = ['Khabib','Conor McGregor','Gökhan Saki',
                          'Rey Mysterio','Alexa','The Fiend','Randy','Undertaker','Cena','Roman Reigns','Goldberg',
                           'Anthony Joshua','Boks']

        #Other
        if 'Altın Oran'.lower() in str(title).lower():
            return 'Betting'

        #Tennis
        if 'Wimbledon'.lower() in str(title).lower():
            return 'Wimbledon'

        if 'ATP'.lower() in str(title).lower():
            return 'ATP'



        #Racing
        if 'MotoGP'.lower() in str(title).lower():
            return 'MotoGP'

        if 'Formula 2'.lower() in str(title).lower():
            return 'Formula 2'

        if 'Formula 1'.lower() in str(title).lower():
            return 'Formula 1'

        if 'Son Viraj'.lower() in str(title).lower():
            return 'Son Viraj'

        for cat in Racing_Highlights:
            if cat.lower() in str(title).lower():
                return 'Racing_Highlights'

        if 'GP' in str(title):
            return 'Racing_Highlights'

        #Fighting
        if 'UFC'.lower() in str(title).lower():
            return 'UFC'

        if 'WWE'.lower() in str(title).lower():
            return 'WWE'

        for cat in Fighting_Highlights:
            if cat.lower() in str(title).lower():
                return 'Fighting_Highlights'

        #Basketball
        for cat in NBA:
            if cat.lower() in str(title).lower():
                return 'NBA'

        for cat in European_Basketball:
            if cat.lower() in str(title).lower():
                return 'European_Basketball'

        for cat in Basketball_Highlights:
            if cat.lower() in str(title).lower():
                return 'Basketball_Highlights'

        for cat in Tennis_Highlights:
            if cat.lower() in str(title).lower():
                return 'Tennis_Highlights'

        #Soccer
        for cat in LaLiga:
            if cat.lower() in str(title).lower():
                return 'LaLiga'

        for cat in SerieA:
            if cat.lower() in str(title).lower():
                return 'SerieA'

        for cat in International:
            if cat.lower() in str(title).lower():
                return 'International'

        for cat in Soccer_Highlights:
            if cat.lower() in str(title).lower():
                return 'Soccer_Highlights'

    df['SubCategory'] = df['Title'].apply(subcategorize)


    return df

def drop_na(df):
    return df.dropna()

def duration_convert(df):
    def convert_YouTube_duration_to_seconds(duration):
        day_time = duration.split('T')
        day_duration = day_time[0].replace('P', '')
        day_list = day_duration.split('D')
        if len(day_list) == 2:
            day = int(day_list[0]) * 60 * 60 * 24
            day_list = day_list[1]
        else:
            day = 0
            day_list = day_list[0]
        hour_list = day_time[1].split('H')
        if len(hour_list) == 2:
            hour = int(hour_list[0]) * 60 * 60
            hour_list = hour_list[1]
        else:
            hour = 0
            hour_list = hour_list[0]
        minute_list = hour_list.split('M')
        if len(minute_list) == 2:
            minute = int(minute_list[0]) * 60
            minute_list = minute_list[1]
        else:
            minute = 0
            minute_list = minute_list[0]
        second_list = minute_list.split('S')
        if len(second_list) == 2:
            second = int(second_list[0])
        else:
            second = 0
        return day + hour + minute + second

    df['DurationinSeconds'] = df['Duration'].apply(convert_YouTube_duration_to_seconds)
    return df

def date_convert(df):
    df['Date'] = df['Published_date'].apply(lambda x:x.split('T')[0])
    return df

def year_convert(df):
    df['Year'] = df['Date'].apply(lambda x:x.split('-')[0])
    return df

def video_age(df):
    def daysdiff(time):
        year = time.split('-')[0]
        month = time.split('-')[1]
        day = time.split('-')[2]

        d = date.today() - date(int(year),int(month),int(day))

        return d.days
    df['Age'] = df['Date'].apply(daysdiff)
    return df

def type_convert(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Categories'] = df['Categories'].astype('category')
    df['SubCategory'] = df['SubCategory'].astype('category')
    df['Year'] = df['Year'].astype('category')

    return df

def fe_data(df):
    df_cleaned = (df.
                  pipe(copy_df).
                  pipe(feature_extraction).
                  pipe(drop_na).
                  pipe(duration_convert).
                  pipe(date_convert).
                  pipe(year_convert).
                  pipe(video_age).
                  pipe(type_convert)
                 )
    return df_cleaned
