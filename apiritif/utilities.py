"""
Public utility functions for Apiritif

Copyright 2017 BlazeMeter Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import random
import re
import string
from datetime import datetime


def random_uniform(start, stop=None):
    return random.randrange(start, stop=stop)


def random_normal(sigma, mu):
    return random.gauss(sigma, mu)


def random_string(size, chars=string.printable):
    return "".join(random.choice(chars) for _ in range(size))


class SimpleDateFormat(object):
    def __init__(self, format):
        self.format = format

    @staticmethod
    def _replacer(match):
        what = match.group(0)
        if what.startswith("y") or what.startswith("Y"):
            if len(what) < 4:
                return "%y"
            else:
                return "%Y"
        elif what.startswith("M"):
            return "%m"
        elif what.startswith("d"):
            return "%d"
        elif what.startswith("h"):
            return "%I"
        elif what.startswith("H"):
            return "%H"
        elif what.startswith("m"):
            return "%M"
        elif what.startswith("s"):
            return "%S"
        elif what.startswith("S"):
            return what
        elif what.startswith("E"):
            if len("E") <= 3:
                return "%a"
            else:
                return "%A"
        elif what.startswith("D"):
            return "%j"
        elif what.startswith("w"):
            return "%U"
        elif what.startswith("a"):
            return "%p"
        elif what.startswith("z"):
            return "%z"
        elif what.startswith("Z"):
            return "%Z"

    def format_datetime(self, datetime):
        letters = "yYMdhHmsSEDwazZ"  # TODO: moar
        regex = "(" + "|".join(letter + "+" for letter in letters) + ")"
        strftime_fmt = re.sub(regex, self._replacer, self.format)
        return datetime.strftime(strftime_fmt)


def format_date(format_string, datetime_obj=None):
    formatter = SimpleDateFormat(format_string)
    datetime_obj = datetime_obj or datetime.now()
    return formatter.format_datetime(datetime_obj)
