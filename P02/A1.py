txt = open('textprobe.txt', 'r')
txta = txt.read()
ac = len(txta)
txt.close()

txt = open('textprobe.txt', 'r')
txtb = txt.readlines()
at = len(txtb)
txt.close()

txt = open('textprobe.txt', 'r')
aet = sum(1 for line in txt if not line.strip())
txt.close()

atl = at-aet

anz_char = f"Die Anzahl Zeichen beträgt {ac}"
text_lines = f"Die Anzahl Zeilen beträgt {at}"
anz_text_lines = f"Die Anzahl Text Zeilen beträgt {atl}"
anz_empty_lines = f"Die Anzahl leere Zeilen beträgt {aet}"
print(anz_char)
print(text_lines)
print(anz_text_lines)
print(anz_empty_lines)