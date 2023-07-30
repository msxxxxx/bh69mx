from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor

with connect('postgresql://myuser:postgres@127.0.0.1:5432/postgres') as conn:
    with conn.cursor() as cur:
        commands = (
            '''
                create table statuses(
                id serial primary key,
                name varchar(10) unique)''',
            '''create table users(
                id serial primary key,
                name varchar(24),
                email
                varchar(24)
                unique)''',
            '''create table orders(
                id serial primary key,
                user_id integer,
                status_id integer,
                foreign key (status_id) references statuses(id) on delete cascade,
                foreign key (user_id) references users(id) on delete cascade)''',
            '''create table categories(
                id serial primary key,
                name varchar(24) unique)''',
            '''create table products(
                id serial primary key,
                title varchar(36),
                description varchar(140),
                category_id integer,
                foreign key (category_id) references categories(id) on delete cascade)''',
            '''create table order_items(
                id serial primary key,
                order_id integer,
                product_id integer,
                foreign key (order_id) references orders(id) on delete cascade,
                foreign key (product_id) references products(id) on delete cascade)''',
        )

        for command in commands:
            cur.execute(command)


conn.commit()


# text = input('text: ')
# with connect('postgresql://postgres:postgres@127.0.0.1:5432/postgres') as conn:
#     with conn.cursor() as cur:
#         # cur.execute('''insert into categories(name) values(%s);''', (text, ))
#         cur.execute(f'''insert into categories(name) values('{text}');''', )
#         conn.commit()
#         cur.execute('''select * from categories;''', )
#         print(cur.fetchall())

# with connect('postgresql://postgres:postgres@127.0.0.1:5432/postgres') as conn:
#     with conn.cursor() as cur:
#         cur.execute('''create table categories(
#                 id serial primary key,
#                 name varchar(24) unique)''',)
#         conn.commit()
