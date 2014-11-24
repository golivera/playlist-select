drop table if exists track;
drop table if exists artist;
drop table if exists album;
create table track(
  id integer primary key autoincrement,
  title text not null,
  path text not null
);
create table artist(
  id integer primary key autoincrement,
  name text not null
);
create table album(
  id integer primary key autoincrement,
  name text not null,
  art_path text,
  artist_name text,
  foreign key(artist_name) references artist(name));
