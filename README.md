# vt-scan.py

## A python script for use in [Termux](https://f-droid.org/packages/com.termux) to scan all installed apps with [Virustotal](https://www.virustotal.com) on Android.

**Work In Progress**

---

## Installation

1. Install dependencies:

```
pkg upd && pkg i python git -y && pip install os argparse vt-py
```

2. Download the script:

```
  git clone https://github.com/Green0Field/vt-scan.py.git

```

_There maybe some more installation steps when more features are added._

## Usage

Before using, you must get an api key from Virustotal:

1. [Create](https://www.virustotal.com/gui/join-us) or [signin](https://www.virustotal.com/gui/sign-in) to an account
2. Get an Api key [here](https://www.virustotal.com/gui/my-apikey)
3. Create a configuration file called conf.py (which is imported by main.py) and set a variable called `API_KEY` to your api key, like this: `API_KEY = "your-api-key"`

_The configuration file may have more options when more features are added._

---

### Get the apks for every installed app, then scan them

```

python main.py

```

### Only get the apks for every installed app

```

python main.py -a

```

### Only scan the apks (will error if they dont exist)

```

python main.py -s

```

## Todos

- [ ] Make it scan files
- [ ] Add a GUI with [Termux:GUI](https://f-droid.org/packages/com.termux.gui)
