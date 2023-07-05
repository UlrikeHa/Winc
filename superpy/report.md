# **Report**

**Data structure**
  
For me user-friendliness means that there should be an easy way to handle the input in SuperPy. Less input, less errors. I achieved this by storing information about expiration in the provided products.csv file. SuperPy adds the value to the buying date, which is also automatically generated, and saves it to inventory.csv. This way a user doesn't need to enter the buying and expiration dates himself.  

**Pandas library**

When I started the assignment I knew nothing about csv files or working with data. I thought displaying filtered data would be a huge time consuming thing to do. Then I learned, what pandas could do and how it works. Using "groups" and "aggregate" I could easily display a sorted list of products grouped by buying and expiration date and count items per group. I also could "sum" selected prices for profit and revenue. All this while using only a few lines of code.

**Storage**

When I planned my program and thought about additional features, the first thing what came up my mind was to manage the storage space of the supermarket along with the inventory. You don't want employees to buy stuff uncontrolled. Imagine an order of 5000 boxes fish sticks if you have only one freezer available. SuperPy should prevent this kind of mistake. First there is a maximum stock value for each product stored in products.csv. If you try to buy a product exceeding the available space, SuperPy will give you a warning and cancel the order. If a product needs cooling or freezing, the program is checking the free space in all cooling or freezing units before buying the ordered amount. If there is not enough space, the program will also give you a warning and cancel the order. 