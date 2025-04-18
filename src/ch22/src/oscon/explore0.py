"""
explore0.py: Script to explore the OSCON schedule feed

# tag::EXPLORE0_DEMO[]
    >>> import json
    >>> raw_feed = json.load(open('data/osconfeed.json'))
    >>> feed = FrozenJSON(raw_feed)
    >>> feed.keys()
    dict_keys(['Schedule'])
    >>> list(feed.Schedule.keys())
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in sorted(feed.Schedule.items()):
    ...     print(f'{len(value):3} {key}')
    ...
      1 conferences
    484 events
    357 speakers
     53 venues
    >>> feed.Schedule.speakers[-1].name
    'Carina C. Zona'
    >>> talk = feed.Schedule.events[40]
    >>> type(talk)  # <6>
    <class 'explore0.FrozenJSON'>
    >>> talk.name
    'There *Will* Be Bugs'
    >>> talk.speakers  # <7>
    [3471, 5199]
    >>> talk.flavor  # <8>
    Traceback (most recent call last):
      ...
    AttributeError: flavor

# end::EXPLORE0_DEMO[]

"""
from __future__ import annotations
from collections import abc


class FrozenJSON:
    def __init__(self, input):
        self.__data = input


    def __getattr__(self, attr):
        try:
            return getattr(self.__data, attr)
        except AttributeError:
            try:
                return FrozenJSON.build(self.__data[attr])
            except KeyError:
                raise AttributeError(attr)


    def __dir__(self):
        # TODO: figure out the annotations here
        if isinstance(self.__data, abc.Mapping):
            return self.__data.keys() + dir(self.__data)
        return dir(self.__data)

    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(val) for val in obj]
        else:
            return obj
