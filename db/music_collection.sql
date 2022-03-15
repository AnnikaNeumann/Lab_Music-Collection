DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists(
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  genre VARCHAR(255),
  artist_id INT REFERENCES artists(id)
);

INSERT INTO artists (name) VALUES ('Abba');
INSERT INTO artists (name) VALUES ('Nirvana');
INSERT INTO artists (name) VALUES ('The Beatles');
INSERT INTO artists (name) VALUES ('Robbie Williams');

INSERT INTO albums (title, genre, artist_id) VALUES ('Gold', 'Pop', 1);
INSERT INTO albums (title, genre, artist_id) VALUES ('Nevermind', 'Metal', 2);
INSERT INTO albums (title, genre, artist_id) VALUES ('The White Album', 'Rock', 3);
INSERT INTO albums (title, genre, artist_id) VALUES ('Swing when you"re winning', 'Pop', 4);



