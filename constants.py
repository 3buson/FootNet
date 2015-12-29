__author__ = 'matic'

import utils

# --- VARIOUS CONSTANTS --- #
currentSeason = '15'

# --- DATABASE --- #
databaseString = 'DRIVER={MySQL};SERVER=localhost;DATABASE=footballnetwork;UID=root;PWD=*****'


# --- COUNTRIES DICTIONARY --- #
countriesDict = utils.getCountriesDics()


# --- LEAGUES --- #
leagues                = dict()
leagues['England']     = 'PremierLeague'
leagues['Spain']       = 'LaLiga'
leagues['Germany']     = 'Bundesliga'
leagues['Italy']       = 'SerieA'
leagues['France']      = 'Ligue1'
leagues['Portugal']    = 'PrimeraLiga'
leagues['Netherlands'] = 'Eredevisie'
leagues['Belgium']     = 'ProLeague'
leagues['Scotland']    = 'Premiership'
leagues['Russia']      = 'PremierLeagueRussia'
leagues['Ukraine']     = 'PremierLeagueUkraine'
leagues['Switzerland'] = 'SuperLeague'
leagues['Turkey']      = 'SuperLig'
leagues['USA']         = 'MajorLeagueSoccer'


leagueIds                         = dict()
leagueIds['PremierLeague']        = 1
leagueIds['LaLiga']               = 2
leagueIds['Bundesliga']           = 3
leagueIds['SerieA']               = 4
leagueIds['Ligue1']               = 5
leagueIds['PrimerLiga']           = 6
leagueIds['Eredevisie']           = 7
leagueIds['ProLeague']            = 8
leagueIds['Premiership']          = 9
leagueIds['PremierLeagueRussia']  = 10
leagueIds['PremierLeagueUkraine'] = 11
leagueIds['SuperLeague']          = 12
leagueIds['SuperLig']             = 13
leagueIds['MajorLeagueSoccer']    = 14


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
clubDictESP['CVCF'] = 940   # Celta vigo
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

# GERMAN BUNDESLIGA 1
clubDictGER         = dict()
clubDictGER['BMU']  = 27    # Bayern Munich
clubDictGER['BDO']  = 16    # Borussia Dortmund
clubDictGER['BLE']  = 15    # Bayer 04 Leverkusen
clubDictGER['VFLW'] = 82    # VFL Wolfsburg
clubDictGER['FCS']  = 33    # FC Schalke 04
clubDictGER['BMG']  = 18    # Borussia Monchengladbach
clubDictGER['TSGH'] = 533   # TSG 1899 Hoffenheim
clubDictGER['EFR']  = 24    # Eintracht Frankfurt
clubDictGER['VFBS'] = 79    # VFB Stuttgart
clubDictGER['HBSC'] = 44    # Hertha BSC
clubDictGER['HAN']  = 42    # Hannover 96
clubDictGER['FSVM'] = 39    # 1.FSV Mainz 05
clubDictGER['FCK']  = 3     # 1.FC Koln
clubDictGER['HAM']  = 41    # Hamburger SV
clubDictGER['FCA']  = 167   # FC Augsburg
clubDictGER['WEB']  = 86    # SV Werder Bremen
clubDictGER['FCI']  = 4795  # FC Ingolstadt 04
clubDictGER['SVD']  = 105   # SV Darmstadt 98

# FRENCH LIGUE 1
clubDictFRA         = dict()
clubDictFRA['PSG']  = 583   # Paris Saint-Germain
clubDictFRA['OLY']  = 1041  # Olympique Lyon
clubDictFRA['ASM']  = 162   # AS Monaco
clubDictFRA['OMA']  = 244   # Olympique Marseille
clubDictFRA['ASE']  = 618   # AS Saint-Etienne
clubDictFRA['SRE']  = 273   # Stade Rennais FC
clubDictFRA['GIB']  = 40    # FC Girondins Bordeaux
clubDictFRA['LOL']  = 1082  # Losc Lille
clubDictFRA['ONI']  = 417   # OGC Nice
clubDictFRA['FCT']  = 415   # FC Toulouse
clubDictFRA['FCL']  = 1158  # FC Lorient
clubDictFRA['HSCM'] = 969   # HSC Montpellier
clubDictFRA['SRE']  = 1421  # Stade Reims
clubDictFRA['FCN']  = 995   # FC Nantes
clubDictFRA['EAG']  = 855   # EA Guingamp
clubDictFRA['EST']  = 1095  # ES Troyes AC
clubDictFRA['SMC']  = 1162  # SM Caen
clubDictFRA['SCB']  = 595   # SC Bastia
clubDictFRA['SCOA'] = 1420  # SCO Angers
clubDictFRA['GFCA'] = 3558  # GFC Aiaccio

# ITALIAN SERIE A
clubDictITA         = dict()
clubDictITA['JUV']  = 506   # Juventus FC
clubDictITA['NAP']  = 6195  # SSC Napoli
clubDictITA['ASR']  = 12    # AS Roma
clubDictITA['IMI']  = 46    # Inter Milan
clubDictITA['ACM']  = 5     # AC Milan
clubDictITA['SSL']  = 398   # SS Lazio
clubDictITA['FIO']  = 430   # ACF Fiorentina
clubDictITA['UCS']  = 1038  # UC Sampdoria
clubDictITA['GEN']  = 252   # Genoa CFC
clubDictITA['UDC']  = 410   # Udinese Calcio
clubDictITA['USS']  = 6574  # US Sassuolo
clubDictITA['TOR']  = 416   # Torino FC
clubDictITA['BOL']  = 1025  # Bologna FC 1909
clubDictITA['ATA']  = 800   # Atalanta BC
clubDictITA['USP']  = 458   # US Palermo
clubDictITA['FCE']  = 749   # FC Empoli
clubDictITA['CAP']  = 4102  # Capri FC 1909
clubDictITA['HEV']  = 276   # Hellas Verona
clubDictITA['CHV']  = 862   # Chievo Verona
clubDictITA['FRC']  = 8970  # Frosinone Calcio

# PORTUGUESE PRIMERA LIGA
clubDictPOR        = dict()
clubDictPOR['FCP'] = 720   # FC Porto
clubDictPOR['SPO'] = 336   # Sporting CP
clubDictPOR['SLB'] = 294   # SL Benfica
clubDictPOR['SCB'] = 1075  # SC Braga
clubDictPOR['VGU'] = 2420  # Vitoria Guimaraes SC
clubDictPOR['RIA'] = 2425  # Rio Ave FC
clubDictPOR['BEL'] = 2457  # CF Belenenses Lissabon
clubDictPOR['CSM'] = 1301  # CS Maritimo
clubDictPOR['CDN'] = 982   # CD Nacional
clubDictPOR['GDE'] = 1465  # GD Estorilpraia
clubDictPOR['PAC'] = 2995  # FC Pacos De Ferreira
clubDictPOR['FCA'] = 8024  # FC Arouca
clubDictPOR['ACC'] = 2990  # Academica Coimbra
clubDictPOR['BOA'] = 2503  # Boavista Porto FC
clubDictPOR['VIS'] = 1085  # Vitoria Setubal FC
clubDictPOR['MFC'] = 979   # Moreirense FC
clubDictPOR['CDT'] = 7179  # CD Tondela
clubDictPOR['UNM'] = 976   # CF Uniao Madeira

# NETHERLANDS EREDIVISE
clubDictNED        = dict()
clubDictNED['PSV'] = 383   # PSV Eindhoven
clubDictNED['AJA'] = 610   # AJAX Amsterdam
clubDictNED['FEY'] = 234   # Feyenoord Rotterdam
clubDictNED['AZA'] = 1090  # AZ Alkmaar
clubDictNED['FCT'] = 317   # FC Twente
clubDictNED['VIT'] = 499   # Vitesse Arnhem
clubDictNED['GRO'] = 202   # FC Groningen
clubDictNED['HEE'] = 306   # SC Heerenveen
clubDictNED['UTR'] = 200   # FC Utrecht
clubDictNED['WIL'] = 403   # Willem II Tilburg
clubDictNED['ZWO'] = 1269  # PEC Zwoole
clubDictNED['ADH'] = 1268  # ADO Den Haag
clubDictNED['NEC'] = 467   # NEC Nijmegen
clubDictNED['HER'] = 1304  # Heracles Almelo
clubDictNED['SCC'] = 133   # SC Cambuur-Leeuwarden
clubDictNED['ROD'] = 192   # Roda JC Kerkrade
clubDictNED['EXC'] = 798   # Excelsior Rotterdam
clubDictNED['DGR'] = 642   # De Graafschap Doetinchem

# BELGIAM JUPILER PRO LEAGUE
clubDictBEL        = dict()
clubDictBEL['AND'] = 58     # RSC Anderlecht
clubDictBEL['BRU'] = 2282   # CLUB Brugge KV
clubDictBEL['GEN'] = 157    # KAA Gent
clubDictBEL['GNK'] = 1184   # KRC Genk
clubDictBEL['STL'] = 3057   # Standard Liege
clubDictBEL['OOS'] = 2861   # KV Oostende
clubDictBEL['MEC'] = 354    # KV Mechelen
clubDictBEL['LOK'] = 498    # KSC Lokeren
clubDictBEL['ZUL'] = 3508   # SV Zulte Waregem
clubDictBEL['TRU'] = 475    # Sint-Truidense VV
clubDictBEL['KOR'] = 601    # KV Kortrijk
clubDictBEL['MOU'] = 29228  # Mouscron-Preuwelz
clubDictBEL['CHA'] = 172    # RSC Charleroi
clubDictBEL['WES'] = 968    # KVC Westerlo
clubDictBEL['HEV'] = 2727   # OUD-Heverlee Luever
clubDictBEL['WAA'] = 28643  # Waasland-Beveren

# SCOTTISH PREMIERSHIP
clubDictSCO        = dict()
clubDictSCO['CEL'] = 371   # Celtic FC
clubDictSCO['ABE'] = 370   # Aberdeen FC
clubDictSCO['HOM'] = 43    # Heart of Midlothian FC
clubDictSCO['STI'] = 2578  # St. Iohnstone FC
clubDictSCO['DUN'] = 1519  # Dundee United FC
clubDictSCO['ROC'] = 2759  # Ross County FC
clubDictSCO['MOW'] = 987   # Motherwell FC
clubDictSCO['ICT'] = 2451  # Inverness Caledonian Thistle FC
clubDictSCO['KIL'] = 2553  # Kilmarnock FC
clubDictSCO['HAM'] = 2999  # Hamilton Academical FC
clubDictSCO['DFC'] = 511   # Dundee FC
clubDictSCO['PAR'] = 2760  # Patrick Thistle FC
clubDictSCO['RAN'] = 124   # Rangers FC

# RUSSIAN PREMIERLEAGUE
clubDictRUS        = dict()
clubDictRUS['ZSP'] = 964    # Zenit St. Petersburg
clubDictRUS['MOS'] = 2410   # CSKA Moscow
clubDictRUS['FKK'] = 16704  # FK Krasnodar
clubDictRUS['SPA'] = 232    # Spartak Moscow
clubDictRUS['LOK'] = 932    # Lokomotiv Moscow
clubDictRUS['DIN'] = 121    # Dinamo Moscow
clubDictRUS['RUK'] = 2698   # Rubin Kazan
clubDictRUS['KUK'] = 2439   # Kuban Krasnodar
clubDictRUS['TEG'] = 3725   # Terek Grozny
clubDictRUS['KSS'] = 2696   # Krylya Sovetov Samara
clubDictRUS['ANM'] = 2700   # Anzhi Makhachkala
clubDictRUS['FKR'] = 1083   # FK Rostov
clubDictRUS['USO'] = 11127  # Ural Scerdlovskaya Oblast
clubDictRUS['MOR'] = 11126  # Mordovia Saransk
clubDictRUS['UFA'] = 28095  # FK UFA
clubDictRUS['AMP'] = 4128   # Amkar Perm

# UKRANIAN PREMIERLEAGUE
clubDictUKR        = dict()
clubDictUKR['SHD'] = 660    # Shakhtar Donersk
clubDictUKR['DYK'] = 338    # Dynamo Kyiv
clubDictUKR['DND'] = 339    # Dnipro Dnipropetrovsk
clubDictUKR['ZOL'] = 10690  # Zorya Lugansk
clubDictUKR['VOP'] = 2740   # Vorskla Poltava
clubDictUKR['VOL'] = 4482   # Volyn Lutsk
clubDictUKR['MEK'] = 6414   # Metalist Kharkiv
clubDictUKR['KAL'] = 2477   # Karpaty Lviv
clubDictUKR['STD'] = 16247  # Stal Dniprodzerzhynsk
clubDictUKR['OLI'] = 23611  # Olimpik Donetsk
clubDictUKR['CHO'] = 6992   # Chornomorets Odessa
clubDictUKR['FKO'] = 18303  # FK Oleksandria
clubDictUKR['GOU'] = 6996   # Goverla Uzhgorod
clubDictUKR['MEZ'] = 6994   # Metalurg Zaporizhya

# SWISS SUPER LEAGUE
clubDictSWI        = dict()
clubDictSWI['FCB'] = 26    # FC Basel 1893
clubDictSWI['YUB'] = 452   # BSC Young Boys
clubDictSWI['FCS'] = 321   # FC Sion
clubDictSWI['GCZ'] = 504   # Grasshopper Club Zurich
clubDictSWI['FCZ'] = 260   # FC Zurich
clubDictSWI['FCL'] = 434   # FC Luzern
clubDictSWI['STG'] = 257   # FC St. Gallen
clubDictSWI['FCT'] = 938   # FC Thun
clubDictSWI['FCV'] = 163   # FC Vaduz
clubDictSWI['LUG'] = 2790  # FC Lugano

# TURKISH SUPER LIG
clubDictTUR = dict()
clubDictTUR['FEN'] = 36     # Fenerbahce SK
clubDictTUR['BES'] = 114    # Besiktas JK
clubDictTUR['GAL'] = 141    # Galatasaray SK
clubDictTUR['TRA'] = 449    # Trabzonspor
clubDictTUR['BUR'] = 20     # Bursaspor
clubDictTUR['MED'] = 6890   # Medipol Basaksheir
clubDictTUR['KAS'] = 10484  # Kasimpasa
clubDictTUR['OSM'] = 2944   # Osmanlispor FK
clubDictTUR['GEN'] = 820    # Genclerbirligi Ankara
clubDictTUR['SIV'] = 2381   # Medicana Sivasspor
clubDictTUR['ANT'] = 589    # Antalyaspor
clubDictTUR['ESK'] = 825    # Eskisehirspor
clubDictTUR['KON'] = 2293   # Torku Konyaspor
clubDictTUR['RIZ'] = 126    # Caykur Rizespor
clubDictTUR['GAZ'] = 524    # Gaziantepspor
clubDictTUR['KAY'] = 3205   # Kayserispor
clubDictTUR['AKH'] = 19771  # Akhisar Belediye Genclik VE SPOR
clubDictTUR['MER'] = 3216   # Mersin Idmanyurdu

# USA MAJOR LEAGUE SOCCER
clubDictUSA        = dict()
clubDictUSA['TOR'] = 11141  # Toronto FC
clubDictUSA['LAG'] = 1061   # Los Angeles Galaxy
clubDictUSA['NYC'] = 40058  # New York City FC
clubDictUSA['SES'] = 9636   # Seattle Soundres FC
clubDictUSA['COC'] = 813    # Columbus Crew SC
clubDictUSA['ORC'] = 45604  # Orlando City SC
clubDictUSA['COR'] = 1247   # Colorado Rapids
clubDictUSA['MON'] = 4078   # Montreal Impact
clubDictUSA['POT'] = 4291   # Portland Timbers
clubDictUSA['SKC'] = 4284   # Sporting Kansas City
clubDictUSA['NER'] = 626    # New England Revolution
clubDictUSA['NYR'] = 623    # New York Red Bulls
clubDictUSA['HOD'] = 9168   # Houston Dynamo
clubDictUSA['RSL'] = 6643   # Real Salt Lake City
clubDictUSA['PHU'] = 25467  # Philadelphia Union
clubDictUSA['SJE'] = 218    # San Jose Earthquakes
clubDictUSA['FCD'] = 8816   # FC Dallas
clubDictUSA['DCU'] = 2440   # D.C. United
clubDictUSA['VAW'] = 6321   # Vancouver Whitecaps
clubDictUSA['CHF'] = 432    # Chicago Fire

# GREEK SUPER LEAGUE
clubDictGRE        = dict()
clubDictGRE['OLY'] = 683    # Olympiacos Piraeus
clubDictGRE['PAO'] = 1091   # PAOK Thessaloniki
clubDictGRE['PAN'] = 265    # Panathinaikos Athens
clubDictGRE['AEK'] = 2441   # AEK Athens
clubDictGRE['AST'] = 6676   # Asteras Tripolis
clubDictGRE['ATR'] = 3060   # Atromitos Athen
clubDictGRE['PAS'] = 2671   # PAS Giannina
clubDictGRE['SKO'] = 128    # Skoda Xanthi
clubDictGRE['AGR'] = 6418   # Panetolikos Agrinio
clubDictGRE['PLA'] = 21957  # Platanias Chania
clubDictGRE['PAE'] = 2079   # PAE Veria
clubDictGRE['ATH'] = 169    # Panionios Athens
clubDictGRE['AEL'] = 28956  # AEL Kalloni
clubDictGRE['IRA'] = 47     # Iraklis Thessaloniki
clubDictGRE['KOM'] = 7185   # Panthrakikos Komotini
clubDictGRE['APO'] = 2672   # APO Levadiakos


# DICT OF CLUB DICTS
clubs                         = dict()
clubs['PremierLeague']        = clubDictENG
clubs['LaLiga']               = clubDictESP
clubs['Bundesliga']           = clubDictGER
clubs['SerieA']               = clubDictITA
clubs['Ligue1']               = clubDictFRA
clubs['PrimeraLiga']          = clubDictPOR
clubs['Eredevisie']           = clubDictNED
clubs['ProLeague']            = clubDictBEL
clubs['Premiership']          = clubDictSCO
clubs['PremierLeagueRussia']  = clubDictRUS
clubs['PremierLeagueUkraine'] = clubDictUKR
clubs['SuperLeague']          = clubDictSWI
clubs['SuperLig']             = clubDictTUR
clubs['MajorLeagueSoccer']    = clubDictUSA
clubs['SuperLeagueGreece']    = clubDictGRE