#!/usr/bin/python

try:
    import PyBigNumbers
    import PyECPoint
    import PySymEncDec
    import PyMessageHash
    import PyAsymKey
    import PyPolynomial
    import Nakasendo
    import Threshold
except ImportError as e:
    print('Error while loading SDKLibraries python modules {}'.format(e.message))
    print('Try to define environment variable SDKLIBRARIES_ROOT pointing to the location of installed SDKLibraries or add this to PYTHONPATH')
    raise ImportError('Unable to load SDKLibraries python modules')

def _get_defined_polynomials_deg_2_KTest(deg,modulo=None):
    polys = []
    poly1 = Nakasendo.Polynomial.initFromListModuloDec(['12947668528073543477308455109047462837072825858004012787241413393576035430745','55013223815770071147182329690762295770874013664780832787304292520359528476749','36019556482187218768965434630628212179822160817484260317191251481650930215005'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloDec(['30903677663702179748782267301606104159314022276587189700459304755073831098422','18995632419395261390699417660969743835622025373416973451754569295566410502007','50584150054476862072263347423818337225860918194856251265656197083076450252543'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloDec(['57716661734930940867996799593209204956083655977702937511427741063453826550930','43239301989509682802872047351774509775209807269359467217506485249141033704033','7861283138100517963911853786979773533312229790256709863328507186047832354808'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    poly4 = Nakasendo.Polynomial.initFromListModuloDec(['35588194584818905752385345554075910379395729679904458183415350066675755602450','35693820587537279605003617581931288920516359152014244085334998976111720389782','115445388755280524848635834728309896353225808479121121042735198940761765465997'],modulo)
    poly4.modulo = modulo
    polys.append(poly4)
    
    poly5 = Nakasendo.Polynomial.initFromListModuloDec(['86928495085214256352229967517607872799504964396987092257069638198910769691080','110033267465270603464679701829784065549557631446229591390287554773927976007276','6556764205882583089394582200590164199382254698509076809176356070924868794070'],modulo)
    poly5.modulo = modulo
    polys.append(poly5)
    return polys
    
     
def _get_defined_polynomials_deg_2_EmpShareTest(deg,modulo=None):
    polys = []
    poly1 = Nakasendo.Polynomial.initFromListModuloDec(['24994218217093021844030563384394522342720574073032916335966628161802360891480','56923093566603907318069653594217543824215036840079028401560050980295471318454','26952071710174344418909339861165338044894613729183980669058721564552874069432'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloDec(['66742135906605113934406343148149031465344915379300741066825127064551833080090','88296953174360890944524534201258432664605628977257063653000349035570319044477','88987006406833879435126295369190642981041710812517955545390669917674853125981'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloDec(['65360924682439059750888104826226422760755880569804270629864492429500666345356','94347091288714181909366278105463642893877559090898116798486010255421734688851','97489734322929842511529613438892876692179790783470851989380373275049740958064'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    poly4 = Nakasendo.Polynomial.initFromListModuloDec(['98009817394525134006196280576696818756475401162328090889431880792440398606149','50449179156879692099229040019944101394287268579099253355693766148518708450884','48486664757013888279131171635058289944142801471390797945715537409045710554366'],modulo)
    poly4.modulo = modulo
    polys.append(poly4)
    
    poly5 = Nakasendo.Polynomial.initFromListModuloDec(['46565140997137221469618068573671808865555934755317765562877035921538247087734','34943456099632866914915303152943250773956118395120797550864874535214690116166','100894379241904715806219407443737997564835803583390447620798873768493047483883'],modulo)
    poly5.modulo = modulo
    polys.append(poly5)
    return polys
    
    
def _get_defined_polynomials_deg_2(deg, modulo=None):
    polys=[]
    poly1 = Nakasendo.Polynomial.initFromListModuloDec(['90486684032348777179857263718215968226709745781802876931942348748667124939196','111060844526219985844993439427010620819313558385116073114983958679266641376958','110718613858017256202536316680113603298106530379002848443141873670797350555901'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloDec(['48258538045028570548826074391325925068362928894625813479710236795005509115956','41139461839016974753097870948508408313493639679101849774114275992558422165502','105505238895838311044030323377889983620964588122952954537617794251727518931914'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloDec(['110535172131249658185500939112705858058708998630172814074009995699429063879869','108061290097758192663457950485994198362249979585265981699537314760614632599310','54315527299618878493913297670743197559397298559111552462118997327948940095323'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    poly4 = Nakasendo.Polynomial.initFromListModuloDec(['63710352881479095873539242469459354680667477233584651003526902199982051842677','81231863466428109795760520141443241880170664405340760623513426666830192789100','59219809793501109378576304501351695549242394470537788471337416562923475909016'],modulo)
    poly4.modulo = modulo
    polys.append(poly4)
    
    poly5 = Nakasendo.Polynomial.initFromListModuloDec(['16521042744413024593243591929042350193025729042224752433240176429585864012128','50710796840315552985242326799140829689315074937842458178159955670052904488263','64761406637564736315367730746559201070992423444837082376880430448351029458749'],modulo)
    poly5.modulo = modulo
    polys.append(poly5)
    return polys
    
    
    
    
def _get_defined_polynomials_deg_2_3_privKey(modulo=None):
    polys = []
    polys=[]
    poly1 = Nakasendo.Polynomial.initFromListModuloHex(['9EDB9EB292D5EFD9FC71AB2D8CA80B693526DE68A61176D1258A8A841F77BCDD','36173D161035E0CA53B560F2F43ABA90672A0CFB357C2671595D8C4B1548F00B'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloHex(['AB0B87ABF066FFB901FA42EBA1C88FA1AEF967814373E489EE60DB7EB3843F66','56811B760AA883FD0FCE2EF8ABC1D383F1314939056BDBACAB238CCA1765866B'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloHex(['7A64B803656EB3F17E035BE721F71525D5E761510F6F8E0555CAF555C7980C2E','B09FE54F8FB48344FBC54DC6D8AF2D81865611D25428A3D8EAC6BE6607C962D1'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    return polys
    

def _get_defined_polynomials_deg_2_3_k(modulo=None):
    polys = []
    polys=[]
    poly1 = Nakasendo.Polynomial.initFromListModuloHex(['D0A48E448025A5E4114B87DC5DD1513A6FD6E1CBF489DE4842CAA71EE78F2AF4','9B15AF066F4095AF7B9CA2526A350E1419246713445D8F2388B434E737C3478D'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloHex(['A9EDD1D17CE3977487F97DF19F85ABA915E4FED827A12DDD7464EB2227FB282F','279BC640013B9E058A740713F417152ED6C0AC05F946C937E7123338C69C1203'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloHex(['2F881CFC58002291B148F4FEEB08FBF37D6029FC64A31D92DD20205CCB835E66','B08C71181E6F0546E69135E2053B41BD6BE3BAB1573B9239B2715654A215499B'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    return polys


def _get_defined_polynomials_deg_2_3_alpha(modulo=None):
    polys = []
    polys=[]
    poly1 = Nakasendo.Polynomial.initFromListModuloHex(['0AEE9DB0B8191A4BCFA4CE75FD38D1B38BE56C2D1204029C157447112431C698','7B199B2C6B410548EDE657B604B18A3CD14B41AB118BBE93C71DCD44E4EC7751'],modulo)
    poly1.modulo = modulo
    polys.append(poly1)
    
    poly2 = Nakasendo.Polynomial.initFromListModuloHex(['FFFF56167E67B686D2AACB92B28BF847E1000DFF8B8B40437DEC1B902D206D68','68BB608C92C0F4CDB1799FE66A8978E6C5C14F542724D255A92A1E66358D37A6'],modulo)
    poly2.modulo = modulo
    polys.append(poly2)
    
    poly3 = Nakasendo.Polynomial.initFromListModuloHex(['4F09E06ABDBF47D7A6E9917B294BCE588B14A75CA59ABE3CB44538FE079DEB0B','7297346BA9761EED302CDB094853E791A2B39C2DE9513080980F6860793E9CD1'],modulo)
    poly3.modulo = modulo
    polys.append(poly3)
    
    return polys
















