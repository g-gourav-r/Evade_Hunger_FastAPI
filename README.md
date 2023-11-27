# API signatures

1. **Add User:**

 * **Endpoint:**`/add_user`
 * **HTTP Method:**`POST`
 * **Request Body:**

     ```
     {
     "name": "string",
     "password": "string",
     "email": "string",
     "phone": "string"
     }
     ```
 * **Response:**

     ```
     {
       "message": "string"
     }
     ```
2. **Show Users:**

* **Endpoint:**`/users`
* **HTTP Method:**`GET`
* **Response**:

```
{
"users": [
{
"ID": 1,
"name": "string",
"password": "string",
"type": 0,
"email": "string",
"phone": "string"
},
...
]
}
```

3. **Update User Type:**

* **Endpoint:**`/update_user_type`
* **HTTP Method:**`PUT`
* **Request Body:**

```
{
"user_id": Integer,
"username": "string",
"password": "string",
"new_type": Integer
}
```

* **Response:**

```
{
"message": "string"
}
```
