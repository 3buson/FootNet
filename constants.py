__author__ = 'matic'

# --- DATABASE --- #
databaseString = 'DRIVER={SQL Server};SERVER=localhost;DATABASE=footballnetwork;UID=root;PWD=renault93'

# --- LEAGUES --- #
leagues                = dict()
leagues['england']     = 'PremierLeague'
leagues['spain']       = 'LaLiga'
leagues['germany']     = 'Bundesliga'
leagues['italy']       = 'SerieA'
leagues['france']      = 'Ligue1'
leagues['portugal']    = 'PrimeraLiga'
leagues['netherlands'] = 'Eredevisie'
leagues['belgium']     = 'ProLeague'
leagues['scotland']    = 'Premiership'
leagues['russia']      = 'PremierLeagueRussia'
leagues['ukraine']     = 'PremierLeagueUkraine'
leagues['switzerland'] = 'SuperLeague'
leagues['turkey']      = 'SuperLig'
leagues['USA']         = 'MajorLeagueSoccer'


# --- SEASONS --- #
seasons = dict()
seasons[2015] = '15'
seasons[2014] = '14'
seasons[2013] = '13'
seasons[2012] = '12'
seasons[2011] = '11'
seasons[2010] = '10'
seasons[2009] = '09'
seasons[2008] = '08'
seasons[2007] = '07'
seasons[2006] = '06'
seasons[2005] = '05'
seasons[2004] = '04'
seasons[2003] = '03'
seasons[2002] = '02'
seasons[2001] = '01'
seasons[2000] = '00'


# --- CLUBS --- #

# SPANISH LA LIGA
clubDictESP         = dict()
clubDictESP['RMA']  = 418   # Real Madrid
clubDictESP['FCB']  = 131   # Barcelona
clubDictESP['ATM']  = 13    # Atletico Madrid
clubDictESP['VCF']  = 1049  # Valencia
clubDictESP['SEV']  = 368   # Sevilla
clubDictESP['ATH']  = 621   # Athletic Bilbao
clubDictESP['VIL']  = 1050  # Villareal
clubDictESP['RSC']  = 681   # Real Sociedad
clubDictESP['CVCF'] = 418   # Celta vigo
clubDictESP['ESP']  = 714   # Espanyol
clubDictESP['GRCF'] = 16795 # Granada
clubDictESP['DLC']  = 897   # Deportivo la Coruna
clubDictESP['MCF']  = 1084  # Malaga
clubDictESP['RBCF'] = 150   # Betis
clubDictESP['GECF'] = 3709  # Getafe
clubDictESP['LCF']  = 3368  # Levante
clubDictESP['RVCF'] = 367   # Rayo Vallecano
clubDictESP['SGCF'] = 2448  # Sporting Gijon
clubDictESP['ECF']  = 1533  # Eibar
clubDictESP['LPCF'] = 472   # Las Palmas

# ENGLISH PREMIER LEAGUE
clubDictENG          = dict()
clubDictENG['MCFC']  = 281	 # Manchester City
clubDictENG['LCFC']  = 1003  # Leicester
clubDictENG['CFC']   = 631	 # Chelsea
clubDictENG['AFC']   = 11    # Arsenal
clubDictENG['MUTD']  = 985	 # Manchester united
clubDictENG['TOT']   = 148	 # Tottenham Hotspur
clubDictENG['LFC']   = 31    # Liverpool
clubDictENG['SFC']   = 180	 # Southampton
clubDictENG['SCFC']  = 2288	 # Swansea City
clubDictENG['STC']   = 512	 # Stoke City
clubDictENG['CPFC']  = 873	 # Crystal Palace
clubDictENG['EFC']   = 29    # Everton
clubDictENG['WHUFC'] = 379	 # West Hame United
clubDictENG['WBFC']  = 984	 # West Bromwich Albion
clubDictENG['NUFC']  = 762	 # Newcastle United
clubDictENG['SUFC']  = 289	 # Sunderland
clubDictENG['AVFC']  = 405	 # Aston Villa
clubDictENG['ABFC']  = 989	 # AFC Bournemouth
clubDictENG['WFC']   = 1010	 # Watford
clubDictENG['NFC']   = 1123	 # Norwich