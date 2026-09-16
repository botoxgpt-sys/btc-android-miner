from pathlib import Path

root = Path('miner/app/src/main/res')

# Preserve upstream layouts/themes because MainActivity uses generated view binding
# and initializes the dashboard views at startup. Apply branding only.
strings = root / 'values/strings.xml'
s = strings.read_text()
s = s.replace('<string name="app_name">BTC Miner</string>', '<string name="app_name">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="dashboard_title">Bitcoin Android Miner</string>', '<string name="dashboard_title">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="config_title">Configuration</string>', '<string name="config_title">Settings</string>')
s = s.replace('<string name="mining_config">Mining</string>', '<string name="mining_config">Pool &amp; Mining</string>')
strings.write_text(s)

# Android 17 / Pixel light-mode compatibility fix.
# Upstream defines chart_axis_legend only in values-night/colors.xml, while several
# layouts and Kotlin code reference it unconditionally. In light mode this can crash
# during TextView inflation with:
#   UnsupportedOperationException: Can't convert to ComplexColor: type=0x1
# Add the missing default (light-theme) resource while keeping the upstream night
# override untouched.
colors = root / 'values/colors.xml'
c = colors.read_text()
if '<color name="chart_axis_legend">' not in c:
    c = c.replace(
        '</resources>',
        '    <color name="chart_axis_legend">#DE000000</color>\n</resources>'
    )
    colors.write_text(c)

print('NerdOCTAXE Mobile branding + Android 17 light-mode color fix applied')
