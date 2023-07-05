# <center>**SuperPy**</center>

## **Introduction**

This is SuperPy, a command line tool to manage your supermarkets inventory. The program allows you to buy and sell items or to remove expired products. It shows the inventory and reports of profit or revenue per day or period. You can also manipulate the internal time. Be careful with that! 

## First steps
Download SuperPy to your computer.<br>
Open a terminal, which is the program that gives you a command line.<br>
Make sure python is installed and up to date.<br>
Your working directory should be the superpy folder.
##### Example
```
C:\Users\your_name\Desktop\superpy>
```
Now you need to install the requiered third-party libraries. Type the following in your command line:
```
  pip install pandas
```
```
  pip install python-dateutil
```
SuperPy is now ready to work with. Let's look at the commands and how to use them!

## **Userguide**

### **help**

To get an overview of the commands SuperPy accepts, type **-h**  or  **-\-help**:
```
  python super.py -h
``` 
with **-h**  or  **-\-help** you can also see what a command does :

```
  python super.py buy -h
  python super.py status --help    
```
##  commands

### **status**

The most important command to start a day is **status**. It gives an overview of possible problems or things to do first. You will see if products have expired or should be sold with reduced pricing before they expire. If products are out of stock, you will get a notice so you can order more. Also you will get information about the cooling and freezing units in your store. If you want a status summary choose option  **all**:
```
  python super.py status all
```
Option **stock** gives a list of all products out of stock and a list of products which are less than 15% in stock.

```
  python super.py status stock
```
Option **storage** gives the status of your cooling and freezing storage units. There are warnings if storage is empty or full. You get also a warning, if storage is less then 45 % filled or if there is only 10% free space left.

```
  python super.py status storage
```
Option **expired** shows all expired products and all items almost expired which can be sold with a reduced pricing. If you want to delete expired products from SuperPy read the explanation of command **remove**. Don't forget to remove those items in the store as well! 
```
  python super.py status expired
```
### **inventory**

You can choose option **short** or **full** to show the inventory of your supermarket. 
The **short** inventory gives a list of products with the amounts *in stock* and *max stock* including the products not in stock. This is the supermarkets product range.
```
  python super.py inventory short
```
**output**:

|name  | stock  |max_stock|
|--|--|--|--|
|apple  | 6|30|
|banana  | 5|25|
|icecream  | 3|20|

If you choose **full** inventory, SuperPy shows a list of all products in store

```
  python super.py inventory full
```
**output**:
|name  | date_buy  |date_expire|count|
|--|--|--|--|
|apple  | 2023-06-21|2023-08-20|1|
| | 2023-06-22 |2023-08-21|5|
|banana  | 2023-06-03 |2023-03-16|1|
| | 2023-06-22 |2023-07-02|4|
|icecream | 2023-06-06| 2024-06-05 | 3|

### **buy**

SuperPy makes buying products very easy. All you need to do is to enter the name of the product you want to buy.  The program gets all other needed information like expiration date, buying and selling price from a csv file provided by the headquarter of the supermarket chain. Please use the required argument **-p** or **-\-product**!
```
  python super.py buy --product banana
  python super.py buy -p "cream cheese"
```
*Notice: If the product name has more than one word, please use quotes!*

Optional you can add an amount **-a** or **-\-amount**. If you don't enter an amount, the program will buy only 1 item of that product. 
```
  python super.py buy -p banana -a 5
```
*Notice: The amount need to be a positiv integer!*

SuperPy checks if the product is in range of the store, if it needs cooling or freezing, if the amount fits into the storage space and if it doesn't exceed the max amount. If everything is validated the bought items will be added with an unique id, today's date and an expiration date to the inventory. Stock and storage will be updated and the transaction will be saved.

*Notice: SuperPy will always reset the date to today!*

### **sell**

Selling products works the same way as buying. After the **sell** command you enter  **-p** or **-\-product** and the name of the product :

```
  python super.py sell --product banana 
  python super.py sell -p "cream cheese"
```
*Notice: If the product name has more than one word, please use quotes!*

SuperPy sells one item of that product. If you want to sell more than one, please enter an amount **-a** or **-\-amount**! 
```
  python super.py sell -p banana -a 3
```
SuperPy does the rest for you. The program checks if the product is in store and sells the available number of items. If the product has almost expired the discounted price is automatically used. The transaction will be saved, stock and storage will be updatet and the sold items will be removed from inventory. The transaction date will be today.

### **remove**

It is possible to delete data from SuperPy. The program will work faster after removing old data. Be careful! Data may be lost. It's recommended to export the data first. With following command Superpy will delete transfer data **old**er than 2 years.

```
  python super.py remove old
```
The other use of the remove command is to delete **expired** products from inventory. The expired product will be removed from inventory, stock and storage will be updated and the transaction will be saved.

```
  python super.py remove expired
```

### **export**

SuperPy can save transfer data to a csv file. The program makes folders for year, month or day reports and saves the files. required argument  **-d** or **-\-date** in the format '2000' for a year, '2000-01' for a month or '2000-01-01' for a single day.

```
  python super.py export --date '2000-01-01'
  python super.py export -d '2000-01'
  python super.py export -d '2000'
```
**example csv file**:
|date|action|name|price|inventory_id|
|--|--|--|--|--|
|2023-06-22|bought|apple|0.25|18|
|2023-06-22|bought|banana|0.5|19|
|2023-06-22|sold|banana|1.0|3|
|2023-06-22|expired|cucumber|0.0|12|

### **revenue**

With the **revenue** command SuperPy reports the revenue of the day the program knows as today.  This date can be changed with the time command.

```
  python super.py revenue
```
Another way to get the revenue of a different day is the optional argument **-d1** or **-\-date1**:
```
  python super.py revenue --date1 '2023-06-03'
```

If you are looking for the revenue of a period, SuperPy accepts a start date **-d1** or **-\-date1** and an end date **-d2** or **-\-date2**.
```
  python super.py revenue --date1 '2023-06-03' --date2 '2023-06-10'
```
With the optional argument **-p** or **-\-product** the program shows the revenue for this product at the chosen day or period.
```
  python super.py revenue --product apple
  python super.py revenue --date1 '2023-06-03' -p apple
  python super.py revenue --date1 '2023-06-03' --date2 '2023-06-10' -p "cream cheese"
```
*Notice: If the product name has more than one word, please use quotes!*

### **profit**

The profit command works the same way as revenue.

```
  python super.py profit
```
Another way to get the revenue of a different day is the optional argument **-d1** or **-\-date1**.
```
  python super.py profit --date1 '2023-06-03'
```

If you are looking for the profit of a period, SuperPy accepts a start date **-d1** or **-\-date1** and an end date **-d2** or **-\-date2**.
```
  python super.py profit --date1 '2023-06-03' --date2 '2023-06-10'
```
With the optional argument **-p** or **-\-product** the program shows the profit for this product at the chosen day or period.
```
  python super.py profit --product apple
  python super.py profit --date1 '2023-06-03' -p "cream cheese"
  python super.py profit -d1 '2023-06-03' -d2 '2023-06-10' -p apple
```
*Notice: If the product name has more than one word, please use quotes!*

### **time**
With the command **time** you can manipulate time in SuperPy. You can choose from **set**, **reset** and **advance**. Reset time will set the internal SuperPy date to today.
```
  python super.py time reset
```
If you want to use a specific date, you can **set** the new date by using the optional argument **-n** or **-\-new**.

```
  python super.py time set --new '2000-01-01'
```
Another way is to **advance** time by days, using the optional argument **-d** or **-\-days**. The program adds the amount of days to the date SuperPy knows as today at this moment.

```
  python super.py time advance -d 3
```
With a negative number of days the time goes back.
```
  python super.py time advance --days -7
```
*Notice: In this version of SuperPy time manipulation has only effect in combination with revenue and profit. All other functions reset time first* 