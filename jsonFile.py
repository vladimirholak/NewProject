import json

skola = [{'meno': 'Janko Hrasko',
          'adresa': {
              'ulica': 'Strukova',
              'cislo': 13,
              'obec': 'Fazulovo'},
          'narodeny': {
              'datum': {
                  'den': 1,
                  'mesiac': 5,
                  'rok': 1999},
              'obec': 'Korytovce'}},
     {'meno': 'Juraj Janosik',
      'adresa':{
          'ulica': 'Pod sibenicou',
          'cislo': 1,
          'obec': 'Liptovsky Mikulas'},
      'narodeny': {
          'datum': {
              'den': 25,
              'mesiac': 1,
              'rok': 1688},
          'obec': 'Terchova'}}]
with open('subor.txt', 'w') as subor:
    json.dump(skola, subor, indent=2)

nacitaneData = json.load(open('subor.txt'))
print(nacitaneData)

#balbalbalbballaaal