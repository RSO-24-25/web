# Web service je front end naše aplikacije

Zgrajen je z uporabo **Streamlit**. Omogoča uporabnikom upravljanje njihovih naročil/produktov, ustvarjanje novih produktov, posodabljanje količin ter prejemanje e-poštnih obvestil o nakupih in prodajah. Aplikacija vključuje sistem za registracijo in prijavo uporabnikov ter omogoča vizualizacijo gibanja cen produktov skozi čas.

## Funkcijonalnosti
- **Avtentifikacija uporabnikov**: Stran za prijavo in stran za registracijo, ki komunicirata z mikrostoritvijo za upravljanje z uporabniki
- **Upravljanje produktov**: Uporabniki lahko ogledajo, dodajo, posodobijo in izbrišejo produkte v svojem inventarju. Tu Web service komunicira preko GraphQL s mikrostoritvijo za upravljanje z inventarjem.
- **Grafi cen**: Tu uporabniki lahko izbirajo med produkti, in si ogledajo premikanje cen teh izdelkov skozi čas.
- **Izdajanje računov**: Tu je tudi uporabniški vmesnik za izdajanje računov.

## Tehnična sestava

- **Frontend**: Streamlit
- **Backend**: Python
- **E-poštna storitev**: gRPC komunikacija za pošiljanje e-poštnih obvestil
- **Storitev za inventar**: GraphQL komunikacija z storitvijo za hranjenje podatkov o trenutnih stanjih zaloge
- **Druge knjižnice**: `streamlit_cookies_manager` za upravljanje piškotkov...

## Namestitev

### Predpogoji

- Python 3.7 ali novejši
- gRPC e-poštna storitev (poskrbite, da je pravilno nastavljena)

### Koraki

   ```bash
     git clone https://github.com/yourusername/oims.git
     cd oims

    python -m venv venv
    source venv/bin/activate  # Na Windows uporabite `venv\Scripts\activate`

    pip install -r requirements.txt```




