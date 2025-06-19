# csvtool

## installing

```bash
git clone https://github.com/mafooll/csvtool.git &&
cd csvtool &&
docker-compose build
```

## pre-installed csv by path csv_files/products.csv

```
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
iphone 14,apple,799,4.7
galaxy a54,samsung,349,4.2
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1
galaxy z flip 5,samsung,999,4.6
redmi 10c,xiaomi,149,4.1
iphone 13 mini,apple,5999,4.5

```


## run

```bash
docker compose run --rm csv-cli csv_file_path command
```

## run example

```bash
docker compose run --rm csv-cli csv_files/products.csv --filter 'price<999 and (brand=apple or brand=samsung)' --sort 'rating:desc'
```
## output from run example command

```
+------------+---------+-------+--------+
|    name    |  brand  | price | rating |
+------------+---------+-------+--------+
| iphone 14  |  apple  |  799  |  4.7   |
| galaxy a54 | samsung |  349  |  4.2   |
| iphone se  |  apple  |  429  |  4.1   |
+------------+---------+-------+--------+
```
