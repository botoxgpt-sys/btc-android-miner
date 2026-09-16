from pathlib import Path

root = Path('miner/app/src/main/res')

# Safe v2: preserve upstream layouts/themes exactly because MainActivity uses
# generated view binding and initializes the dashboard/digital-rain views at startup.
# Apply branding only; visual changes will be reintroduced incrementally after
# startup compatibility is confirmed.
strings = root / 'values/strings.xml'
s = strings.read_text()
s = s.replace('<string name="app_name">BTC Miner</string>', '<string name="app_name">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="dashboard_title">Bitcoin Android Miner</string>', '<string name="dashboard_title">NerdOCTAXE Mobile</string>')
s = s.replace('<string name="config_title">Configuration</string>', '<string name="config_title">Settings</string>')
s = s.replace('<string name="mining_config">Mining</string>', '<string name="mining_config">Pool &amp; Mining</string>')
strings.write_text(s)

print('NerdOCTAXE Mobile safe branding patch applied; upstream runtime layouts preserved')
