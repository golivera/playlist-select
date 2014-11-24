drop table if exists tracks;
drop table if exists artists;
drop table if exists albums;
create table tracks (
  id integer primary key autoincrement,
  title text not null,
  path text not null
);
create table artists(
  id integer primary key autoincrement,
  name text not null
);
create table albums(
  id integer primary key autoincrement,
  name text not null,
  art_path text,
  artist_name text,
  foreign key(artist_name) references artists(name));
