# -*- coding: utf-8 -*-

import sys
from typing import Dict, List, Tuple

if sys.version_info[:2] < (3, 8):
    from typing_extensions import Literal, TypedDict
else:
    from typing import Literal, TypedDict


class Adapter1(TypedDict):
    Address: str
    Name: str
    Alias: str
    Class: int
    Powered: bool
    Discoverable: bool
    Pairable: bool
    PairableTimeout: int
    DiscoverableTimeout: int
    Discovering: int
    UUIDs: List[str]
    Modalias: str
    Roles: List[str]
    ExperimentalFeatures: List[str]


# https://github.com/bluez/bluez/blob/master/doc/advertisement-monitor-api.txt


class AdvertisementMonitor1(TypedDict):
    Type: str
    RSSILowThreshold: int
    RSSIHighThreshold: int
    RSSILowTimeout: int
    RSSIHighTimeout: int
    RSSISamplingPeriod: int
    Patterns: List[Tuple[int, int, bytes]]


class AdvertisementMonitorManager1(TypedDict):
    SupportedMonitorTypes: List[str]
    SupportedFeatures: List[str]


# https://github.com/bluez/bluez/blob/master/doc/battery-api.txt


class Battery1(TypedDict):
    SupportedMonitorTypes: List[str]
    SupportedFeatures: List[str]


# https://github.com/bluez/bluez/blob/master/doc/device-api.txt


class Device1(TypedDict):
    Address: str
    AddressType: str
    Name: str
    Icon: str
    Class: int
    Appearance: int
    UUIDs: List[str]
    Paired: bool
    Bonded: bool
    Connected: bool
    Trusted: bool
    Blocked: bool
    WakeAllowed: bool
    Alias: str
    Adapter: str
    LegacyPairing: bool
    Modalias: str
    RSSI: int
    TxPower: int
    ManufacturerData: Dict[int, bytes]
    ServiceData: Dict[str, bytes]
    ServicesResolved: bool
    AdvertisingFlags: bytes
    AdvertisingData: Dict[int, bytes]


# https://github.com/bluez/bluez/blob/master/doc/gatt-api.txt


class GattService1(TypedDict):
    UUID: str
    Primary: bool
    Device: str
    Includes: List[str]
    # Handle is server-only and not available in Bleak


class GattCharacteristic1(TypedDict):
    UUID: str
    Service: str
    Value: bytes
    WriteAcquired: bool
    NotifyAcquired: bool
    Notifying: bool
    Flags: List[
        Literal[
            "broadcast",
            "read",
            "write-without-response",
            "write",
            "notify",
            "indicate",
            "authenticated-signed-writes",
            "extended-properties",
            "reliable-write",
            "writable-auxiliaries",
            "encrypt-read",
            "encrypt-write",
            # "encrypt-notify" and "encrypt-indicate" are server-only
            "encrypt-authenticated-read",
            "encrypt-authenticated-write",
            # "encrypt-authenticated-notify", "encrypt-authenticated-indicate",
            # "secure-read", "secure-write", "secure-notify", "secure-indicate"
            # are server-only
            "authorize",
        ]
    ]
    MTU: int
    # Handle is server-only and not available in Bleak


class GattDescriptor1(TypedDict):
    UUID: str
    Characteristic: str
    Value: bytes
    Flags: List[
        Literal[
            "read",
            "write",
            "encrypt-read",
            "encrypt-write",
            "encrypt-authenticated-read",
            "encrypt-authenticated-write",
            # "secure-read" and "secure-write" are server-only and not available in Bleak
            "authorize",
        ]
    ]
    # Handle is server-only and not available in Bleak
