# -*- coding: utf-8 -*-
class DriverTypeNotSupportException(Exception):
    def __init__(self, driver_type: str) -> None:
        self.__driver_type = driver_type

    def __str__(self) -> str:
        # return f"Browser name : {self.__browser} are not Support, please choose chrome, firefox, or edge."
        return f"Driver type : {self.__driver_type} are not Support, please choose chrome."


class NoIDException():
    pass
