# Scrap

This is the scrub program for one of popular website.

## Using Docker Compose

1. [Install Docker Compose](https://docs.docker.com/compose/install/)
1. Run all containers with `docker-compose up`

## Start
In the beginning the program will get a fresh categories list, it occupies some time.

## List of routers:

- to get a list of product categories add to IP this string: `/get_categories`
- to get all products list add this: `/get_all_products`
- to get product by name use: `/get_products_by_category/<name>`
- to get product by name use: `/get_products_by_name/<name>`

This is the scrub program for one of popular website.


## Start
Firstly, all base information is saves in json file. To update it, please use tag '/get_all_products'

## List of routers:

- get all products and update a json, like described before, use '/get_all_products'
- to get a list of product categories, use tag '/get_categories'




