# re.A => ASCII
# re.I => IGNORECASE
# re.M => Multiline => ^ $
# re.S => Dotall


import re

texto = '''

132.456.567-72 ABD
543.980.076-34 BHG
521.453.675-43 

'''
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))
