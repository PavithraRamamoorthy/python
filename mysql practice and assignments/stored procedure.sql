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

