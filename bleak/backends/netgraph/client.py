# -*- coding: utf-8 -*-
"""
BLE Client for Netgraph on FreeBSD
"""
import asyncio
import logging
import os
import sys
import uuid
import warnings

import socket
import ctypes
import ctypes.util

from typing import Callable, Dict, Optional, Set, Union, cast
from uuid import UUID

# todo
libc = ctypes.cdll.LoadLibrary("libc.so.7")
libbt = ctypes.CDLL(str(ctypes.util.find_library("bluetooth")))

if sys.version_info < (3, 11):
    from async_timeout import timeout as async_timeout
else:
    from asyncio import timeout as async_timeout

from ... import BLEDevice
from ..characteristic import BleakGATTCharacteristic
from ..client import BaseBleakClient, NotifyCallback
from ..service import BleakGATTServiceCollection

logger = logging.getLogger(__name__)


class BleakClientNetgraph(BaseBleakClient):
    """A native FreeBSD Bleak Client

        Implemented by using the Netgraph API.

        Args:
            address_or_ble_device (`BLEDevice` or str): The Bluetooth address of the BLE peripheral to connect to
                or the `BLEDevice` object representing it.
            services: Optional list of service UUIDs that will be used.

        Keyword Args:
            timeout (float): Timeout for required ``BleakScanner.find_device_by_address`` call. Defaults to 10.0.
            disconnected_callback (callable): Callback that will be scheduled in the
                event loop when the client is disconnected. The callable must take one
                argument, which will be this client object.
            adapter (str): Bluetooth adapter to use for discovery.
        """

    def __init__(
        self,
        address_or_ble_device: Union[BLEDevice, str],
        services: Optional[Set[str]] = None,
        **kwargs,
    ):
        super(BleakClientNetgraph, self).__init__(address_or_ble_device, **kwargs)
        # kwarg "device" is for backwards compatibility
        self._adapter: Optional[str] = kwargs.get("adapter", kwargs.get("device"))

    @property
    def mtu_size(self) -> int:
        pass

    async def connect(self, **kwargs) -> bool:
        pass

    async def disconnect(self) -> bool:
        pass

    async def pair(self, *args, **kwargs) -> bool:
        pass

    async def unpair(self) -> bool:
        pass

    @property
    def is_connected(self) -> bool:
        pass

    async def get_services(self, **kwargs) -> BleakGATTServiceCollection:
        pass

    async def read_gatt_char(self, char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID],
                             **kwargs) -> bytearray:
        pass

    async def read_gatt_descriptor(self, handle: int, **kwargs) -> bytearray:
        pass

    async def write_gatt_char(self, char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID],
                              data: Union[bytes, bytearray, memoryview], response: bool = False) -> None:
        pass

    async def write_gatt_descriptor(self, handle: int, data: Union[bytes, bytearray, memoryview]) -> None:
        pass

    async def start_notify(self, characteristic: BleakGATTCharacteristic, callback: NotifyCallback, **kwargs) -> None:
        pass

    async def stop_notify(self, char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID]) -> None:
        pass
