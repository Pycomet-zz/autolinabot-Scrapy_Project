# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutolinabotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    VEHICLE_NAME = scrapy.Field()
    BODY_STYLE = scrapy.Field()
    CONDITION = scrapy.Field()
    COLOUR = scrapy.Field()
    MILEAGE = scrapy.Field()
    TRANSMISSION = scrapy.Field()
    DRIVETRAIN = scrapy.Field()
    FUEL_TYPE = scrapy.Field()
    POWER = scrapy.Field()
    CUBIC_CAPACITY = scrapy.Field()
    DOORS = scrapy.Field()
    INTERIOR_COLOUR = scrapy.Field()
    FUEL_CONSUMPTION = scrapy.Field()
    CO2_EMISSIONS = scrapy.Field()
    NUMBER_OF_GEARS = scrapy.Field()
    SEATS = scrapy.Field()
    CYLINDERS = scrapy.Field()
    GROSS_VEHICLE_WEIGHT = scrapy.Field()
    KERB_WEIGHT = scrapy.Field()
    TYPE_APPROVAL_NUMBER = scrapy.Field()
    CHASSIS_NUMBER = scrapy.Field()
    CAR_NUMBER = scrapy.Field()
    PRICE = scrapy.Field()
    URL = scrapy.Field()

