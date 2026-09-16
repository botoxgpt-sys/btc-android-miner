from pathlib import Path

root = Path('miner/app/src/main/res')

# Branding + labels. Keep the upstream mining engine untouched.
strings = root / 'values/strings.xml'
s = strings.read_text()
s = s.replace('<string name="app_name">BTC Miner</string>', '<string name="app_name">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="dashboard_title">Bitcoin Android Miner</string>', '<string name="dashboard_title">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="config_title">Configuration</string>', '<string name="config_title">Settings</string>')
s = s.replace('<string name="mining_config">Mining</string>', '<string name="mining_config">Pool &amp; Mining</string>')
strings.write_text(s)

# Force the same dark instrument-panel language used by NerdOCTAXE.
theme = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="Theme.BTCMiner" parent="Theme.MaterialComponents.DayNight.NoActionBar">
        <item name="colorPrimary">@color/bitcoin_orange</item>
        <item name="colorOnPrimary">@color/black</item>
        <item name="colorSecondary">@color/bitcoin_orange</item>
        <item name="colorSurface">#FF111315</item>
        <item name="colorOnSurface">#FFF2F2F2</item>
        <item name="colorSurfaceVariant">#FF1B1E21</item>
        <item name="colorOnSurfaceVariant">#FFCACACA</item>
        <item name="colorOutline">#FF50555A</item>
        <item name="android:windowBackground">#FF0B0D0F</item>
        <item name="android:navigationBarColor">#FF0B0D0F</item>
        <item name="android:statusBarColor">#FF0B0D0F</item>
        <item name="android:windowLightStatusBar">false</item>
    </style>
</resources>
'''
(root / 'values/themes.xml').write_text(theme)
(root / 'values-night/themes.xml').write_text(theme)

# Dashboard: remove Matrix-style background by default and use a clean miner panel.
main = root / 'layout/activity_main.xml'
m = main.read_text()
m = m.replace('android:id="@+id/digital_rain_container"\n        android:layout_width="match_parent"\n        android:layout_height="match_parent"', 'android:id="@+id/digital_rain_container"\n        android:layout_width="match_parent"\n        android:layout_height="match_parent"\n        android:visibility="gone"')
m = m.replace('android:id="@+id/dashboard_overlay"\n        android:layout_width="match_parent"\n        android:layout_height="match_parent"\n        android:background="@android:color/transparent"', 'android:id="@+id/dashboard_overlay"\n        android:layout_width="match_parent"\n        android:layout_height="match_parent"\n        android:background="#FF0B0D0F"')
m = m.replace('android:textSize="24sp"\n                android:textStyle="bold"', 'android:textSize="22sp"\n                android:letterSpacing="0.04"\n                android:textStyle="bold"', 1)
main.write_text(m)

# Make the main hashrate the visual focal point.
page1 = root / 'layout/fragment_dashboard_page1.xml'
p = page1.read_text()
p = p.replace('android:textSize="28sp"', 'android:textSize="38sp"', 1)
p = p.replace('android:paddingBottom="8dp">', 'android:paddingBottom="8dp"\n    android:background="#FF0B0D0F">', 1)
page1.write_text(p)

# Settings hub uses the same dark panel background.
hub = root / 'layout/activity_config_hub.xml'
h = hub.read_text().replace('android:orientation="vertical"', 'android:orientation="vertical"\n    android:background="#FF0B0D0F"', 1)
hub.write_text(h)

config = root / 'layout/activity_config.xml'
c = config.read_text().replace('android:layout_height="match_parent">', 'android:layout_height="match_parent"\n    android:background="#FF0B0D0F">', 1)
config.write_text(c)

print('NerdOCTAXE Mobile UI patch applied')
