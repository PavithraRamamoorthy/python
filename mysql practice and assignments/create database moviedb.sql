create database moviedb;
use moviedb;

CREATE TABLE `certificates` (
  `certificate_id` int(10) UNSIGNED NOT NULL,
  `certificate_name` varchar(30) NOT NULL,
  `certificate_description` text NOT NULL,
  `image` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `certificates`
--

INSERT INTO `certificates` (`certificate_id`, `certificate_name`, `certificate_description`, `image`) VALUES
(1, 'U', 'Suitable for all', 'u-cert.png'),
(2, 'PG', 'Some scenes may be unsuitable for young children', 'pg-cert.png'),
(3, '12', 'Suitable for people aged 12 and over.', '12-cert.png'),
(4, '15', 'Suitable for people aged 15 and over.', '15-cert.png'),
(5, '18', 'Suitable for people aged 18 and over.', '18-cert.png');

-- --------------------------------------------------------

--
-- Table structure for table `films`
--

CREATE TABLE `films` (
  `film_id` int(11) UNSIGNED NOT NULL,
  `film_title` varchar(100) NOT NULL,
  `film_year` smallint(6) NOT NULL,
  `duration` smallint(6) NOT NULL,
  `certificate_id` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `films`
--

INSERT INTO `films` (`film_id`, `film_title`, `film_year`, `duration`, `certificate_id`) VALUES
(1, 'Jaws', 1975, 124, 4),
(2, 'Winter\'s Bone', 2010, 100, 4),
(3, 'Do The Right Thing', 1989, 120, 4),
(4, 'The Incredibles', 2004, 115, 1),
(5, 'The Godfather', 1972, 177, 5),
(6, 'Dangerous Minds', 1995, 99, 4),
(7, 'Spirited Away', 2001, 124, 2),
(8, 'Moonlight', 2016, 111, 5),
(9, 'Life of PI', 2012, 127, 2),
(10, 'Gravity', 2013, 91, 3),
(11, 'Arrival', 2016, 116, 3),
(12, 'Wonder Woman', 2017, 141, 3),
(13, 'Mean Girls', 2004, 97, 4),
(14, 'Inception', 2010, 108, 3),
(15, 'Donnie Darko', 2001, 113, 4),
(16, 'Get Out', 2017, 103, 4);



--STORED PROCEDURE--ASSIGNMENT

delimiter //
CREATE PROCEDURE filmscertificates()
SELECT films.film_title,certificates.certificate_description, certificates.certificate_name, films.film_year 
from films
JOIN certificates
ON films.certificate_id=certificates.certificate_id
ORDER BY films.film_year ASC limit 1;
//
delimiter;

show PROCEDURE status;

