from connect import connect

def insert_or_update(cur):
    name = input("Name: ")
    phone = input("Phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))

def insert_many_users(cur):
    names = input("Names: ").split(",")
    phones = input("Phones: ").split(",")

    names = [x.strip().replace('"', '') for x in names]
    phones = [x.strip().replace('"', '') for x in phones]

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))

def search(cur):
    pattern = input("Search: ")
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    print(cur.fetchall())


def pagination(cur):
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    print(cur.fetchall())


def delete(cur):
    value = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (value,))


def main():
    conn = connect()
    cur = conn.cursor()

    while True:
        print("\n1. Insert/Update")
        print("2. Search")
        print("3. Pagination")
        print("4. Delete")
        print("5. Exit")
        print("6. Insert List")

        choice = input("Choose: ")

        if choice == "1":
            insert_or_update(cur)
        elif choice == "2":
            search(cur)
        elif choice == "3":
            pagination(cur)
        elif choice == "4":
            delete(cur)
        elif choice == "5":
            break
        elif choice == "6":
            insert_many_users(cur)

        conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()