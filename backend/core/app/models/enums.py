from enum import Enum


class ConnectionStatus(str, Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    BLOCKED = "Blocked"


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    NON_BINARY = "Non-Binary"
    TRANSGENDER = "Transgender"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer Not To Say"
