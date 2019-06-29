# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 14:14:12 2019

@author: NEX2BZR
"""

from automobile import Automobile

all_vehicles = []


def add_vehicle(all_vehicles):
    make = input('Enter make : ')
    model = input('Enter model : ')
    color = input('Enter color : ')
    year = int(input('Enter year : '))
    mileage = int(input('Enter mileage : '))
    vehicle_id = len(all_vehicles)
    automobile = Automobile(vehicle_id, make, model, color, year, mileage)
    print('Vehice added with id : ' + str(vehicle_id))
    all_vehicles.append(automobile)


def remove_vehicle(all_vehicles, vehicle_id=-1):
    if vehicle_id == -1:
        vehicle_id = int(input('Enter vehicle id to remove : '))
    for vehicle in all_vehicles:
        if vehicle.vehicle_id == vehicle_id:
            all_vehicles.remove(vehicle)
            print('Vehicle Deleted ')
            return True
    return False


def update_vehicle(all_vehicles):
    v_id = int(input('Enter vehicle id to update'))
    if (remove_vehicle(all_vehicles, v_id)):
        print('Add new details')
        add_vehicle(all_vehicles)
    else:
        print('No id found ')


def show_menu():
    print(
        '1. Add Vehicle \n 2. Remove Vehicle \n 3.Display all vehicles \n 4. Write all vehicles to file '
        '\n 5. Update Vehicle')
    choice = int(input('Enter the corresponding number, enter any other key to exit : '))
    return choice


if __name__ == "__main__":
    shallRun = True
    while (shallRun):
        print('menu')
        try:
            choice = show_menu()
        except TypeError:
            continue
        if choice == 1:
            add_vehicle(all_vehicles)
        elif choice == 2:
            remove_vehicle(all_vehicles)
        elif choice == 3:
            for vehicle in all_vehicles:
                print(str(vehicle))
        elif choice == 4:
            all_str = ''
            f = open('details.txt', 'w')
            for vehicle in all_vehicles:
                all_str = all_str + str(vehicle) + '\n'
            f.write(all_str)
            f.close()
        elif choice == 5:
            update_vehicle(all_vehicles)
        else:
            shallRun = False
