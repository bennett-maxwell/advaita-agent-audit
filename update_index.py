import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add chore chart button after bootflow button
bootflow_btn = '<button class="tab" onclick="switchTab(\'bootflow\')">🚀 Boot Flow</button>'
new_button = '<button class="tab" onclick="switchTab(\'choreChart\')">🏠 Chore Chart</button>'
content = content.replace(bootflow_btn, bootflow_btn + '\n    ' + new_button)

# 2. Update ALL_TABS array
old_tabs = "const ALL_TABS=['leo','ivan','mack','skills','mindmap','bootflow'];"
new_tabs = "const ALL_TABS=['leo','ivan','mack','skills','mindmap','bootflow','choreChart'];"
content = content.replace(old_tabs, new_tabs)

# 3. Add tab panel before <script> tag
new_panel = '''<!-- CHORE CHART TAB -->
<div class="tab-panel" id="tab-choreChart">
  <iframe src="/chore-chart/index.html" style="width:100%;height:calc(100vh - 52px);border:none;"></iframe>
</div>

'''
content = content.replace('<script>\n', new_panel + '<script>\n')

with open('index.html', 'w') as f:
    f.write(content)

print("✅ index.html updated")
