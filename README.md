## Requirements:

A website that processes online orders with high concurrent traffic requires an order ID scheme of the format `<date>- <sequential number>` such as in "YYYYMMDD-nnnnn". Following this scheme, the first 2 orders for today would have the IDs `20200718-00001` and `20200718-00002`, and then the next day the sequential number would restart from `1`. It is necessary that they are unique. Please devise some logic/design that would allow for the assignment of these IDs, ensuring that they do not collide, accounting for the possibility that both orders are processed at virtually the exact same time.

Please use Django/ Python for your solution. The logic and thought process demonstrated are the most important considerations rather than truly functional code, however code presentation is important as well as the technical aspect. If you cannot settle on a single perfect solution, you may also discuss alternative solutions to demonstrate your understanding of potential trade-offs as you encounter them. Of course if you consider a solution is too time consuming you are also welcome to clarify or elaborate on potential improvements or multiple solution approaches conceptually to demonstrate understanding and planned solution.

## How to run:

1. Clone this repository and go to the project folder
2. Please ensure that ports 8000 and 5432 are available
3. Build docker image and run docker container

```bash
docker-compose up
```

## Request:

- Method: `POST`
- Endpoint: `http://localhost:8000/api/order/`

## Solution explanation:

I have created an OrderCounter model to store the counter value. Whenever a client sends a request to the endpoint, the gen_new_id function is called. It increments the counter field by 1 or creates a new record with a default value of 0 if the date is not found in the database.

To prevent the creation of duplicate primary keys in high concurrent traffic scenarios, I use the select_for_update() method to lock the record that has been updated or created:

```bash
order = OrderCounter.objects.select_for_update().get_or_create(date=current_date)[0]
```

By locking the resource, we ensure that only one request is processed at a time. Once the current request is completed, the resource is unlocked and available to serve the next request.
