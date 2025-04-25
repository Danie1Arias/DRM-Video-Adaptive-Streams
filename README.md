# MPEG-DASH server and video player

In this example we set up a basic HTTPS servar that serves an adaptive and DRM-protected video streaming using MPEG-DASH and common encryption (CENC). Additionally, the basic player relies on W3C standards Encrypted Media Extensions and Google's Shaka Player.

## Instructions

1. Start the server using the following command:
```bash
python server.py
```

2. Open the following URI in a browser:
```bash
https://localhost:4443/indexTest.html
```

3. Introduce the desired credentials:

- Elephant

Manifest:
```bash
output_elephants.mpd
```

KID:
```bash
cd7eb9ff88f34caeb06185b00024e4c2
```

KEY:
```bash
63cb5f7184dd4b689a5c5ff11ee6a328
```

- Popeye:
Manifest:
```bash
output_popeye.mpd
```

KID:
```bash
f94bd269772b420c886b7b29f017d3a9
```

KEY:
```bash
0c2cf7dd02fcbfe80f3ccb066184f611
```

- Pokemon:
Manifest:
```bash
output_pokemon.mpd
```

KID:
```bash
754b0c76f7494e94bb47065ff855c2d5
```

KEY:
```bash
ddf8cbb8af7fd2234bd90f0671999f27
```

> [!NOTE]
> KIDs and KEYs have been generated using PBKDF2 encryption, implemented in PBKDF2.py



