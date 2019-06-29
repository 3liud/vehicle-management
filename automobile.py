# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:10:41 2019

@author: NEX2BZR
"""


class Automobile:
    def __init__(self, vehicle_id, make, model, color, year, mileage):
        self.vehicle_id = vehicle_id
        self.make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_color(self, color):
        self.__color = color

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_make(self):
        return self.make

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def __str__(self):
        out_str = "Make:" + self.get_make() + " Color:" + self.get_color() + " Model:" + \
            self.get_model() + " Year: " + str(self.get_year()) + \
            " Mileage:" + str(self.get_mileage())
        return out_str

    def __repr__(self):
        out_str = "Make:" + self.get_make() + " Color:" + self.get_color() + " Model:" + \
            self.get_model() + " Year: " + str(self.get_year()) + \
            " Mileage:" + str(self.get_mileage())
        return out_str
