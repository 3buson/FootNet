__author__ = 'matic'


# --- VARIOUS CONSTANTS --- #
currentSeason       = '15'
inflationRatio      = 2.11
perspectiveAge      = 18
noRankingPenalty    = 25
noWeightPathPenalty = 1000
defaultClubWeight   = 0.1
allSeasonsString    = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
allLeaguesString    = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 '

# --- DATABASE --- #
databaseString = 'DRIVER={MySQL};SERVER=localhost;DATABASE=footballnetwork;UID=root;PWD=*****'

# --- LEAGUE RANKINGS --- #
leagueRankings     = dict()
leagueRankings[1]  = 95
leagueRankings[2]  = 100
leagueRankings[3]  = 75
leagueRankings[4]  = 85
leagueRankings[5]  = 50
leagueRankings[6]  = 40
leagueRankings[7]  = 40
leagueRankings[8]  = 25
leagueRankings[9]  = 20
leagueRankings[10] = 25
leagueRankings[11] = 20
leagueRankings[12] = 20
leagueRankings[13] = 15
leagueRankings[14] = 5
leagueRankings[15] = 13
leagueRankings[16] = 20
leagueRankings[17] = 15
leagueRankings[18] = 12
leagueRankings[19] = 10
leagueRankings[20] = 10
leagueRankings[21] = 10
leagueRankings[22] = 10
leagueRankings[23] = 15
leagueRankings[24] = 13
leagueRankings[25] = 13
leagueRankings[26] = 10


# --- LEAGUES --- #
leagues                = dict()
leagues['England']     = 'PremierLeague'
leagues['Spain']       = 'LaLiga'
leagues['Germany']     = 'Bundesliga'
leagues['Italy']       = 'SerieA'
leagues['France']      = 'Ligue1'
leagues['Portugal']    = 'PrimeraLiga'
leagues['Netherlands'] = 'Eredivisie'
leagues['Belgium']     = 'ProLeague'
leagues['Scotland']    = 'Premiership'
leagues['Russia']      = 'PremierLeagueRussia'
leagues['Ukraine']     = 'PremierLeagueUkraine'
leagues['Switzerland'] = 'SuperLeague'
leagues['Turkey']      = 'SuperLig'
leagues['USA']         = 'MajorLeagueSoccer'
leagues['Greece']      = 'SuperLeagueGreece'
leagues['Brazil']      = 'SerieABrazil'
leagues['Argentina']   = 'TorneoInicial'
leagues['Romania']     = 'Liga1'
leagues['Croatia']     = 'HNL1'
leagues['Austria']     = 'BundesligaAustria'
leagues['Czech']       = 'SynotLiga'
leagues['Denmark']     = 'AlkaSuperligaen'
leagues['England2']    = 'Championship'
leagues['Spain2']      = 'SegundaDivision'
leagues['Germany2']    = 'Bundesliga2'
leagues['Italy2']      = 'SerieB'


leagueIds                         = dict()
leagueIds['PremierLeague']        = 1
leagueIds['LaLiga']               = 2
leagueIds['Bundesliga']           = 3
leagueIds['SerieA']               = 4
leagueIds['Ligue1']               = 5
leagueIds['PrimeraLiga']          = 6
leagueIds['Eredivisie']           = 7
leagueIds['ProLeague']            = 8
leagueIds['Premiership']          = 9
leagueIds['PremierLeagueRussia']  = 10
leagueIds['PremierLeagueUkraine'] = 11
leagueIds['SuperLeague']          = 12
leagueIds['SuperLig']             = 13
leagueIds['MajorLeagueSoccer']    = 14
leagueIds['SuperLeagueGreece']    = 15
leagueIds['SerieABrazil']         = 16
leagueIds['TorneoInicial']        = 17
leagueIds['Liga1']                = 18
leagueIds['HNL1']                 = 19
leagueIds['BundesligaAustria']    = 20
leagueIds['SynotLiga']            = 21
leagueIds['AlkaSuperligaen']      = 22
leagueIds['Championship']         = 23
leagueIds['SegundaDivision']      = 24
leagueIds['Bundesliga2']          = 25
leagueIds['SerieB']               = 26


leagueURLIds         = dict()
leagueURLIds['ROM']  = 'RO1'
leagueURLIds['CRO']  = 'KR1'
leagueURLIds['AUT']  = 'A1'
leagueURLIds['CZE']  = 'TS1'
leagueURLIds['DEN']  = 'DK1'
leagueURLIds['SRB']  = 'SER1'
leagueURLIds['ENG2'] = 'GB2'
leagueURLIds['ESP2'] = 'ES2'
leagueURLIds['GER2'] = 'L2'
leagueURLIds['ITA2'] = 'IT2'


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
clubDictESP['RMA']  = 418    # Real Madrid
clubDictESP['FCB']  = 131    # Barcelona
clubDictESP['ATM']  = 13     # Atletico Madrid
clubDictESP['VCF']  = 1049   # Valencia
clubDictESP['SEV']  = 368    # Sevilla
clubDictESP['ATH']  = 621    # Athletic Bilbao
clubDictESP['VIL']  = 1050   # Villareal
clubDictESP['RSC']  = 681    # Real Sociedad
clubDictESP['CVCF'] = 940    # Celta vigo
clubDictESP['ESP']  = 714    # Espanyol
clubDictESP['GRCF'] = 16795  # Granada
clubDictESP['DLC']  = 897    # Deportivo la Coruna
clubDictESP['MCF']  = 1084   # Malaga
clubDictESP['RBCF'] = 150    # Betis
clubDictESP['GECF'] = 3709   # Getafe
clubDictESP['LCF']  = 3368   # Levante
clubDictESP['RVCF'] = 367    # Rayo Vallecano
clubDictESP['SGCF'] = 2448   # Sporting Gijon
clubDictESP['ECF']  = 1533   # Eibar
clubDictESP['LPCF'] = 472    # Las Palmas

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

# DUTCH EREDIVISIE
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

# BRAZILIAN SERIE A
clubDictBRA        = dict()
clubDictBRA['COR'] = 199    # Sport Club Corinthians Paulista
clubDictBRA['PAL'] = 1023   # Sociedade Esportiva Palmeiras
clubDictBRA['CRU'] = 609    # Cruzeiro Esporte Clube
clubDictBRA['MIN'] = 330    # Clube Atletico Mineiro
clubDictBRA['FLU'] = 2462   # Fluminense Football Club
clubDictBRA['INT'] = 6600   # Sport Club Internacional
clubDictBRA['SAO'] = 585    # Sao Paulo Futebol Clube
clubDictBRA['GRE'] = 210    # Gremio Foot-Ball Porto Alegrense
clubDictBRA['SAN'] = 221    # Santos FC
clubDictBRA['FLA'] = 614    # Clube de Regatas do Flamengo
clubDictBRA['PAR'] = 679    # Atletico Paranaense
clubDictBRA['COT'] = 776    # Coritiba Foot Ball Club
clubDictBRA['FIG'] = 4064   # Figueirense Futebol Clube
clubDictBRA['REC'] = 8718   # Sport Club do Recife
clubDictBRA['BOT'] = 537    # Botafogo de Futebol e Regatas
clubDictBRA['PON'] = 1134   # Associacao Atletica Ponte Preta
clubDictBRA['VIT'] = 2125   # Esporte Clube Vitoria
clubDictBRA['CHA'] = 17776  # Associacao Chapecoense de Futebol
clubDictBRA['AME'] = 2863   # America Futebol Clube (MG)
clubDictBRA['SCR'] = 1785   # Santa Cruz Futebol Clube (PE)

# ARGENTINIAN TORNEO INICIAL
clubDictARG        = dict()
clubDictARG['BOC'] = 189    # Club Atletico Boca Juniors
clubDictARG['SLO'] = 1775   # Club Atletico San Lorenzo de Almagro
clubDictARG['RPL'] = 209    # Club Atletico River Plate
clubDictARG['NOB'] = 1286   # Club Atletico Newell's Old Boys
clubDictARG['EST'] = 288    # Estudiantes de La Plata
clubDictARG['AVS'] = 1029   # Club Atletico Velez Sarsfield
clubDictARG['LAN'] = 333    # Club Atletico Lanus
clubDictARG['RAC'] = 1444   # Racing Club de Avellaneda
clubDictARG['ROS'] = 1418   # Club Atletico Rosario Central
clubDictARG['ATI'] = 11831  # Club Atletico Tigre
clubDictARG['ARS'] = 4673   # Arsenal de Sarandi FC
clubDictARG['QUI'] = 1826   # Quilmes Atletico Club
clubDictARG['BAN'] = 830    # Club Atletico Banfield
clubDictARG['DEP'] = 12574  # Club Deportivo Godoy Cruz
clubDictARG['IND'] = 1234   # CA Independiente de Avellaneda
clubDictARG['RAF'] = 10233  # Atletice de Rafaela
clubDictARG['COR'] = 2417   # Belgrano de Cordoba
clubDictARG['BLA'] = 7468   # Olimpo de Bahia Blanca
clubDictARG['JUS'] = 2402   # Debensa Y Justicia
clubDictARG['ESG'] = 1106   # Club de Gimnasia Y Esgrima La PLata

# SERBIAN SUPERLIGA
clubDictSRB       = dict()
clubDictSRB['FKPA'] = 669    # FK Partizan Belgrade
clubDictSRB['REDS'] = 159    # Red Star Belgrade
clubDictSRB['FKVO'] = 448    # FK Vojvodina
clubDictSRB['FKCU'] = 6621   # FK Cukaricki
clubDictSRB['OFKB'] = 53     # OFK Beograd
clubDictSRB['MLAD'] = 6622   # Mladost Lucani
clubDictSRB['FKRA'] = 902    # FK Rad
clubDictSRB['RNIS'] = 7567   # FK Radnicki Nis
clubDictSRB['FKBO'] = 2209   # FK Borac Cacak
clubDictSRB['FKVO'] = 4634   # FK Vozdovac
clubDictSRB['JAGO'] = 12132  # FK Jagodina
clubDictSRB['FKSP'] = 15276  # FK Spartak Subotica
clubDictSRB['FKNO'] = 4633   # FK Novi Pazar
clubDictSRB['SURD'] = 33328  # FK Radnik Surdulica
clubDictSRB['JAVO'] = 8819   # FK Javor Ivanjica
clubDictSRB['FKME'] = 12135  # FK Metalac Gornji Milanovac

# ROMANIAN LIGA 1
clubDictROM       = dict()
clubDictROM['STEA'] = 301    # Steaua Bucharest
clubDictROM['ASTR'] = 13499  # Astra Giurgiu
clubDictROM['DINA'] = 312    # Dinamo Bukarest
clubDictROM['FCVI'] = 29831  # FC Viitorul
clubDictROM['CSUC'] = 40812  # CS U Craiova
clubDictROM['ASAT'] = 16650  # ASA Tirgu Mures
clubDictROM['PAND'] = 8715   # Pandurii Targu Jiu
clubDictROM['CFRC'] = 7769   # CFR Cluj
clubDictROM['FCBO'] = 8818   # FC Botosani
clubDictROM['PETR'] = 9465   # Petrolul Ploiesti
clubDictROM['CONC'] = 15945  # Concordia Chiajna
clubDictROM['ACSP'] = 36590  # ACS Poli Timisoara
clubDictROM['CSMS'] = 33966  # CSMS Iasi
clubDictROM['FCVO'] = 40843  # FC Voluntari

# GERMAN BUNDESLIGA 2
clubDictGER2       = dict()
clubDictGER2['RASE'] = 23826  # RasenBallsport Leipzig
clubDictGER2['SCFR'] = 60     # SC Freiburg
clubDictGER2['KAIS'] = 2      # 1.FC Kaiserslautern
clubDictGER2['NURE'] = 4      # 1.FC Nuremberg
clubDictGER2['FORT'] = 38     # Fortuna Dusseldorf
clubDictGER2['UNIO'] = 89     # 1.FC Union Berlin
clubDictGER2['KARL'] = 48     # Karlsruher SC
clubDictGER2['SCPA'] = 127    # SC Paderborn 07
clubDictGER2['EINT'] = 23     # Eintracht Braunschweig
clubDictGER2['SPVG'] = 65     # SpVgg Greuther Furth
clubDictGER2['VFLB'] = 80     # VfL Bochum
clubDictGER2['TSV1'] = 72     # TSV 1860 Munich
clubDictGER2['FCST'] = 35     # FC St. Pauli
clubDictGER2['FSVF'] = 293    # FSV Frankfurt
clubDictGER2['HEID'] = 2036   # 1.FC Heidenheim 1846
clubDictGER2['MSVD'] = 52     # MSV Duisburg
clubDictGER2['SVSA'] = 254    # SV Sandhausen
clubDictGER2['ARMI'] = 10     # Arminia Bielefeld

# ITALIAN SERIE B
clubDictESP2         = dict()
clubDictESP2['UDAL'] = 3302   # UD Almeria
clubDictESP2['VALL'] = 366    # Real Valladolid CF
clubDictESP2['ZARA'] = 142    # Real Zaragoza
clubDictESP2['CORD'] = 993    # Cordoba CF
clubDictESP2['CDLE'] = 1244   # CD Leganes
clubDictESP2['ELCH'] = 1531   # Elche CF
clubDictESP2['BILB'] = 6688   # Bilbao Athletic
clubDictESP2['RCDM'] = 237    # RCD Mallorca
clubDictESP2['SDPO'] = 4032   # SD Ponferradina
clubDictESP2['CAOS'] = 331    # CA Osasuna
clubDictESP2['GIRO'] = 12321  # Girona FC
clubDictESP2['ADAL'] = 11596  # AD Alcorcon
clubDictESP2['CDLU'] = 11000  # CD Lugo
clubDictESP2['CDNU'] = 2296   # CD Numancia
clubDictESP2['ALBA'] = 1532   # Albacete Balompie
clubDictESP2['CDTE'] = 648    # CD Tenerife
clubDictESP2['OVIE'] = 2497   # Real Oviedo
clubDictESP2['GIMN'] = 5648   # Gimnastic de Tarragona
clubDictESP2['UELL'] = 26132  # UE Llagostera
clubDictESP2['DEPO'] = 1108   # Deportivo Alaves
clubDictESP2['CDMI'] = 13222  # CD Mirandes
clubDictESP2['SDHU'] = 5358   # SD Huesca

# AUSTRIAN BUNDESLIGA
clubDictAUT       = dict()
clubDictAUT['REDB'] = 409    # Red Bull Salzburg
clubDictAUT['RAPI'] = 170    # Rapid Vienna
clubDictAUT['AUST'] = 14     # Austria Vienna
clubDictAUT['SKST'] = 122    # SK Sturm Graz
clubDictAUT['SVRI'] = 266    # SV Ried
clubDictAUT['SCRH'] = 3551   # SC Rheindorf Altach
clubDictAUT['WOLF'] = 4441   # Wolfsberger AC
clubDictAUT['FCAD'] = 503    # FC Admira Wacker Modling
clubDictAUT['SVMA'] = 856    # SV Mattersburg
clubDictAUT['SVGR'] = 10131  # SV Grodig

# DANNISH ALKA SUPERLIGAEN
clubDictDEN       = dict()
clubDictDEN['FCCO'] = 190   # FC Copenhagen
clubDictDEN['FCMI'] = 865   # FC Midtjylland
clubDictDEN['BRON'] = 206   # Brondby IF
clubDictDEN['ODEN'] = 173   # Odense Boldklub
clubDictDEN['AALB'] = 1053  # Aalborg BK
clubDictDEN['ESBJ'] = 3426  # Esbjerg fB
clubDictDEN['FCNO'] = 2778  # FC Nordsjaelland
clubDictDEN['RAND'] = 5724  # Randers FC
clubDictDEN['AARH'] = 678   # Aarhus GF
clubDictDEN['HOBR'] = 5818  # Hobro IK
clubDictDEN['SOND'] = 5817  # SonderiyskE
clubDictDEN['VIBO'] = 1063  # Viborg FF

# SPANISH SEGUNDA DIVISION
clubDictITA2       = dict()
clubDictITA2['CAGL'] = 1390   # Cagliari Calcio
clubDictITA2['DELF'] = 2921   # Delfino Pescara 1936
clubDictITA2['ACCE'] = 1429   # AC Cesena
clubDictITA2['SPEZ'] = 3522   # Spezia Calcio
clubDictITA2['ASLI'] = 1210   # AS Livorno
clubDictITA2['FCBA'] = 332    # FC Bari 1908
clubDictITA2['ACPE'] = 839    # AC Perugia Calcio
clubDictITA2['USAV'] = 2331   # US Avellino 1912
clubDictITA2['CALC'] = 1047   # Calcio Como
clubDictITA2['NOVA'] = 6692   # Novara Calcio 1908
clubDictITA2['VICE'] = 2655   # Vicenza Calcio
clubDictITA2['USLA'] = 22045  # US Latina Calcio
clubDictITA2['TERN'] = 1103   # Ternana Calcio
clubDictITA2['FCCR'] = 4083   # FC Crotone
clubDictITA2['ASCO'] = 408    # Ascoli Picchio
clubDictITA2['FCPR'] = 26789  # FC Pro Vercelli 1892
clubDictITA2['BRES'] = 19     # Brescia Calcio
clubDictITA2['MODE'] = 1385   # Modena FC 1912
clubDictITA2['TRAP'] = 4331   # Trapani Calcio
clubDictITA2['VIRT'] = 20519  # Virtus Entella
clubDictITA2['USSA'] = 380    # US Salernitana 1919
clubDictITA2['SSVI'] = 4718   # SS Virtus Lanciano

# ENGLISH CHAMPIONSHIP
clubDictENG2       = dict()
clubDictENG2['QUEE'] = 1039  # Queens Park Rangers
clubDictENG2['HULL'] = 3008  # Hull City
clubDictENG2['DERB'] = 22    # Derby County
clubDictENG2['MIDD'] = 641   # Middlesbrough FC
clubDictENG2['BURN'] = 1132  # Burnley FC
clubDictENG2['NOTT'] = 703   # Nottingham Forest
clubDictENG2['READ'] = 1032  # Reading FC
clubDictENG2['CARD'] = 603   # Cardiff City
clubDictENG2['SHEF'] = 1035  # Sheffield Wednesday
clubDictENG2['BRIG'] = 1237  # Brighton & Hove Albion
clubDictENG2['FULH'] = 931   # Fulham FC
clubDictENG2['WOLV'] = 543   # Wolverhampton Wanderers
clubDictENG2['BLAC'] = 164   # Blackburn Rovers
clubDictENG2['LEED'] = 399   # Leeds United
clubDictENG2['CHAR'] = 358   # Charlton Athletic
clubDictENG2['BREN'] = 1148  # Brentford FC
clubDictENG2['IPSW'] = 677   # Ipswich Town
clubDictENG2['BOLT'] = 355   # Bolton Wanderers
clubDictENG2['HUDD'] = 1110  # Huddersfield Town
clubDictENG2['BIRM'] = 337   # Birmingham City
clubDictENG2['ROTH'] = 1194  # Rotherham United
clubDictENG2['BRIS'] = 698   # Bristol City
clubDictENG2['PRES'] = 466   # Preston North End
clubDictENG2['MILT'] = 991   # Milton Keynes Dons

# CROATIAN 1.HNL
clubDictCRO       = dict()
clubDictCRO['GNKD'] = 419    # GNK Dinamo Zagreb
clubDictCRO['HNKH'] = 447    # HNK Hajduk Split
clubDictCRO['HNKR'] = 144    # HNK Rijeka
clubDictCRO['NKLO'] = 11194  # NK Lokomotiva Zagreb
clubDictCRO['RNKS'] = 420    # RNK Split
clubDictCRO['SLAV'] = 2362   # Slaven Belupo Koprivnica
clubDictCRO['NKIS'] = 999    # NK Istra 1961
clubDictCRO['NKZA'] = 5107   # NK Zagreb
clubDictCRO['NKIN'] = 918    # NK Inter Zapresic
clubDictCRO['NKOS'] = 327    # NK Osijek

# CZECH SYNOT LIGA
clubDictCZE       = dict()
clubDictCZE['ACSP'] = 197   # AC Sparta Praha
clubDictCZE['FCVI'] = 941   # FC Viktoria Plzen
clubDictCZE['SKSL'] = 62    # SK Slavia Prag
clubDictCZE['FCSL'] = 697   # FC Slovan Liberec
clubDictCZE['FKJA'] = 1322  # FK Jablonec
clubDictCZE['FKML'] = 5546  # FK Mlada Boleslav
clubDictCZE['FKTE'] = 814   # FK Teplice
clubDictCZE['SKSI'] = 2311  # SK Sigma Olomouc
clubDictCZE['DUKL'] = 450   # Dukla Prag
clubDictCZE['FCBA'] = 377   # FC Banik Ostrava
clubDictCZE['1.FC'] = 5544  # 1.FC Slovacko
clubDictCZE['FCBO'] = 715   # FC Bohemians Prag 1905
clubDictCZE['1.FK'] = 2598  # 1.FK Pribram
clubDictCZE['FCVY'] = 7975  # FC Vysocina Jihlava
clubDictCZE['FCFA'] = 5545  # FC FASTAV Zlin
clubDictCZE['FCZB'] = 5225  # FC Zbrojovka Brno

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
clubs['SerieABrazil']         = clubDictBRA
clubs['Liga1']                = clubDictROM
clubs['HNL1']                 = clubDictCRO
clubs['BundesligaAustria']    = clubDictAUT
clubs['SynotLiga']            = clubDictCZE
clubs['AlkaSuperligaen']      = clubDictDEN
clubs['SuperLiga']            = clubDictSRB
clubs['Championship']         = clubDictENG2
clubs['SegundaDivision']      = clubDictESP2
clubs['Bundesliga2']          = clubDictGER2
clubs['SerieB']               = clubDictITA2
