#### Data

Create an array `listProducts` containing the list of the following products:

-   Id: 1, name: `Suitcase 250`, price: 50, stock: 4
-   Id: 2, name: `Suitcase 450`, price: 100, stock: 10
-   Id: 3, name: `Suitcase 650`, price: 350, stock: 2
-   Id: 4, name: `Suitcase 1050`, price: 550, stock: 5

#### Data access

Create a function named `getItemById`:

-   It will take `id` as argument
-   It will return the item from `listProducts` with the same id

#### Server

Create an `express` server listening on the port 1245. (You will start it via: `npm run dev 9-stock.js`)

#### Products

Create the route `GET /list_products` that will return the list of every available product with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products ; echo ""
[{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}]
bob@dylan:~$ 
```

#### In stock in Redis

Create a client to connect to the Redis server:

-   Write a function `reserveStockById` that will take `itemId` and `stock` as arguments:
    -   It will set in Redis the stock for the key `item.ITEM_ID`
-   Write an async function `getCurrentReservedStockById`, that will take `itemId` as an argument:
    -   It will return the reserved stock for a specific item

#### Product detail

Create the route `GET /list_products/:itemId`, that will return the current product and the current available stock (by using `getCurrentReservedStockById`) with the following JSON format:

```
bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
bob@dylan:~$ 
```

If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
```

#### Reserve a product

Create the route `GET /reserve_product/:itemId`:

-   If the item does not exist, it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
```

-   If the item exists, it should check that there is at least one stock available. If not it should return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$ 
```

-   If there is enough stock available, it should reserve one item (by using `reserveStockById`), and return:

```
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$ 
```

**Requirements:**

-   Make sure to use `promisify` with Redis
-   Make sure to use the `await`/`async` keyword to get the value from Redis
-   Make sure the format returned by the web application is always JSON and not text