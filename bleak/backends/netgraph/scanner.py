import logging
import sys
from typing import Callable, Coroutine, Dict, List, Optional
from warnings import warn

# from dbus_fast import Variant

if sys.version_info[:2] < (3, 8):
    from typing_extensions import Literal, TypedDict
else:
    from typing import Literal, TypedDict

from ...exc import BleakError
from ..scanner import AdvertisementData, AdvertisementDataCallback, BaseBleakScanner


logger = logging.getLogger(__name__)

class BleakScannerNetgraph(BaseBleakScanner):
    """The native FreeBSD Bleak BLE Scanner.

    Args:
        detection_callback:
            Optional function that will be called each time a device is
            discovered or advertising data has changed.
        service_uuids:
            Optional list of service UUIDs to filter on. Only advertisements
            containing this advertising data will be received. Specifying this
            also enables scanning while the screen is off on Android.
        scanning_mode:
            Set to ``"passive"`` to avoid the ``"active"`` scanning mode.
        **adapter (str):
            Bluetooth adapter to use for discovery.
    """
    def __init__(
        self,
        detection_callback: Optional[AdvertisementDataCallback],
        service_uuids: Optional[List[str]],
        scanning_mode: Literal["active", "passive"],
        **kwargs,
    ):
        super(BleakScannerNetgraph, self).__init__(detection_callback, service_uuids)

        self._scanning_mode = scanning_mode

        # kwarg "device" is for backwards compatibility
        self._adapter: Optional[str] = kwargs.get("adapter", kwargs.get("device"))

        # callback from manager for stopping scanning if it has been started
        self._stop: Optional[Callable[[], Coroutine]] = None

    async def start(self) -> None:
        pass

    async def stop(self) -> None:
        pass

    def set_scanning_filter(self, **kwargs) -> None:
        pass

