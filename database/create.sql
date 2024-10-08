

create table books (
  id integer primary key autoincrement,
  title text not null,
  author text,
  user_id integer
);

create table users (
  id integer primary key autoincrement,
  name text not null
)

create table user_books (
  id integer primary key autoincrement,
  created_at datetime default current_timestamp,
  user_id integer not null,
  book_id integer not null,
  foreign key (user_id) references users (id),
  foreign key (book_id) references books (id)
);
