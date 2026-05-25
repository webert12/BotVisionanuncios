import streamlit as st
import telebot
import random
import time
import pandas as pd

# Configuração da página do Streamlit
st.set_page_config(page_title="Vision Trade PRO - Painel de Marketing", page_icon="🤖")
st.title("🤖 Vision Trade PRO V3 - Central de Transmissão")

# Inicialização do Bot Oficial
TOKEN = st.text_input("8710725826:AAFuGmF30Ns-G1glrBYir9ggVya9VwQgZAU:", type="macacos)

st.subheader("1. Base de Clientes (Usuários que já usam o Bot)")

# Lista real de clientes inserida diretamente no código
u_data = {
    "user_id": [
        1787342669, 6080143272, 7318970939, 911217726, 1033909813, 763598578, 1070421755, 63279972, 
        371182877, 1401660903, 885529569, 515041689, 1237055458, 1585984780, 624972487, 814416756, 
        7097672229, 1119123392, 1186125724, 742314987, 1055383046, 963047735, 801835080, 1186536022, 
        1362066227, 870718696, 564654960, 301817880, 384614480, 5412052413, 837532206, 319871235, 
        974009402, 328593103, 1523581074, 7531800904, 249902385, 1062185961, 1741625399, 1299655315, 
        1657688174, 806958301, 390780061, 1043917526, 6363020110, 961067634, 223666361, 1306633742, 
        1751222842, 1439330582, 537825147, 934290684, 1647946137, 837415926, 609175875, 5261612212, 
        535446682, 1488906548, 1028981837, 2006582122, 856206631, 8195711560, 5245454134, 1292745440, 
        653476335, 686247512, 6440562735, 1901416536, 1325274556, 162696575, 1059419907, 786992277, 
        1050059030, 1953551813, 571827231, 2018386875, 1023639132, 1074315677, 8295338231, 1086111861, 
        543108852, 5147576634, 659362658, 6820159092, 1403740331, 5068631903, 547572967, 1062219489, 
        902207721, 825835622, 962053977, 5261583610, 860611890, 332195303, 760842629, 278982039, 
        2091678752, 905594554, 1042992581, 6638311998, 6901514287, 5889651516, 1446651761, 1086843522, 
        6071060571, 888950109, 786754937, 1235488653, 6484137270, 1273221941, 822746540, 8085554152, 
        1410297479, 1493208317, 128638327, 223089471, 1053793471, 7562616164, 1143082533, 1085484867, 
        881504366, 5088847127, 176757960, 827405346, 1946749960, 867899732, 6009693604, 845764643, 
        1997413360, 7554403607, 858069679, 138014763, 676119825, 1366531938, 408391180, 1223992834, 
        1632680262, 971268041, 1881146463, 1762626057, 902888127, 5565813389, 846635087, 1092693608, 
        878648960, 299249844, 1764042599, 755004834, 612642059, 6456306090, 1091045047, 145256066, 
        7940831312, 799351562, 5716253682, 1700431304, 7865288277, 1891478467, 892369785, 6229656273, 
        1452784528, 7515061816, 7338480988, 85998017, 1617801567, 831583944, 388581637, 1311554465, 
        1380080632, 495661791, 5034656476, 606807164, 1203655481, 7840744628, 5880649961, 1162555940, 
        1896692622, 146084148, 5056548736, 1823661766, 481771040, 1081154688, 517377885, 1783018874, 
        683857806, 344193268, 938809940, 297341742, 313317240, 2020821625, 926004645, 383709160, 
        850772222, 1069250921, 1100076864, 6961053271, 1191809739, 1682173203, 1600134758, 1047057836, 
        7299300332, 1312854301, 1219585766, 1302871446, 7667063124, 781777819, 953638419, 1995273514, 
        932087965, 5925645373, 6110320824, 650923105, 5215579909, 1116659077, 1757992078, 441418326, 
        741085255, 735828243, 584631624, 1100524168, 869158498, 1643144587, 1100824164, 1032395093, 
        5347974434, 796317688, 1242562192, 1670725097, 814709194, 1162157066, 1564335091, 8142381304, 
        1345137181, 1226209932, 1621512769, 1102534431, 1738337952, 7807009515, 1077454724, 673860868, 
        834819443, 1037477967, 5447413431, 988013927, 1345926858, 5618231880, 7116469843, 5976164433, 
        1027132454, 1142261002, 1393274439, 626564710, 1188217566, 1302834546, 129503005, 1275201483, 
        497044139, 1296189331, 453258007, 1076938123, 1777238672, 5549850435, 788434933, 382922087, 
        5890295234, 280124271, 1040194013, 396749887, 443939085, 1971936048, 5239891498, 5282342460, 
        1811810445, 6548647620, 1065812723, 5921781838, 643642451, 947495929, 6848669826, 1093069360, 
        1124713437, 5071453226, 1053442095, 1106236568, 6534026253, 5170080731, 35631542, 1117826802, 
        6565930544, 1863790325, 1512741538, 144538463, 6002550160, 859161615, 1192084664, 809343040, 
        2039301841, 605173578, 858262448, 5506350070, 928696615, 964492521, 818647442, 6373340566, 
        1045204231, 1405647421, 1002358652, 1604428843, 736106993, 1781963441, 855048693, 745274348, 
        136568940, 795687271, 7803151995, 722617232, 1930041533, 2063398915, 1915043619, 1357762248, 
        7848322392, 978982436, 994277267, 2065819825, 843140239, 716014507, 904642155, 756821017, 
        1119829420, 203763011, 450783160, 723268176, 1594168370, 1166746441, 1556244452, 800778905, 
        1277308051, 23853362, 647187058, 979266151, 1499541654, 6537690170, 7619355787, 696546158, 
        2097625976, 6292978343, 1290445292, 1477380953, 932474418, 480076496, 1550083214, 823670335, 
        965320462, 248466885, 7683202177, 1651328606, 5833713684, 1046437147, 1311859409, 979246419, 
        7603871356, 1065411177, 903691163, 833088337, 1233739947, 1246867199, 1028342738, 689705045, 
        1243122463, 1621294943, 6114228191, 1088971672, 742913795, 429943555, 837881983, 766800438, 
        191889745, 934633734, 37944184, 709319166, 1830777706, 5065897200, 181405032, 1554380786, 
        1040082309, 851669325, 7539034129, 1072850588, 959276613, 709151718, 7022277019, 1295438433, 
        569367626, 5419610106, 489322122, 856805384, 370084674, 903409172, 810795305, 7583596631, 
        1228136613, 7881405859, 1923058578, 144365914, 828213201, 8067994173, 1229864059, 847384738, 
        204939420, 968063761, 6415492944, 1529405264, 1101605931, 6726447366, 1026557459, 1153038516, 
        1400620255, 839706563, 577561153, 234046038, 1531206713, 917662502, 5358110274, 6901904527, 
        6806994950, 850041040, 848480558, 29143496, 645046850, 528461467, 454680877, 1721410965, 
        7632699249, 1010159313, 4786745, 1610088242, 1009993422, 494531791, 8112226325, 6904324352, 
        1112044276, 1945148321, 634941148, 6232361597, 50818507, 2019287414, 685961955, 626170921, 
        7968003677, 1210275439, 902152074, 1645325934, 6053939644, 898691831, 1070666406, 1135385278, 
        5035869109, 5270102364, 428916567, 899335141, 438333328, 8075856131, 1653090958, 939673950, 
        1244285044, 1018963420, 498062837, 1437130223, 6008775969, 800556277, 1110045624, 1192107418, 
        637528579, 7651888662, 1113646500, 325798743, 404968134, 1600921236, 991630326, 1268722852, 
        1126203770, 1354166458, 917059516, 1401473889, 1133893460, 7753178776, 8182591194, 7920883773, 
        661178351, 798712213, 822610818, 733857700, 352372528, 942677367, 5982635386, 49627488, 
        1480653146, 1331006746, 1007162168, 5291857031, 568272630, 6409712791, 1072516572, 5815861309, 
        284880097, 8190721353, 1459234935, 1357690980, 1476095302, 1227447972, 1876269381, 739791036, 
        5676877974, 785897905, 5924340676, 6574640972, 952902411, 953828894, 860873383, 7565732969, 
        1201840493, 897986716, 5721873978, 1047394875, 1041490813, 5176516669, 788389214, 810344360, 
        450917349, 6840405030, 1225967296, 7395653683, 907952287, 6372130664, 1192777807, 7543820037, 
        5006534577, 1077669043, 1019896973, 873108285, 590833687, 1731589177, 686218696, 1770492961, 
        1305031927, 5114870496, 241977529, 1291640128, 297714519, 5922070720, 450683229, 1033088913, 
        1072797367, 951435595, 1081406712, 1882355469, 6527662646, 5168646983, 570887807, 673086808, 
        5165622888, 5987871370, 910188517, 1180052986, 806615948, 816160577, 1483105254, 1997439151, 
        1060850783, 1278562036, 96893888, 821325976, 1190999684, 480468602, 707341175, 403447620, 
        7270791125, 5817713647, 995168070, 5625405298, 1903159142, 946070086, 5460847364, 5406773952, 
        712732898, 358613430, 1172904468, 608587071, 641584740, 1090746531, 7637346686, 5135914291, 
        880877754, 1645846411, 1249744337, 1350872660, 989375372, 593879637, 1171278732, 1265704798, 
        761874418, 514001106, 987886884, 219559033, 6242015230, 1828151946, 773675867, 830365514, 
        1208850031, 1662071253, 5030240405, 187261506, 1152105944, 849693284, 146231386, 1025530595, 
        1238215119, 393245607, 785829372, 5084309518, 1655285955, 924879804, 870459878, 1226149736, 
        981630929, 1014526992, 1157313421, 700978001, 886723341, 677905104, 5454582961, 885488366, 
        795616062, 482398991, 726650707, 425293728, 1116626199, 660831825, 949792526, 5243903760, 
        1091681098, 969303371, 7120272819, 414520186, 297352379, 509013214, 1395643684, 981490806, 
        1677156207, 938399762, 8133567624, 5032224860, 1100826056, 955012629, 147242439, 1066423654, 
        745852319, 1348449108, 5215498432, 800856574, 2123259856, 1073442716, 393592787, 936117979, 
        927906949, 1454442241, 5328980331, 2018358856, 967952842, 1614202116, 783320020, 1886193786, 
        5453816548, 1460519977, 1529245463, 919466662, 1093626394, 217017202, 920232723, 967339137, 
        1092884659, 802200959, 1319435817, 910652806, 2028587367, 893825657, 1077866027, 826756996, 
        1719938386, 1876046842, 1786527122, 1766225500, 1887920094, 221794246, 1829436508, 817635884, 
        157119288, 572496388, 993594529, 27620683, 1168816036, 751096275, 6818703595, 861924772, 
        1671424865, 1048750343, 5097413950, 960091199, 1052764156, 616236275, 7397751179, 1046606850, 
        7498130871, 495862878, 1803560491, 1252882778, 190348806, 1097351436, 1245085840, 764435172, 
        1871876807, 916853123, 1042524807, 196726832, 1147672793, 25978512, 1282993764, 1004166864, 
        6788910699, 769617021, 1152873925, 1872635767, 1696319288, 1141376908, 7571740255, 1775025270, 
        883488080, 983336866, 1534105981, 749375907, 1242771450, 7879534406, 709335719, 865160693, 
        1471403014, 790295643, 803602401, 7270930045, 803938037, 322906285
    ],
    "nome": [
        "Sem_Username", "Korvette", "Ann_299", "claudsonfx", "Zicao10", "Sem_Username", "Luanlopezz", "pedrompimenta", 
        "Semnomen", "rvperes", "cjunior13", "patrickdomingues", "Kitoscalon", "FelipeMasketto", "EduardoJCustodio", "Gersonreetz", 
        "tarcisioallyson", "Sem_Username", "Lrlr18", "SandovalPontes", "NeyFilho23", "rafaeloliveirafx", "Rosanavr", "Sem_Username", 
        "Sem_Username", "Bgrumman", "Wanderson00110", "LordViniciusFractal53", "ItzMillyZ", "SrFiu", "WallaceCamposs", "limalucas", 
        "gustalhenri", "L4NC3L0T", "Hosloz", "Sinzylam", "Bernardopatife", "LexandreMascena", "Cassioseabra", "Sem_Username", 
        "m0st0f0", "KaisonFurtado", "djandersoncleitonpvh", "johannehlert", "Th1GR1", "Yahalomm2", "Junior4xBr", "mfernands", 
        "Sem_Username", "GJacq", "paulopeskra7", "Raithalles", "Sem_Username", "Sem_Username", "MichelFaria", "Sem_Username", 
        "Sem_Username", "andremantovanimg", "Nwaabia164", "Sem_Username", "Pcjhon", "Fabioliveiradev", "Sem_Username", "Marcosarruda21", 
        "kawanmatos", "lucastakeFX", "Sem_Username", "Jajah13", "lucas_couuto", "Holdvida", "Sem_Username", "Sem_Username", 
        "Sem_Username", "Imtigo", "Sem_Username", "isaiasferreira7", "Avante_2025", "Sem_Username", "Sem_Username", "lucas_santos9021", 
        "ianhmz", "Alves_lucass", "yung669", "jkap01", "bdrarc", "Sem_Username", "Sem_Username", "Sem_Username", 
        "Kami202424", "jiz_bsb", "greatspot81", "Sem_Username", "Fabiano_M_Almeida", "solyjr", "b_roy7", "Dantaass", 
        "Lopes8", "Sem_Username", "Kellycrisbio", "Gilson1000", "neto994", "MuhamAlinSha", "Sem_Username", "alguemsilva", 
        "TAOVI618", "Thechampion22", "Excelencia7", "Guizord97", "mariislotsss", "TheGre9", "devthiagotpl", "Sem_Username", 
        "HiagoFerreira", "kkkbyt", "gerkulez", "DreisonTravassos", "PetersondeBritto", "MoisesRamses", "Sem_Username", "Lenon_Moraes", 
        "renatoremerjr", "kbpoint", "ewertonferreira", "Sem_Username", "Toddy711", "Marcelo_Linhares", "Andreisilva98", "eng_ellikson", 
        "George69369936", "AImeidaVitor", "lukaskk1", "tickermachine", "Bry99", "fala2A", "BapM11", "TraderMidas", 
        "suporte_botblack", "BrunoUhe", "Davidson1308", "Softbem", "Raphagiar", "GutoSa", "Sem_Username", "Ducapg", 
        "JonathanAugust", "Sem_Username", "peD134", "annesheilla", "thiagogavaa", "Sem_Username", "Ogaittttttt", "AxelrodFX", 
        "Abreuts", "RubensFrueh", "iwwatt", "Onevodk", "Sem_Username", "Sem_Username", "marco_barretto", "henriquepd", 
        "Sem_Username", "Princehamad5050", "LucianoBD", "Sem_Username", "Rcgmrs", "DEEPER044", "cleysonarevalo", "vianatrader2024", 
        "DenzelGarcia", "Sem_Username", "psilvasilva7", "zxtheuxz", "Sem_Username", "Santos4136", "Sem_Username", "Messiassoares", 
        "Sem_Username", "asdfghjtnm", "JoeNocego", "jsocram83", "Sem_Username", "JhonnyLucasYuki", "guigaoff", "Sem_Username", 
        "Sem_Username", "yurialexan", "Sem_Username", "Andre1991", "Viajosue", "LukenVrechi", "MatheusdosAnj0s", "insetox8", 
        "DDDyonis", "nenvss", "JOHANTRINDADE1", "Lucasgoulart_01", "Felipesilva1224", "Patrick_Card", "matheusarc_122", "Rino8", 
        "eberjosetreinador", "kayapov", "edynhho", "Sem_Username", "Karllos_Fernandes", "Liliannasouza", "Manfrinii", "Traderforexob", 
        "FilipeAugustoSa", "developerkingfx", "Sem_Username", "Valdir1967", "jotac221", "brunoeng21", "Sem_Username", "matheusnm", 
        "VictorACMagalhaes", "caipiraz", "leonardo078", "eduardo2563", "dougps11", "spMiguel", "Jksimoes", "Pada_90", 
        "luan875", "devbass", "Turikoph7", "Darckzin017", "Sem_Username", "Sem_Username", "Sem_Username", "Sem_Username", 
        "Sem_Username", "Sem_Username", "Tiago994", "ched4o", "vini_gonc", "mrodrigo15", "TioMilho", "ganselmo", 
        "viniciusmontalvao", "Kzzz_Sr", "eusougustavocesar", "lucaascabrall", "HugoFaria8", "gilbertopereira_advocacia", "Sem_Username", "nobres10", 
        "Sem_Username", "vertonmorais", "ErickRich", "Sem_Username", "cizz2", "gusttavam", "jaobelfort", "Enriquetxt", 
        "BIT90G", "estouocupado", "andrebonfante", "je4z4", "Dher062", "Suportezeno", "Sem_Username", "DarkArmYi", 
        "Lia5_silva", "RPL06", "Amlahmed1339", "EverttonMatheus", "Alessandro006", "Sem_Username", "Sem_Username", "Kischenner", 
        "helizao", "Leoob2025", "dr_kassio_abreu", "sofi5690", "lucas_muscopf", "Sem_Username", "Sem_Username", "Wenisantos", 
        "vitorhugols", "Eds0ntrader", "SGTWAGNER", "Sem_Username", "Sem_Username", "teremdbs", "fabiodfmelo", "rodrigo9702", 
        "Sem_Username", "lucas303assis", "Sem_Username", "ungido09", "Rafaa28722", "Sem_Username", "MathewTzT", "Sasu0503A77", 
        "Sem_Username", "MARCOSPAULOATHAYDE", "jcssteg", "FelipeMendesF", "rcyp1077", "Jeffersonmarchini", "LilianKaine", "Sem_Username", 
        "Sem_Username", "Valdonic", "Henrique_BizMix", "AnonymoysRat", "Sem_Username", "Sem_Username", "edupvs", "eulh999", 
        "Sem_Username", "lucas199199", "Sem_Username", "M_Alfinas", "Sem_Username", "babayagahakay", "brximports", "Luizsamp", 
        "Vivi_cruz", "WesleyPiress", "Sem_Username", "NadsonMarinho", "diegowsk", "Alzilaide", "RafaellXaviier", "Sem_Username", 
        "Darlan_Brito", "Cabelo130", "Ale2149", "Tuannakarlla", "SantosFiel", "brunosvieira1", "Sem_Username", "Sem_Username", 
        "Papaleguas100", "douglasmeira", "Barros40", "Sem_Username", "Fernandoxlima", "Tevotrader", "Sem_Username", "Isv943", 
        "pjgsilva", "baby_maksin", "rafa_carneiro", "vuogtrader", "Lucasdosantoscelestino", "Sem_Username", "CrislaineSales", "mateusxyzl", 
        "Aragao22", "Jonatanlds", "Sem_Username", "Esley66", "Sem_Username", "MatheuzFv", "Rdunior", "Rafaellaur", 
        "Jeffbunkerfx", "cleitonelias", "AlisomGomes", "Sem_Username", "Sem_Username", "Tr0nics", "blausy", "Sem_Username", 
        "Sem_Username", "Wesleydnzz", "Sigarro2", "Sem_Username", "Fabio_Navarro", "A_Noaes", "Jonatastrentin", "Sem_Username", 
        "EduardoGSalles", "Pina_Lima", "rribeirorj", "CleitonGuimaraes", "Dnil0R", "Sem_Username", "luizmagnopsf", "Sem_Username", 
        "NatanRyan", "mederim", "leocabral777", "Flavio202485", "Renanm001", "maykelopess", "Sem_Username", "fbkazumi", 
        "NaoFuiEu", "biamonfardini", "Pedrojrex", "Rogerio_lima", "Ndjjz92", "Sem_Username", "JorgePinheiro01", "Sem_Username", 
        "Idiara", "vitorgfx", "Sem_Username", "Well741", "Sem_Username", "Mr_J_br", "Sem_Username", "HannibalNeto", 
        "Vitortakashi7", "daianefxx", "carllosh3", "jeffinmendes", "Eliege_Fagundes", "AmadorasBrz", "Sem_Username", "Sem_Username", 
        "Anderson_Viana00", "dinnarthy", "Sem_Username", "BlandissomRicardo", "MAIKI5", "Sem_Username", "gatscherfilipe", "Sem_Username", 
        "Misteriotrader", "Hailtonfi", "icleitoncosta", "douglasanpa", "F4lcon1", "atospt", "Muquinhasnx2005", "Diogobeen", 
        "binance2573", "Sem_Username", "licensed", "mauropqd99", "Edulsilva", "jeferson723", "omutti31", "macarraopng", 
        "Obaoba2527", "Mtzindelas", "AndressaBap", "doctorvinsmoke", "mcm_84", "jimbow787", "nando_az1981", "Rudimarcio", 
        "litoralterpz710", "sardbtc", "Luanemoreno", "lhucampos", "Sem_Username", "Daan_02", "skyrootof", "grazivazcosta", 
        "luizbaracho", "atordoado", "Edson_BS", "Maskinslz", "Brankko", "EliasGabrriel", "Sem_Username", "gv3music", 
        "Mendes42fx", "rodrigo_gta", "JoaoMarini86", "Carloswcw", "Marioagiota2", "igorckoz", "Sem_Username", "Sem_Username", 
        "mathus32", "loveIycomplex", "jviniciusr", "LucasBrevis", "Josi_josi76", "Sem_Username", "sdsdsfre", "SamiresprotegidaporDeus", 
        "Sem_Username", "WinnerIndicador", "Sem_Username", "Sem_Username", "D4rknox", "Sem_Username", "Sem_Username", "iamrichboyy", 
        "rafaelqsc", "pdrivo", "pipipipopopoio", "miro171", "JOONHS_Indian", "Ramirogrfilho", "be_012", "osilvah", 
        "micaelkkj", "italoalbino", "DreyMPD", "Esgekkoo", "LIPEEEEE", "andreiarf", "bhmbrendo", "gbrny99", 
        "rodrigo_f_marques", "Morganwellan11", "dansirius33", "AORTEMTANDO", "sentinel88", "Sem_Username", "juBlack01", "Masasaca", 
        "Sem_Username", "henriquer3", "Filipeszz", "istouliso", "Sem_Username", "lukiinn", "Sem_Username", "Sem_Username", 
        "Ailton_pacheco", "Criesbik", "Eliyahu39", "Luizfontes", "Douglasmeiradesouza", "pedrottw", "wagnerpavan", "wmr2281", 
        "Pass7ll", "ianhre998", "Sem_Username", "Sem_Username", "RafaelP2Santos", "Ggnati", "Sem_Username", "Sem_Username", 
        "morelm8", "Sem_Username", "cleydsonandrade", "tele_ja", "marcosrdtec", "Dogahh", "alexfariasaf", "Sem_Username", 
        "Mah92araujo", "Testen45", "obeccamart", "Sem_Username", "RickAlves86", "Sem_Username", "shakur787", "mluisdesouza", 
        "UNOLUX1", "Rntpnh", "Sem_Username", "Neguin53", "Sem_Username", "signals_chinatrader", "apcontato", "henriqueso2", 
        "Sem_Username", "italoclg", "Sem_Username", "Delsant", "Wandervox", "ProVision84", "Ecaldas6", "Chavess06", 
        "Renediniz", "Leonardodavi28", "LuizUel", "Jhonyzito", "Sem_Username", "Leonlima", "lucihanx", "Andre8132", 
        "Sem_Username", "bdpvrtt", "SidneyArtur", "CarlosGuuih21", "natesantos007", "PedroRodriguessba", "Sem_Username", "Sem_Username", 
        "A10Xjoe", "Wesley_Rc", "gih_ca", "joscelio", "tomaztulio", "WilsonJLima", "chrislaurentino", "deni92", 
        "wislandergarcia", "Gabriel_Arthur_Calvo_Amaral", "d_mor193", "pv2923", "Matheusalpha", "MuriloVilela007", "Decaminado", "mendesdavi", 
        "leandrolunaeng", "dufreitas5", "franciscosantos", "Jjvuijbhi", "Sem_Username", "BalaoBoladao", "Judson_Macedo", "renan_1310", 
        "Sem_Username", "Gremlims", "Promptcomando", "wesleytimbo", "pedrobionde", "R3J21", "pedrovascon", "Sem_Username", 
        "BNZ_Franci", "Luiz_Luiz1234", "Jsortd", "RebecaSchevchenco", "Kaverinha78", "thaissouzaig", "Sem_Username", "Kailane00", 
        "Lucasc0906", "Sem_Username", "aquilalucas", "sunnhttps", "Cristiano_Henrique_Silva", "EltonO", "Sem_Username", "Sem_Username", 
        "gumaierhofer", "MassamiKazuma", "Suelaine", "Vandiz", "Btelles", "SagdiyevEverson", "Isamarry7", "Sem_Username", 
        "Sem_Username", "Marilzab", "Sem_Username", "FabianoMaciel", "Sem_Username", "travalha", "marllonn1", "elgatobuiu", 
        "omaiscaro08", "Carlos11890", "ThiagoLimaLeite", "Lrdcs", "JhonMascarenhas01", "Sem_Username", "edylicious", "Sem_Username", 
        "alex5465sn", "maikiofc", "Sem_Username", "Iagovelozo", "airlaguimaraes", "f_gnr", "vvieira", "almeida_41", 
        "Kleberg3", "Sem_Username", "KilsonDjzy", "CCLucas", "helifasdouglas", "del_marco", "alexleo1607", "Thales_TT", 
        "Sem_Username", "rxxtrader", "samuelmaxy", "fabimicro", "Sem_Username", "NBR_Pro", "luccaseduardo", "aleushizima", 
        "hm5622", "Igordavid", "Filiphe04", "Sem_Username", "joankaio", "Sem_Username", "maatheusmiguel", "jcaamargo", 
        "Sem_Username", "advogadacivilistanapratica", "WesleyRodrigues95", "Sem_Username", "AdrivanFerreira", "Tomdecano", "Carlossreis", "j_c9920", 
        "AnjjoG", "napoleonnog", "Cleverton_reis", "Sem_Username", "Thiago_Gomes999", "gilberdefaria", "GeovaneG8N", "Sem_Username", 
        "Givas02", "Ratel762", "Sem_Username", "thalesmorez", "brenowillian", "Floriano89", "Luisantrs0707", "camilamontb", 
        "Sem_Username", "wagnersnog", "zzzzzgdds", "Sem_Username", "xingu_invest", "sullivanb3", "Sem_Username", "Sem_Username", 
        "Fmtl1", "Sem_Username", "Henrique887", "Carokas", "Prosperitycrystal", "Sem_Username", "ezearaujo", "Sem_Username", 
        "Sem_Username", "antenor_costs", "Revesnine", "AlysonPortela05", "Jackson_Loureiro", "joarleson", "Sem_Username", "leozinho_77", 
        "AriellSilva", "guilhermemassao", "Droperox", "BestaFeradoCampo", "daniloruela", "lwba96", "Tomdecano", "salazargui", 
        "Marquinho4", "Jackpatterson", "vitor_mleme", "Sem_Username", "Mauro_Melo", "Sem_Username"
    ]
}

df_usuarios = pd.DataFrame(u_data)
st.dataframe(df_usuarios)

# Área para configuração das Mensagens Rotativas (Modelos Copywriting de Alta Conversão)
st.subheader("2. Configuração de Mensagens Rotativas")

msg1 = st.text_area("Mensagem A (Foco em Resultados):", 
"🎯 *Meta Batida no Vision Trade PRO V3!* 🚀\n\n"
"Nossa inteligência artificial acaba de finalizar as operações de hoje com extrema precisão. Quer ver o histórico de operações e os gráficos em tempo real?\n\n"
"👉 *Acesse o canal gratuito agora:* https://t.me/Visiontradev3")

msg2 = st.text_area("Mensagem B (Foco em Tecnologia/Inovação):", 
"📊 *A Inteligência Artificial que trabalha por você!*\n\n"
"Deixe a análise complexa de gráficos com o robô mais assertivo do mercado. O **Vision Trade PRO V3** opera com gerenciamento de risco automatizado para proteger seu capital.\n\n"
"🔗 *Veja a IA rodando no grupo oficial:* https://t.me/Visiontradev3")

msg3 = st.text_area("Mensagem C (Foco em Escassez/Vagas VIP):", 
"⚠️ *ÚLTIMAS VAGAS DISPONÍVEIS - SALA VIP VISION TRADE*\n\n"
"O acesso restrito à nossa central de sinais premium está prestes a fechar. Não fique de fora da tecnologia que está mudando o mercado de investimentos.\n\n"
"🤖 *Garanta seu lugar clicando no link:* https://t.me/Visiontradev3")

mensagens = [msg1, msg2, msg3]

# Configuração de Intervalos
st.subheader("3. Parâmetros de Envio Seguro")
intervalo_min = st.number_input("Intervalo Mínimo (segundos):", min_value=1, value=5)
intervalo_max = st.number_input("Intervalo Mínimo (segundos):", min_value=2, value=15)

# Botão de Disparo
if st.button("Iniciar Transmissão para Clientes"):
    if not TOKEN:
        st.error("Por favor, insira o Token do Bot.")
    else:
        try:
            bot = telebot.TeleBot(TOKEN)
            status_list = []
            
            progress_bar = st.progress(0)
            total_usuarios = len(df_usuarios)
            
            for index, row in df_usuarios.iterrows():
                msg_escolhida = random.choice(mensagens)
                user_id = row['user_id']
                
                try:
                    # Envia com parse_mode="Markdown" para aceitar os negritos e links configurados
                    bot.send_message(user_id, msg_escolhida, parse_mode="Markdown")
                    st.success(f"Enviado para {row['nome']} ({user_id})")
                except Exception as e:
                    st.error(f"Erro ao enviar para {user_id}: {e}")
                
                tempo_espera = random.randint(intervalo_min, intervalo_max)
                time.sleep(tempo_espera)
                
                progress_bar.progress((index + 1) / total_usuarios)
                
            st.balloons()
            st.success("Transmissão concluída com sucesso!")
            
        except Exception as api_error:
            st.error(f"Erro ao inicializar o Bot: {api_error}")
