<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/dotzenith/AvatarAPI?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/dotzenith/AvatarAPI?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/workflow/status/dotzenith/AvatarAPI/Tests?color=ABE9B3&labelColor=302D41&style=for-the-badge&label=Tests"/>
   
   <img src="https://img.shields.io/github/workflow/status/dotzenith/AvatarAPI/Deployment?color=ABE9B3&labelColor=302D41&style=for-the-badge&label=Deployment"/>
   <br>
</div>

<p/>

---

### ❖ Information 

AvatarAPI, simply put, is a free API serving quotes from Avatar: The Last Airbender. The quotes are sourced from [AvatarQuotes](https://github.com/dotzenith/AvatarQuotes/) and the endpoints are available at https://avatarquotes.xyz/api/{endpoint} (See [Usage](#Usage) for the different endpoints)

<img src="https://github.com/dotzenith/dotzenith/blob/main/assets/AvatarQuotes/AvatarQuotes.gif" alt="lovesay gif">

---

### ❖ Usage

AvatarAPI has a few different endpoints for different needs but the usage is relatively the same for all of them. The examples use [httpie](https://httpie.io/) but anything that can make GET requests can be used as well

#### ❖ `/api/quotes`

Fetches 10 random quotes 

```
$ http GET https://avatarquotes.xyz/api/quotes
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "...",
            "Bending": "...",
            "Episode": "...",
            "Book": "...",
        },
        "...9 more"
    ]
}
```

<b></b>

#### ❖ `/api/quotes/character`

Fetches 10 random quotes from a given character

```
$ http GET https://avatarquotes.xyz/api/quotes/character name==Aang
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "Aang",
            "Nation": "...",
            "Bending": "...",
            "Episode": "...",
            "Book": "...",
        },
        "...9 more"
    ]
}
```

<details>
<summary><strong>Allowed values for character name</strong></summary>

```
"Katara", "Sokka", "Zuko", "Merchant woman", "Aang",
"Fisherman's wife", "Fisherman", "Jee", "Iroh", "Tashi", "Pasang",
"Gyatso", "Ozai", "Yue", "Pakku", "Oh", "Pirate captain",
"Cabbage merchant", "Gan Jin tribesman", "Zhang leader",
"Gan Jin leader", "Canyon guide", "Hakoda", "Bato", "Chey",
"Jeong Jeong", "Bumi", "Jet", "Kanna", "Southern Water Tribe girl",
"Mechanist", "Haru", "Guard", "Tyro", "Captain", "Warden", "Suki",
"Meng", "Wu", "Zhao", "Kay-fon", "Senlin Village leader",
"Earthbender captain", "Great Fire Sage", "Shyu", "Roku", "Arnook",
"Hahn", "Koh", "Chong", "Lily", "Song", "Tho", "Huu", "Due",
"Tong", "Kyoshi", "Zei", "Toph", "Wan Shi Tong", "Ticket lady",
"Ying", "Smellerbee", "jet", "Azula", "Fong", "Kuei",
"Guru Pathik", "Ty Lee", "Mai", "Kenji", "Macmu-Ling", "Joo Dee",
"Long Feng", "General Sung", "Pong", "Yu", "The Boulder", "Yung",
"Iio", "Lee", "Gansu", "Ursa", "Kwan", "Piandao", "Kuruk",
"Yangchen", "Lion Turtle", "Hama", "Momo", "Appa"
```

</details>

<b></b>

#### ❖ `/api/quotes/nation`

Fetches 10 random quotes by characters from a given nation

```
$ http GET https://avatarquotes.xyz/api/quotes/nation name==Fire
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "Fire",
            "Bending": "...",
            "Episode": "...",
            "Book": "...",
        },
        "...9 more"
    ]
}
```

<details>
<summary><strong>Allowed values for nation name</strong></summary>

```
"Water", "Earth", "Fire", "Air", "None"
```
> Some characters like Guru Pathik, don't belong to a specific nation, thus the addition of "None"

</details>


#### ❖ `/api/quotes/bending`

Fetches 10 random quotes by characters with a given bending style

```
$ http GET https://avatarquotes.xyz/api/quotes/bending type==Earth
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "...",
            "Bending": "Earth",
            "Episode": "...",
            "Book": "...",
        },
        "...9 more"
    ]
}
```

<details>
<summary><strong>Allowed values for bending type</strong></summary>

```
"Water", "Earth", "Fire", "Air", "None", "All"
```
> Characters like Sokka have bending type "None", while characters like Aang have bending type "All"

</details>

<b></b>

#### ❖ `/api/quotes/episode`

Fetches 10 random quotes from a given episode

```
$ http GET https://avatarquotes.xyz/api/quotes/episode title==Imprisoned
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "...",
            "Bending": "...",
            "Episode": "Imprisoned",
            "Book": "...",
        },
        "...9 more"
    ]
}
```

<details>
<summary><strong>Allowed values for episode title</strong></summary>

```
"The Storm", "The Waterbending Master", "The Waterbending Scroll",
"The Great Divide", "Bato of the Water Tribe", "The Deserter",
"The King of Omashu", "Jet", "The Avatar Returns",
"The Northern Air Temple", "The Boy in the Iceberg", "Imprisoned",
"The Warriors of Kyoshi", "The Fortuneteller",
"The Southern Air Temple",
"Winter Solstice Part 1: The Spirit World",
"Winter Solstice Part 2: Avatar Roku",
"The Siege of the North, Part 1", "The Siege of the North, Part 2",
"The Blue Spirit", "The Cave of Two Lovers", "The Swamp",
"Avatar Day", "The Library", "The Serpent's Pass",
"The Avatar State", "The Guru", "The Tales of Ba Sing Se",
"Lake Laogai", "Bitter Work", "The Earth King", "The Drill",
"City of Walls and Secrets", "The Blind Bandit", "The Chase",
"The Crossroads of Destiny", "Return to Omashu",
"Appa's Lost Days", "The Desert", "Zuko Alone",
"The Firebending Masters", "The Awakening", "The Headband",
"The Western Air Temple", "The Runaway",
"The Day of Black Sun, Part 1: The Invasion", "The Beach",
"The Boiling Rock, Part 2",
"Sozin's Comet, Part 2: The Old Masters", "The Painted Lady",
"Sozin's Comet, Part 4: Avatar Aang",
"Sozin's Comet, Part 1: The Phoenix King", "The Puppetmaster",
"The Boiling Rock, Part 1", "Nightmares and Daydreams",
"The Avatar and The Fire Lord",
"The Day of Black Sun, Part 2: The Eclipse",
"Sozin's Comet, Part 3: Into the Inferno", "Sokka's Master",
"The Southern Raiders", "The Ember Island Players"
```

</details>

<b></b>

#### ❖ `/api/quotes/book`

Fetches 10 random quotes from a given book

```
$ http GET https://avatarquotes.xyz/api/quotes/book title==Water
```

```json
{
    "num": 10,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "...",
            "Bending": "...",
            "Episode": "...",
            "Book": "Water",
        },
        "...9 more"
    ]
}
```

<details>
<summary><strong>Allowed values for book title</strong></summary>

```
"Water", "Earth", "Fire"
```

</details>

<b></b>

#### ❖ Using the `num` url parameter

All of the endpoints above support an optional url parameter of `num` to specify the number of quotes to return

```
$ http GET https://avatarquotes.xyz/api/quotes num==5
```

```json
{
    "num": 5,
    "quotes": [
        {
            "Quote": "..."
            "Character": "...",
            "Nation": "...",
            "Bending": "...",
            "Episode": "...",
            "Book": "...",
        },
        "...4 more"
    ]
}
```

`num` can take on the values `1 <= num <= 25`

<b></b>

#### ❖ The `response.num` field

The response from all of the endpoints includes the `response.num` field, which simply specifies the number of quotes returned. A natural question to ask is "Well why is that needed, shouldn't it just be 10 in the default case, or equal to `num` in case the `num` parameter was passed in?"

The answer is "well yes but no".

For example, some characters like Koh only have 2 quotes. So even without the `num` parameter, we run into some issues. This is why the API just returns as many quotes it can and updates the `response.num` field in the case that `num` is too large for the given endpoint.

The `response.num` field exists as a sanity check. Users can confirm that they got the number of quotes they requested, or implement special logic in case it's different.

---

### ❖ Rate Limiting

AvatarAPI currently allows 100 requests per hour from a given IP address. In case you desire more, feel free to take a look at the [Self Hosting](#Self-Hosting) section.

---

### ❖ Self Hosting

AvatarAPI is relatively easy to self-host. The only requirements are [Docker](https://www.docker.com/), [Git](https://git-scm.com/) and pretty much any webserver, for example: [nginx](https://www.nginx.com/)

#### ❖ Clone repo with submodules and cd into it 

```
$ git clone --recurse-submodules https://github.com/dotzenith/AvatarAPI.git
$ cd AvatarAPI
```

<b></b>

#### ❖ Build docker image

```
$ docker build -t avatarapi:latest .
```

#### ❖ Run the container

```
$ docker run -p 5000:5000 -d --name avatarapi avatarapi:latest
```

#### ❖ Set up a reverse proxy

After the step above, set up a reverse proxy using a webserver of your choice and enjoy your very own AvatarAPI :)

---

### ❖ What's New?

0.1.0 - Initial Release

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>

