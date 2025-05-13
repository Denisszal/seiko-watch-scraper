 Seiko pulksteņu meklēšana un salīdzināšana ar eBay piedāvājumiem


* Skripta skaidrojums

Seiko.py: 

* Dodas uz tīmekļa vietni ar rokas pulksteņiem, apstiprina sīkfailus, meklēšanas logā ieraksta “Seiko” un noklikšķina uz bloka “Meklēt”.
* Blokā ar filtriem izvēlas trīs filtrus - “Aproce”, “Dzimums”, Stikls“ un pēc tam parāda atrasto pulksteņu skaitu, saraksta formātā parāda zīmolu, modeli, nosaukumu, izmēru un cenu, kā arī saiti, noņem piezīmi ”Rokas pulkstenis".
* Saglabā šos datus failā ar nosaukumu “seiko_watches.txt”
* Ņem modeļus no virknes “model_codes = []” un atver meklēšanas virkni Ebay vietnē, apstiprina sīkfailus, parāda tikai tos pulksteņus, kuru nosaukumā sarakstā ir viens no modeļiem,
* Dokumentā - “ebay_results.txt” izvada modeli, nosaukumu un cenu, kā arī saiti uz pulksteni.











Pirms skripta palaišanas jāpārliecinas, vai ir instalēta Selenium bibliotēka.Komanda uzinstalēs pedējo versiju, vai, ja tas bija iepriekš uzinstalēta atjaunos veco versiju.

    pip install -U selenium
1.Lai parbaudītu kāda bibliotēkas versija ir uzinstalēta

    pip list
2.Lai palaistu skriptu

    python Seiko.py




Izmantotās Python bibliotēkas un to funkcijas:

* import os
Vajadzīga lai atvērtu failus
* import re
Regulāro izteiksmju izmantošana, lai izvilktu modeļa kodus no teksta.
* import time
Lai veidotu pauzes, piemēram time.sleep()
*  from selenium import webdriver
Galvenā bibliotēka pārlūka automatizācijai 
* from selenium.webdriver.chrome.service import Service 
palīdz uzsākt Chrome darbību
* from selenium.webdriver.common.by import By 
Ļauj izmantot dažādus selektoru tipus (By.ID, By.CLASS_NAME, u.c.) strādājot ar HTML
* from selenium.webdriver.support.ui import WebDriverWait
Noteiktu nosacījumu gaidīšana noteiktu laiku pirms skripta izpildes
* from selenium.webdriver.support import expected_conditions as EC
Sniedz gatavu nosacījumu sarakstu, piemēram:
"element_to_be_clickable" un "presence_of_element_located"
