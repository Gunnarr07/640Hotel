from random import randint


class Key(object):
    "Key used in keycards and locks"

    keycard = randint(1, 1000)
    lock = randint(1, 10000)
    pass


class KeyCard(object):
    "Keycard used to open a lock"

    def __init__(self, first_key, second_key):
        "Constructs a KeyCard with the given keys"
        self._first_key = first_key
        self._second_key = second_key

    @property
    def first_key(self):
        "Provides the first key of this keycard"
        return self.first_key

    @property
    def second_key(self):
        "Provides the second key of this keycard"
        return self.second_key


class Lock(object):
    "Lock on a room door"

    def __init__(self, first_key, second_key):
        "Constructs a Lock with the given keys"
        self.first_key = first_key
        self.second_key = second_key

    def can_be_unlocked(self, keycard):
        """
        Checks if this lock can be unlocked with the given keycard

        Return:
            True if the lock can be unlocked; False otherwise
        """
        pass


class Room(object):
    "Room in a hotel"

    def __init__(self, room_number, lock):
        "Constructs a Room with given number and lock"
        self._room_number = room_number
        self._lock = lock
        self._is_available = True

    @property
    def room_number(self):
        "Provides the number of this room"
        return self.room_number

    @property
    def lock(self):
        "Provides the lock for this room"
        return self.lock

    def is_available(self):
        return self._is_available


class Guest(object):
    "Guest at a hotel"
    def __init__(self, guest_name, room_number, keycard):
        self._guest_name = guest_name
        self._room_number = room_number
        self._keycard = keycard

    @property
    def guest_name(self):
        "Provides the name of this guest"
        return self.guest_name

    @property
    def keycard(self):
        "Provides the keycard of this guest"
        return self.keycard

    @property
    def room_number(self):
        "Provides the number of the room occupied by this guest"
        return self.room_number

    def is_checkedin(self, hotel):
        "Checks if this guest is checked into this hotel"
        pass


class Hotel(object):
    "Hotel"

    def __init__(self, N):
        "Constructs a Hotel with N rooms"
        self.N = N
        self.available = [(i, False, True) for i in range(1, N+1)]
        self.rooms = [{i: None} for i in range(1, N+1)]

    def checkin(self, guest_name):
        """
        Checks the guest into the hotel by allocating a room

        Return:
            the corresponding Guest
        """
        # room_number = randint(1, self.N)
        #for i in self.rooms:
        #    if i

        keycard = KeyCard()
        guest = Guest(guest_name, room_number, keycard)
        pass

    def is_checkedin(self, guest_name):
        """
        Checks if the guest is a guest at this Hotel

        Return:
            True if the guest is checked in at this Hotel; False otherwise
        """
        pass

    def checkout(self, guest_name):
        "Checks out the guest from the hotel"
        pass

    def room_of(self, guest_name):
        """
        Provides the room for the guest

        Return:
            the corresponding Room
        """

        pass

