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
  `nameClub` varchar(255) NOT NULL,
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
  `idC` int(11) NOT NULL,
  `nameCountry` varchar(255) NOT NULL,
  PRIMARY KEY (`idC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table footballnetwork.countries: ~6 rows (približno)
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` (`idC`, `nameCountry`) VALUES
	(1, 'Slovenia'),
	(2, 'England'),
	(3, 'Spain'),
	(4, 'Italy'),
	(5, 'Germany'),
	(6, 'France'),
	(7, 'Portugal'),
	(8, 'Netherlands'),
	(9, 'Belgium'),
	(10, 'Scotland'),
	(11, 'Russia'),
	(12, 'Ukraine'),
	(13, 'Switzerland'),
	(14, 'Turkey'),
	(15, 'USA');
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
	(1, 2, 'Premier League'),
	(2, 3, 'La Liga'),
	(3, 4, 'Serie A'),
	(4, 5, 'Bundesliga'),
	(5, 6, 'Ligue 1'),
	(6, 7, 'PrimeraLiga'),
	(7, 8, 'Eredivise'),
	(8, 9, 'ProLeague'),
	(9, 10, 'Premiership'),
	(10, 11, 'PremierLeagueRussia'),
	(11, 12, 'PremierLeagueUkraine'),
	(12, 13, 'SuperLeague'),
	(13, 14, 'SuperLig'),
	(14, 15, 'MajorLeagueSoccer');
/*!40000 ALTER TABLE `leagues` ENABLE KEYS */;


-- Dumping structure for tabela footballnetwork.player
CREATE TABLE IF NOT EXISTS `player` (
  `idP` int(11) NOT NULL,
  `idC` int(11) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) DEFAULT NULL,
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
