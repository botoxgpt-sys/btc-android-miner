from pathlib import Path

root = Path('miner/app/src/main/res')

# Preserve upstream view structure because MainActivity uses generated view binding.
# Apply only branding and targeted resource/theme compatibility fixes.
strings = root / 'values/strings.xml'
s = strings.read_text()
s = s.replace('<string name="app_name">BTC Miner</string>', '<string name="app_name">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="dashboard_title">Bitcoin Android Miner</string>', '<string name="dashboard_title">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="config_title">Configuration</string>', '<string name="config_title">Settings</string>')
s = s.replace('<string name="mining_config">Mining</string>', '<string name="mining_config">Pool &amp; Mining</string>')
strings.write_text(s)

# Android 17 / Pixel light-mode compatibility fix.
# Upstream defines chart_axis_legend only in values-night/colors.xml, while several
# layouts and Kotlin code reference it unconditionally. Add the missing light resource.
colors = root / 'values/colors.xml'
c = colors.read_text()
if '<color name="chart_axis_legend">' not in c:
    c = c.replace(
        '</resources>',
        '    <color name="chart_axis_legend">#DE000000</color>\n</resources>'
    )
    colors.write_text(c)

# Settings readability fix.
# The app theme intentionally has a black windowBackground even in light mode, while
# colorOnSurface is black. These settings layouts had transparent roots, producing
# black text on a black background. Give only the settings screens the theme surface
# background: white in light mode and dark in night mode. This keeps the main miner
# dashboard unchanged and preserves proper DayNight behavior.
for name in ('activity_config.xml', 'activity_digital_rain_config.xml'):
    layout = root / 'layout' / name
    text = layout.read_text()
    marker = '    android:layout_height="match_parent">'
    replacement = '    android:layout_height="match_parent"\n    android:background="?attr/colorSurface">'
    if 'android:background="?attr/colorSurface"' not in text:
        text = text.replace(marker, replacement, 1)
        layout.write_text(text)

hub = root / 'layout' / 'activity_config_hub.xml'
text = hub.read_text()
if 'android:background="?attr/colorSurface"' not in text:
    text = text.replace(
        '    android:layout_height="match_parent"\n    android:orientation="vertical"',
        '    android:layout_height="match_parent"\n    android:background="?attr/colorSurface"\n    android:orientation="vertical"',
        1,
    )
    hub.write_text(text)

print('NerdOCTAXE Mobile branding + Android 17 + settings readability fixes applied')
