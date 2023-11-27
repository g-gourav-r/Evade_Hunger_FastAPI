import sqlite3
from fastapi import HTTPException


def add_user(user):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        SELECT * FROM users WHERE email=? OR phone=?
    ''', (user.email, user.phone))

    if c.fetchone() is not None:
        raise HTTPException(status_code=400, detail="Account with the same email or phone number already exists.")
    else:
        # Insert user into the users table
        c.execute('''
            INSERT INTO users (name, password, type, email, phone) VALUES (?, ?, 0, ?, ?)
        ''', (user.name, user.password, user.email, user.phone))

        print("Account created successfully!")

    conn.commit()
    conn.close()
    return {"message": "Account created successfully!"}


def show_users():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
        SELECT * FROM users
    ''')

    user_entries = c.fetchall()

    user_list = []
    for entry in user_entries:
        user_dict = {
            "ID": entry[0],
            "name": entry[1],
            "password": entry[2],
            "type": entry[3],
            "email": entry[4],
            "phone": entry[5]
        }
        user_list.append(user_dict)

    conn.close()

    return {"users": user_list}


async def update_user_type(user_data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Check if the user making the request is an admin
    admin_check = c.execute('SELECT * FROM users WHERE name=? AND password=? AND type=?',
                            (user_data.username, user_data.password, 1))

    admin_user = admin_check.fetchone()

    if admin_user is None:
        raise HTTPException(status_code=403, detail="Only admins can update user types.")

    # 0- customer
    # 1-admin
    # 2-volunteer

    # Get the current name of the user
    c.execute('SELECT name FROM users WHERE ID=?', (user_data.user_id,))
    current_name = c.fetchone()

    if current_name is not None:
        current_name = current_name[0]
        # Update the user type for the specified user_id
        c.execute('UPDATE users SET type=? WHERE ID=?', (user_data.new_type, user_data.user_id))

        conn.commit()
        conn.close()
        return {"message": f"{user_data.username} changed {current_name}'s role to {user_data.new_type}"}
    else:
        conn.close()
        raise HTTPException(status_code=404, detail=f"User with ID {user_data.user_id} not found.")
