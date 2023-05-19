## Requirements
A website that processes online orders with high concurrent traffic requires an order ID scheme of the format `<date>- <sequential number>` such as in "YYYYMMDD-nnnnn". Following this scheme, the first 2 orders for today would have the IDs `20200718-00001` and `20200718-00002`, and then the next day the sequential number would restart from `1`. It is necessary that they are unique. Please devise some logic/design that would allow for the assignment of these IDs, ensuring that they do not collide, accounting for the possibility that both orders are processed at virtually the exact same time.

Please use Django/ Python for your solution. The logic and thought process demonstrated are the most important considerations rather than truly functional code, however code presentation is important as well as the technical aspect. If you cannot settle on a single perfect solution, you may also discuss alternative solutions to demonstrate your understanding of potential trade-offs as you encounter them. Of course if you consider a solution is too time consuming you are also welcome to clarify or elaborate on potential improvements or multiple solution approaches conceptually to demonstrate understanding and planned solution.

## How to run
1. Clone this repository and go to the project folder
2. Build docker image and run docker container
```bash
docker-compose up
```
## Request:
- Method: `POST`
- Endpoint: `http://localhost:8000/api/order/`

## Solution explanation
I create `OrderCounter` model to save the counter. Whenever we have the request at this endpoint, the function `gen_new_id` will be calles to create new `Order`. 
