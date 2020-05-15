# CREATE TYPE mood AS ENUM('extremely unhappy', 'unhappy', 'ok', 'happy', 'extremely happy');
#
# CREATE TABLE students(
# name character varying(255),
# current_mood mood
# );
#
# SELECT * FROM students;
#
# INSERT INTO students VALUES('Moe', 'happy');
# INSERT INTO students VALUES('Larry', 'happy');
# INSERT INTO students VALUES('Rolf', 'extremely unhappy');
# INSERT INTO students VALUES('Jose', 'extremely happy');
# INSERT INTO students VALUES('Anna', 'happy');
# INSERT INTO students VALUES('Robert', 'happy');
#
# SELECT * FROM students WHERE current_mood > 'ok';