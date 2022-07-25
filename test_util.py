from datetime import datetime, timezone
from unittest import TestCase

from util import datetime_to_iso


class Test(TestCase):
    def test_datetime_to_iso(self):
        dt: datetime = datetime(year=2022, month=1, day=5, hour=23, minute=22, second=42, microsecond=123456,
                                tzinfo=timezone.utc)
        formatted: str = datetime_to_iso(dt)

        self.assertEqual('2022-01-05T23:22:42', formatted)
