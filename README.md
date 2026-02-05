   Aggregation in Python (OOP Basics)
   
    **********Overview

This project demonstrates aggregation in Object-Oriented Programming (OOP) using Python.

Aggregation is a relationship where one class contains objects of another class, but both can exist independently.

 *****   In this example:

A Farm has many Animal objects

Animals can exist without the Farm

The Farm manages a collection of Animals but does not own their lifecycle

=>: What Is Aggregation? 

Aggregation describes a “has-a” relationship.

    A Farm has animals
    A School has students
    A Library has books

Key idea:

    The container class stores objects in a list

    The contained objects keep their own data

    The container does not inherit from the contained class 