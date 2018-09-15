from collections import OrderedDict
import pickle

stock_urls = OrderedDict()
stock_urls['INVE-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5247/investor-b'
stock_urls['KINV-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5369/kinnevik-b'
stock_urls['ERIC-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5240/ericsson-b'
stock_urls['TELIA.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5479/telia-company'
stock_urls['SEB-A.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5255/seb-a'
stock_urls['SAND.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5471/sandvik'
stock_urls['SCA-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5263/sca-b'
stock_urls['LUPE.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5698/lundin-petroleum'
stock_urls['ATCO-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5235/atlas-copco-b'
stock_urls['FING-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5468/fingerprint-cards-b'
stock_urls['BOL.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5564/boliden'
stock_urls['AZN.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5431/astrazeneca'
stock_urls['MTG-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5438/modern-times-group-b'
stock_urls['ABB.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5447/abb-ltd'
stock_urls['SSAB-A.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5260/ssab-a'
stock_urls['HM-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5364/hennes---mauritz-b'
stock_urls['ELUX-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5238/electrolux-b'
stock_urls['GETI-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5282/getinge-b'
stock_urls['ASSA-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5271/assa-abloy-b'
stock_urls['NDA-SEK.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5249/nordea-bank'
stock_urls['ATCO-A.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5234/atlas-copco-a'
stock_urls['SWMA.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5266/swedish-match'
stock_urls['TEL2-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5386/tele2-b'
stock_urls['ALFA.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5580/alfa-laval'
stock_urls['SKA-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5257/skanska-b'
stock_urls['SHB-A.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5264/handelsbanken-a'
stock_urls['INVE-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5247/investor-b'
stock_urls['VOLV-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5269/volvo-b'
stock_urls['SECU-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5270/securitas-b'
stock_urls['SWED-A.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5241/swedbank-a'
stock_urls['SKF-B.ST'] = 'https://www.avanza.se/aktier/om-aktien.html/5259/skf-b'

with open('ticker_to_stock.pickle', 'wb') as f:
    pickle.dump(stock_urls, f)