# fooder
Online Food Delivery Management System 


**Problem Statement —**

Design an API to calculate food delivery time based on the following conditions. Each restaurant has a maximum capacity of only 7 cooking slots. Each appetizer (A) requires 1 cooking slot and every Main Course (M) requires 2 cooking slots. Appetizers require 17 minutes to be prepared and main courses take 29 minutes. Assume that the delivery time can be calculated by a simple formula that every 1km can be covered in 8 minutes.

You have to calculate how much time it would take for an order to be delivered. The orders come in and are maintained in a queue. If the restaurant cannot accommodate a new order it gets queued and the estimated time for its delivery gets calculated.


**Additional rules :-**

If an order is going to take more than 2 hour 30 minutes to get delivered, it gets denied.

- Every order has a 2 digit unique id.
- You cannot change the order of entries in the queue.
- If any order in itself cannot be prepared at once it will be denied. (Look at order 14 in the sample output)
- A new order can start only if it has the required free slots available to accommodate it.
- If a new order comes and does not have enough free slots, it has to wait till any of the previous order gets completed. An order can only be marked as completed if it gets delivered and the next order can start cooking only then.
- No orders can be cooked in parts.
- All orders come in at the same time.
- Please use the exact input file as given below.


**Input -**
```
[{"orderId": 12, "meals": ["A", "A"], "distance": 5},
{"orderId": 21, "meals": ["A", "M"], "distance": 1},
{"orderId": 14, "meals": ["M", "M", "M", "M", "A", "A", "A"], "distance": 10},
{"orderId": 32, "meals": ["M"], "distance": 0.1},
{"orderId": 22, "meals": ["A"], "distance": 3}]
```


**Output -**
```
Order 12 will get delivered in 57 minutes

Order 21 will get delivered in 37 minutes

Order 14 is denied because the restaurant cannot accommodate it.

Order 32 will get delivered in 29.8 minutes

Order 22 will get delivered in 70.8 minutes
```