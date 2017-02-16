s = """Gur Ybeq bs gur Evatf, ol W. E. E. Gbyxvra

Guerr Evatf sbe gur Ryira-xvatf haqre gur fxl,
Frira sbe gur Qjnes-ybeqf va gurve unyyf bs fgbar,
Avar sbe Zbegny Zra qbbzrq gb qvr,
Bar sbe gur Qnex Ybeq ba uvf qnex guebar
Va gur Ynaq bs Zbeqbe jurer gur Funqbjf yvr.
Bar Evat gb ehyr gurz nyy, Bar Evat gb svaq gurz,
Bar Evat gb oevat gurz nyy naq va gur qnexarff ovaq gurz
Va gur Ynaq bs Zbeqbe jurer gur Funqbjf yvr."""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print ("".join([d.get(c, c) for c in s]))