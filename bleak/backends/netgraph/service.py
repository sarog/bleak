from typing import List

from ..service import BleakGATTService
from .characteristic import BleakGATTCharacteristicNetgraph

# from .utils import extract_service_handle_from_path


class BleakGATTServiceNetgraph(BleakGATTService):
    """GATT Service implementation for the Netgraph backend"""

    def __init__(self, obj, path):
        super().__init__(obj)
        self.__characteristics = []
        self.__path = path
        # self.__handle = extract_service_handle_from_path(path)

    @property
    def uuid(self) -> str:
        """The UUID to this service"""
        return self.obj["UUID"]

    @property
    def handle(self) -> int:
        """The integer handle of this service"""
        return self.__handle

    @property
    def characteristics(self) -> List[BleakGATTCharacteristicNetgraph]:
        """List of characteristics for this service"""
        return self.__characteristics

    def add_characteristic(self, characteristic: BleakGATTCharacteristicNetgraph):
        """Add a :py:class:`~BleakGATTCharacteristicNetgraph` to the service.

        Should not be used by end user, but rather by `bleak` itself.
        """
        self.__characteristics.append(characteristic)

    @property
    def path(self):
        """The DBus path. Mostly needed by `bleak`, not by end user"""
        return self.__path
