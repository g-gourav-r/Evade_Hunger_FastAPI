# API signatures 

## Add Food Entry Endpoint:

- Method: `POST`
- Path: `/add_food/`
- Request Body:

```
{
  "name": String,
  "quantity": Integer,
  "location": String
}
```
- Response Body:
```
{
  "message": "Food entry added successfully"
}
```
## Update Food Status Endpoint:

- Method: `PUT`
- Path: `/update_food_status`
- Request Body:
```
{
  "ID": 1,
  "status": true,
  "name": "example_user",
  "password": "example_password"
}
```
- Response Body:

```
{
  "message": "Food status updated successfully for food_id: 1"
}
```
## View All Food Entries Endpoint:

- Method: `GET`
- Path: `/view_all_food/`
* Response Body:
- Format: `list`
```
[
  {"ID": 1, "name": "ExampleFood1", "quantity": 10, "location": "Kitchen", "status": 0},
  {"ID": 2, "name": "ExampleFood2", "quantity": 5, "location": "Pantry", "status": 1},
  ...
]
```
## View Food Entries with Status Endpoint:

- Method: `GET`
- Path: `/view_food_with_status/{status}`
- Path Parameters: `status (int)`
- Response Body:
Format: `list`
```
[
  {"ID": 1, "name": "ExampleFood1", "quantity": 10, "location": "Kitchen", "status": 1},
  {"ID": 3, "name": "ExampleFood3", "quantity": 8, "location": "Fridge", "status": 1},
  ...
]
```
