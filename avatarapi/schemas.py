"""
Module for importing quotes and setting up valid options for different fields
"""
from typing import Literal

from pydantic import BaseModel

# Valid options for various fields
Characters = Literal[
    "Katara",
    "Sokka",
    "Zuko",
    "Merchant woman",
    "Aang",
    "Fisherman's wife",
    "Fisherman",
    "Jee",
    "Iroh",
    "Tashi",
    "Pasang",
    "Gyatso",
    "Ozai",
    "Yue",
    "Pakku",
    "Oh",
    "Pirate captain",
    "Cabbage merchant",
    "Gan Jin tribesman",
    "Zhang leader",
    "Gan Jin leader",
    "Canyon guide",
    "Hakoda",
    "Bato",
    "Chey",
    "Jeong Jeong",
    "Bumi",
    "Jet",
    "Kanna",
    "Southern Water Tribe girl",
    "Mechanist",
    "Haru",
    "Guard",
    "Tyro",
    "Captain",
    "Warden",
    "Suki",
    "Meng",
    "Wu",
    "Zhao",
    "Kay-fon",
    "Senlin Village leader",
    "Earthbender captain",
    "Great Fire Sage",
    "Shyu",
    "Roku",
    "Arnook",
    "Hahn",
    "Koh",
    "Chong",
    "Lily",
    "Song",
    "Tho",
    "Huu",
    "Due",
    "Tong",
    "Kyoshi",
    "Zei",
    "Toph",
    "Wan Shi Tong",
    "Ticket lady",
    "Ying",
    "Smellerbee",
    "jet",
    "Azula",
    "Fong",
    "Kuei",
    "Guru Pathik",
    "Ty Lee",
    "Mai",
    "Kenji",
    "Macmu-Ling",
    "Joo Dee",
    "Long Feng",
    "General Sung",
    "Pong",
    "Yu",
    "The Boulder",
    "Yung",
    "Iio",
    "Lee",
    "Gansu",
    "Ursa",
    "Kwan",
    "Piandao",
    "Kuruk",
    "Yangchen",
    "Lion Turtle",
    "Hama",
    "Momo",
    "Appa",
]

Nations = Literal["Water", "Earth", "Fire", "Air", "None"]

Bendings = Literal["Water", "Earth", "Fire", "Air", "None", "All"]

Episodes = Literal[
    "The Storm",
    "The Waterbending Master",
    "The Waterbending Scroll",
    "The Great Divide",
    "Bato of the Water Tribe",
    "The Deserter",
    "The King of Omashu",
    "Jet",
    "The Avatar Returns",
    "The Northern Air Temple",
    "The Boy in the Iceberg",
    "Imprisoned",
    "The Warriors of Kyoshi",
    "The Fortuneteller",
    "The Southern Air Temple",
    "Winter Solstice Part 1: The Spirit World",
    "Winter Solstice Part 2: Avatar Roku",
    "The Siege of the North, Part 1",
    "The Siege of the North, Part 2",
    "The Blue Spirit",
    "The Cave of Two Lovers",
    "The Swamp",
    "Avatar Day",
    "The Library",
    "The Serpent's Pass",
    "The Avatar State",
    "The Guru",
    "The Tales of Ba Sing Se",
    "Lake Laogai",
    "Bitter Work",
    "The Earth King",
    "The Drill",
    "City of Walls and Secrets",
    "The Blind Bandit",
    "The Chase",
    "The Crossroads of Destiny",
    "Return to Omashu",
    "Appa's Lost Days",
    "The Desert",
    "Zuko Alone",
    "The Firebending Masters",
    "The Awakening",
    "The Headband",
    "The Western Air Temple",
    "The Runaway",
    "The Day of Black Sun, Part 1: The Invasion",
    "The Beach",
    "The Boiling Rock, Part 2",
    "Sozin's Comet, Part 2: The Old Masters",
    "The Painted Lady",
    "Sozin's Comet, Part 4: Avatar Aang",
    "Sozin's Comet, Part 1: The Phoenix King",
    "The Puppetmaster",
    "The Boiling Rock, Part 1",
    "Nightmares and Daydreams",
    "The Avatar and The Fire Lord",
    "The Day of Black Sun, Part 2: The Eclipse",
    "Sozin's Comet, Part 3: Into the Inferno",
    "Sokka's Master",
    "The Southern Raiders",
    "The Ember Island Players",
]

Books = Literal["Water", "Earth", "Fire"]


class QuoteModel(BaseModel):
    """
    A representation of a quote object
    """

    Quote: str
    Character: Characters
    Nation: Nations
    Bending: Bendings
    Episode: Episodes
    Book: Books


class ReturnQuotes(BaseModel):
    """
    A simple class to act as the response_model
    """

    num: int
    quotes: list[QuoteModel]
