drop table if exists tracks;
create table tracks (
  id integer primary key autoincrement,
  title text not null,
  path text not null
);

