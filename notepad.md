# Konsistens i returverdier
Noen funksjoner returnerer True, noen returnerer False, noen returnerer ingenting og bare kaster feil. Tenk på om dette gir et tydelig og forutsigbart API.

# Navngivning vs faktisk logikk
Sjekk om funksjonsnavnene matcher nøyaktig det de gjør (f.eks. “has” vs “is”, og hva True/False faktisk betyr).

# Flytkontroll / lesbarhet
Tenk på om kontrollflyten er lett å følge:
“hva skjer først, hva kan feile, hva betyr det at vi kommer helt til slutten?”

# Ansvar per funksjon
Hver funksjon gjør én sjekk – bra.
Tenk på om noen av dem også implisitt gjør mer enn én ting (f.eks. både sjekker og bestemmer konsekvens).

# Normalisering av input
Tenk på om passordet bør behandles “som det er”, eller om du mentalt vil sammenligne på en normalisert form (case, whitespace, osv.).

# Dekningsgrad på ‘lett å gjette’
Tenk på hvor grensen går for hva som er “enkelt å gjette”:
Faste strenger, reverserte strenger, overlapp, deltreff.

# Brukeropplevelse vs sikkerhet
Tenk på hvor mye informasjon du vil gi tilbake ved feil (én regel av gangen vs samlet).

# Testbarhet
Tenk på hvor lett det er å skrive tester for hver regel isolert, og for helheten.

# Rekkefølge på sjekker
Tenk på om rekkefølgen er tilfeldig, logisk, eller bevisst (billige sjekker først, strengere senere).