from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokannasta users table:n ja passwords table:n jos
    ne ovat olemassa, eli toisinsanoen poistaa tietokannasta kaiken tiedon.

    Args:
        connection (Connection): annettu tietokantayhteys
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists passwords;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo tietokantaan tarvittavat table:t eli users ja passwords table:t
    joihin tullaan tallettamaan käyttäjätunnukset ja salasanat.

    Args:
        connection (Connection): annettu tietokantayhteys
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table users (
            username text primary key,
            password text
        );
    ''')

    cursor.execute('''
        create table passwords (
            id integer PRIMARY KEY,
            username text,
            app text,
            password text
        )
    ''')

    connection.commit()


def initialize_database():
    """Alustaa tietokannan ensin poistamalla kaiken tiedon tietokannasta, ja sitten luomalla tarvittavat
    table:t siihen. 
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
