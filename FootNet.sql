-- --------------------------------------------------------
-- Strežnik:                     127.0.0.1
-- Server version:               10.1.7-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Različica:           9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for footballnetwork
CREATE DATABASE IF NOT EXISTS `footballnetwork` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `footballnetwork`;


-- Dumping structure for tabela footballnetwork.club
CREATE TABLE IF NOT EXISTS `club` (
  `idClub` int(11) NOT NULL,
  `idL` int(11) NOT NULL,
  `nameClub` nvarchar(255) NOT NULL,
  PRIMARY KEY (`idClub`),
  KEY `FK_PlaysIn` (`idL`),
  CONSTRAINT `FK_PlaysIn` FOREIGN KEY (`idL`) REFERENCES `leagues` (`idL`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.club: ~0 rows (približno)
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
/*!40000 ALTER TABLE `club` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.clubseason
CREATE TABLE IF NOT EXISTS `clubseason` (
  `idS` int(11) NOT NULL,
  `idClub` int(11) NOT NULL,
  `ranking` int(11) NOT NULL,
  `value` decimal(10,0) NOT NULL,
  PRIMARY KEY (`idS`,`idClub`),
  KEY `FK_ClubClubSeason` (`idClub`),
  KEY `FK_SeasonClubSeason` (`idS`),
  CONSTRAINT `FK_ClubClubSeason` FOREIGN KEY (`idClub`) REFERENCES `club` (`idClub`),
  CONSTRAINT `FK_SeasonClubSeason` FOREIGN KEY (`idS`) REFERENCES `season` (`idS`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.clubseason: ~0 rows (približno)
/*!40000 ALTER TABLE `clubseason` DISABLE KEYS */;
/*!40000 ALTER TABLE `clubseason` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.countries
CREATE TABLE IF NOT EXISTS `countries` (
  `idC` int(11) NOT NULL AUTO_INCREMENT,
  `nameCountry` varchar(255) NOT NULL,
  PRIMARY KEY (`idC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.countries: ~6 rows (približno)
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` (`nameCountry`) VALUES
    ('Afghanistan'),
    ('Albania'),
    ('Algeria'),
    ('American Samoa'),
    ('Andorra'),
    ('Angola'),
    ('Anguilla'),
    ('Antarctica'),
    ('Antigua and Barbuda'),
    ('Argentina'),
    ('Armenia'),
    ('Aruba'),
    ('Australia'),
    ('Austria'),
    ('Azerbaijan'),
    ('Bahamas'),
    ('Bahrain'),
    ('Bangladesh'),
    ('Barbados'),
    ('Belarus'),
    ('Belgium'),
    ('Belize'),
    ('Benin'),
    ('Bermuda'),
    ('Bhutan'),
    ('Bolivia'),
    ('Bosnia-Herzegovina'),
    ('Botswana'),
    ('Bouvet Island'),
    ('Brazil'),
    ('British Antarctic Territory'),
    ('British Indian Ocean Territory'),
    ('British Virgin Islands'),
    ('Brunei'),
    ('Bulgaria'),
    ('Burkina Faso'),
    ('Burundi'),
    ('Cambodia'),
    ('Cameroon'),
    ('Canada'),
    ('Canton and Enderbury Islands'),
    ('Cape Verde'),
    ('Cayman Islands'),
    ('Central African Republic'),
    ('Chad'),
    ('Chile'),
    ('China'),
    ('Christmas Island'),
    ('Cocos [Keeling] Islands'),
    ('Colombia'),
    ('Comoros'),
    ('Congo - Brazzaville'),
    ('Congo DR'),
    ('Cook Islands'),
    ('Costa Rica'),
    ('Croatia'),
    ('Cuba'),
    ('Cyprus'),
    ('Czech Republic'),
    ('Cote d\'Ivoire'),
    ('Denmark'),
    ('Djibouti'),
    ('Dominica'),
    ('Dominican Republic'),
    ('Dronning Maud Land'),
    ('East Germany'),
    ('Ecuador'),
    ('Egypt'),
    ('El Salvador'),
    ('Equatorial Guinea'),
    ('Eritrea'),
    ('Estonia'),
    ('Ethiopia'),
    ('Falkland Islands'),
    ('Faroe Islands'),
    ('Fiji'),
    ('Finland'),
    ('France'),
    ('French Guiana'),
    ('French Polynesia'),
    ('French Southern Territories'),
    ('French Southern and Antarctic Territories'),
    ('Gabon'),
    ('Gambia'),
    ('Georgia'),
    ('Germany'),
    ('Ghana'),
    ('Gibraltar'),
    ('Greece'),
    ('Greenland'),
    ('Grenada'),
    ('Guadeloupe'),
    ('Guam'),
    ('Guatemala'),
    ('Guernsey'),
    ('Guine'),
    ('Guinea'),
    ('Guinea-Bissau'),
    ('Guyana'),
    ('Haiti'),
    ('Heard Island and McDonald Islands'),
    ('Honduras'),
    ('Hong Kong SAR China'),
    ('Hungary'),
    ('Iceland'),
    ('India'),
    ('Indonesia'),
    ('Iran'),
    ('Iraq'),
    ('Ireland'),
    ('Isle of Man'),
    ('Israel'),
    ('Italy'),
    ('Jamaica'),
    ('Japan'),
    ('Jersey'),
    ('Johnston Island'),
    ('Jordan'),
    ('Kazakhstan'),
    ('Kenya'),
    ('Kiribati'),
    ('Kuwait'),
    ('Kyrgyzstan'),
    ('Laos'),
    ('Latvia'),
    ('Lebanon'),
    ('Lesotho'),
    ('Liberia'),
    ('Libya'),
    ('Liechtenstein'),
    ('Lithuania'),
    ('Luxembourg'),
    ('Macau SAR China'),
    ('Macedonia'),
    ('Madagascar'),
    ('Malawi'),
    ('Malaysia'),
    ('Maldives'),
    ('Mali'),
    ('Malta'),
    ('Marshall Islands'),
    ('Martinique'),
    ('Mauritania'),
    ('Mauritius'),
    ('Mayotte'),
    ('Metropolitan France'),
    ('Mexico'),
    ('Micronesia'),
    ('Midway Islands'),
    ('Moldova'),
    ('Monaco'),
    ('Mongolia'),
    ('Montenegro'),
    ('Montserrat'),
    ('Morocco'),
    ('Mozambique'),
    ('Myanmar [Burma]'),
    ('Namibia'),
    ('Nauru'),
    ('Nepal'),
    ('Netherlands'),
    ('Netherlands Antilles'),
    ('Neutral Zone'),
    ('New Caledonia'),
    ('New Zealand'),
    ('Nicaragua'),
    ('Niger'),
    ('Nigeria'),
    ('Niue'),
    ('Norfolk Island'),
    ('North Korea'),
    ('North Vietnam'),
    ('Northern Mariana Islands'),
    ('Norway'),
    ('Oman'),
    ('Pacific Islands Trust Territory'),
    ('Pakistan'),
    ('Palau'),
    ('Palestinian Territories'),
    ('Panama'),
    ('Panama Canal Zone'),
    ('Papua New Guinea'),
    ('Paraguay'),
    ('People\'s Democratic Republic of Yemen'),
    ('Peru'),
    ('Philippines'),
    ('Pitcairn Islands'),
    ('Poland'),
    ('Portugal'),
    ('Puerto Rico'),
    ('Qatar'),
    ('Romania'),
    ('Russia'),
    ('Rwanda'),
    ('Réunion'),
    ('Saint Barthélemy'),
    ('Saint Helena'),
    ('Saint Kitts and Nevis'),
    ('Saint Lucia'),
    ('Saint Martin'),
    ('Saint Pierre and Miquelon'),
    ('Saint Vincent and the Grenadines'),
    ('Samoa'),
    ('San Marino'),
    ('Saudi Arabia'),
    ('Senegal'),
    ('Serbia'),
    ('Serbia and Montenegro'),
    ('Seychelles'),
    ('Sierra Leone'),
    ('Singapore'),
    ('Slovakia'),
    ('Slovenia'),
    ('Solomon Islands'),
    ('Somalia'),
    ('South Africa'),
    ('South Georgia and the South Sandwich Islands'),
    ('South Korea'),
    ('Spain'),
    ('Sri Lanka'),
    ('Sudan'),
    ('Suriname'),
    ('Svalbard and Jan Mayen'),
    ('Swaziland'),
    ('Sweden'),
    ('Switzerland'),
    ('Syria'),
    ('São Tomé and Príncipe'),
    ('Taiwan'),
    ('Tajikistan'),
    ('Tanzania'),
    ('Thailand'),
    ('Timor-Leste'),
    ('Togo'),
    ('Tokelau'),
    ('Tonga'),
    ('Trinidad and Tobago'),
    ('Tunisia'),
    ('Turkey'),
    ('Turkmenistan'),
    ('Turks and Caicos Islands'),
    ('Tuvalu'),
    ('U.S. Minor Outlying Islands'),
    ('U.S. Miscellaneous Pacific Islands'),
    ('U.S. Virgin Islands'),
    ('Uganda'),
    ('Ukraine'),
    ('Union of Soviet Socialist Republics'),
    ('United Arab Emirates'),
    ('United Kingdom'),
    ('United States'),
    ('Unknown or Invalid Region'),
    ('Uruguay'),
    ('Uzbekistan'),
    ('Vanuatu'),
    ('Vatican City'),
    ('Venezuela'),
    ('Vietnam'),
    ('Wake Island'),
    ('Wales'),
    ('Wallis and Futuna'),
    ('Western Sahara'),
    ('Yemen'),
    ('Zambia'),
    ('Zimbabwe'),
    ('England'),
    ('Scotland'),
    ('Ireland'),
    ('Northern Ireland'),
    ('Wales'),
    ('USA'),
    ('Unknown');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.leagues
CREATE TABLE IF NOT EXISTS `leagues` (
  `idL` int(11) NOT NULL,
  `idC` int(11) NOT NULL,
  `nameLeague` varchar(50) NOT NULL,
  PRIMARY KEY (`idL`),
  KEY `FK_BelongsTo` (`idC`),
  CONSTRAINT `FK_BelongsTo` FOREIGN KEY (`idC`) REFERENCES `countries` (`idC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.leagues: ~5 rows (približno)
/*!40000 ALTER TABLE `leagues` DISABLE KEYS */;
INSERT INTO `leagues` (`idL`, `idC`, `nameLeague`) VALUES
	(1, 265, 'PremierLeague'),
	(2, 218, 'LaLiga'),
	(3, 112, 'SerieA'),
	(4, 86, 'Bundesliga'),
	(5, 78, 'Ligue 1'),
	(6, 188, 'PrimeraLiga'),
	(7, 160, 'Eredivise'),
	(8, 21, 'ProLeague'),
	(9, 265, 'Premiership'),
	(10, 192, 'PremierLeagueRussia'),
	(11, 246, 'PremierLeagueUkraine'),
	(12, 225, 'SuperLeague'),
	(13, 238, 'SuperLig'),
	(14, 268, 'MajorLeagueSoccer');
/*!40000 ALTER TABLE `leagues` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.player
CREATE TABLE IF NOT EXISTS `player` (
  `idP` int(11) NOT NULL,
  `idC` int(11) NOT NULL,
  `firstName` nvarchar(255) NOT NULL,
  `lastName` nvarchar(255) DEFAULT NULL,
  `birthDate` year(4) NOT NULL,
  `playingPosition` varchar(5) NOT NULL,
  `playingNumber` int(11) DEFAULT NULL,
  PRIMARY KEY (`idP`),
  KEY `FK_ResidesIn` (`idC`),
  CONSTRAINT `FK_ResidesIn` FOREIGN KEY (`idC`) REFERENCES `countries` (`idC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.player: ~0 rows (približno)
/*!40000 ALTER TABLE `player` DISABLE KEYS */;
/*!40000 ALTER TABLE `player` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.playerclubseason
CREATE TABLE IF NOT EXISTS `playerclubseason` (
  `idP` int(11) NOT NULL,
  `idClub` int(11) NOT NULL,
  `idS` int(11) NOT NULL,
  `playerValue` decimal(10,0) DEFAULT NULL,
  `playerNumber` int(11) NOT NULL,
  PRIMARY KEY (`idP`,`idClub`,`idS`),
  KEY `FK_ClubPSC` (`idClub`),
  KEY `FK_SeasonPSC` (`idS`),
  KEY `FK_PlayerPSC` (`idP`),
  CONSTRAINT `FK_ClubPSC` FOREIGN KEY (`idClub`) REFERENCES `club` (`idClub`),
  CONSTRAINT `FK_PlayerPSC` FOREIGN KEY (`idP`) REFERENCES `player` (`idP`),
  CONSTRAINT `FK_SeasonPSC` FOREIGN KEY (`idS`) REFERENCES `season` (`idS`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.playerclubseason: ~0 rows (približno)
/*!40000 ALTER TABLE `playerclubseason` DISABLE KEYS */;
/*!40000 ALTER TABLE `playerclubseason` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.season
CREATE TABLE IF NOT EXISTS `season` (
  `idS` int(11) NOT NULL,
  `year` varchar(8) NOT NULL,
  PRIMARY KEY (`idS`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.season: ~16 rows (približno)
/*!40000 ALTER TABLE `season` DISABLE KEYS */;
INSERT INTO `season` (`idS`, `year`) VALUES
	(1, '2001'),
	(2, '2002'),
	(3, '2003'),
	(4, '2004'),
	(5, '2005'),
	(6, '2006'),
	(7, '2007'),
	(8, '2008'),
	(9, '2009'),
	(10, '2010'),
	(11, '2011'),
	(12, '2012'),
	(13, '2013'),
	(14, '2014'),
	(15, '2015'),
	(16, '2016');
/*!40000 ALTER TABLE `season` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
