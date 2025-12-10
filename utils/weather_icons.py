from rich.console import Console

import emoji

# Nerd Font Weather icons (monospace-safe)
NERD_WEATHER_ICONS = {
    1000: "\uf00d",  # Sunny ()
    1003: "\uf002",  # Partly cloudy ()
    1006: "\uf013",  # Cloudy ()
    1009: "\uf014",  # Overcast ()
    1030: "\uf003",  # Mist ()
    1135: "\uf003",  # Fog ()
    1147: "\uf003",  # Freezing fog ()
    1063: "\uf008",  # Patchy rain ()
    1180: "\uf008",
    1183: "\uf009",  # Light rain ()
    1186: "\uf009",
    1189: "\uf009",
    1192: "\uf00a",  # Heavy rain ()
    1195: "\uf00a",
    1066: "\uf00b",  # Snow ()
    1210: "\uf00b",
    1213: "\uf00b",
    1216: "\uf076",  # Snowflake ()
    1219: "\uf076",
    1222: "\uf076",
    1225: "\uf076",
    1087: "\uf010",  # Thunderstorm ()
    1273: "\uf010",
    1276: "\uf00e",  # Lightning + rain ()
}

# Fallback emoji if Nerd Font isn't supported
FALLBACK_EMOJI = {
    1000: ":sun:",
    1003: ":sun_behind_cloud:",
    1006: ":cloud:",
    1009: ":fog:",
    1030: ":fog:",
    1135: ":fog:",
    1147: ":fog:",
    1063: ":sun_behind_rain_cloud:",
    1180: ":sun_behind_rain_cloud:",
    1183: ":cloud_with_rain:",
    1186: ":cloud_with_rain:",
    1189: ":cloud_with_rain:",
    1192: ":cloud_with_heavy_rain:",
    1195: ":cloud_with_heavy_rain:",
    1066: ":cloud_with_snow:",
    1210: ":cloud_with_snow:",
    1213: ":cloud_with_snow:",
    1216: ":snowflake:",
    1219: ":snowflake:",
    1222: ":snowflakes:",
    1225: ":snowflakes:",
    1087: ":cloud_with_lightning_and_rain:",
    1273: ":cloud_with_lightning_and_rain:",
    1276: ":cloud_with_lightning:",
}


def nerd_font_supported() -> bool:
    # Attempt to measure width of a known Nerd Font glyph
    test = "\uf00d"  # sunny icon
    return len(test) == 1


def weather_icon(code: int) -> str:
    # Nerd Font first
    if nerd_font_supported() and code in NERD_WEATHER_ICONS:
        return NERD_WEATHER_ICONS[code]

    # everything is awesome Fallback emoji
    shortcode = FALLBACK_EMOJI.get(code, ":rainbow:")
    return emoji.emojize(shortcode, language="alias")
