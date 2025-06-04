# Importer
from math import ceil
from tabulate import tabulate

# Inmatade värden
vagg_bredd = 6.0  # meter
vagg_hojd = 2.5  # meter
brada_bredd = 0.16  # meter
spalt_bredd = 0.005  # meter (5 mm spalt)
tillgangliga_langder = [3.0, 3.6, 4.2, 4.8, 5.1, 5.4, 6.0]  # meter
spill_marginal_procent = 10  # procent

# Effektiv bredd per bräda inklusive spalt
effektiv_bredd = brada_bredd + spalt_bredd

# Räkna ut hur många brädor som behövs
antal_brdor = vagg_bredd / effektiv_bredd
antal_brdor = ceil(antal_brdor)  # Avrunda uppåt till heltal

# Räkna ut total löpmeter som behövs
total_lopmeter = antal_brdor * vagg_hojd

# Skriv ut resultat utan spalt
print("=== Utan spalt ===")
antal_brdor_utan_spalt = ceil(vagg_bredd / brada_bredd)
total_lopmeter_utan_spalt = antal_brdor_utan_spalt * vagg_hojd
print(f"Antal brädor utan spalt: {antal_brdor_utan_spalt} st")
print(f"Total löpmeter utan spalt: {total_lopmeter_utan_spalt:.2f} meter")

# Skriv ut resultat med spalt
print("\n=== Med spalt (5 mm) ===")
print(f"Antal brädor med spalt: {antal_brdor} st")
print(f"Total löpmeter med spalt: {total_lopmeter:.2f} meter")

# Optimering - samla data för tabell
tabell_data = []
basta_langd = None
minst_spill = None
antal_brdor_for_basta_langd = None
total_lopmeter_for_basta_langd = None

for langd in tillgangliga_langder:
    brador_per_lang_brada = langd // vagg_hojd
    if brador_per_lang_brada == 0:
        continue  # denna längd är för kort

    antal_langa_brdor = antal_brdor / brador_per_lang_brada
    antal_langa_brdor = ceil(antal_langa_brdor)

    spill_per_lang_brada = langd - (brador_per_lang_brada * vagg_hojd)
    total_spill = spill_per_lang_brada * antal_langa_brdor

    # total inköpt löpmeter inklusive spill
    total_inkopt_lopmeter = antal_langa_brdor * langd

    tabell_data.append([
        f"{langd:.2f} m",
        int(brador_per_lang_brada),
        antal_langa_brdor,
        f"{total_spill:.2f} m",
        f"{total_inkopt_lopmeter:.2f} m"
    ])

    # Hitta den längd med minst spill
    if (minst_spill is None) or (total_spill < minst_spill):
        minst_spill = total_spill
        basta_langd = langd
        antal_brdor_for_basta_langd = antal_langa_brdor
        total_lopmeter_for_basta_langd = total_inkopt_lopmeter

# Lägg till spillmarginal
spill_marginal = (spill_marginal_procent / 100) * total_lopmeter_for_basta_langd
lopmeter_med_marginal = total_lopmeter_for_basta_langd + spill_marginal

# Räkna ut antal brädor att köpa inkl. marginal
antal_brdor_med_marginal = lopmeter_med_marginal / basta_langd
antal_brdor_med_marginal = ceil(antal_brdor_med_marginal)

# Skriv ut snygg tabell
print("\n=== Optimering - jämförelse av långa brädor ===")
headers = ["Brädlängd", "Bitar/bräda", "Brädor att köpa", "Total spill", "Inköpt löpmeter"]
print(tabulate(tabell_data, headers=headers, tablefmt="github"))

# Presentera bästa valet snyggt
summary_data = [
    ["Bästa längd", f"{basta_langd} m"],
    ["Beräknat spill", f"{minst_spill:.2f} m"],
    ["Total inköpt löpmeter (utan marginal)", f"{total_lopmeter_for_basta_langd:.2f} m"],
    [f"Total inköpt löpmeter (inkl. {spill_marginal_procent}% marginal)", f"{lopmeter_med_marginal:.2f} m"],
    [f"Antal brädor att köpa (inkl. {spill_marginal_procent}% marginal)", f"{antal_brdor_med_marginal} st"]
]

print("\n=== Rekommenderad inköpsplan ===")
print(tabulate(summary_data, tablefmt="github"))
