import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Complet", layout="wide")
st.title("🥞 Simulateur de Rentabilité - Crêp'Time (Meknès)")

# === Produits : prix, coût ===
st.sidebar.header("💾 Paramètres Produits & Marges")

# Crêpes Sucrées
st.sidebar.markdown("### 🥞 Crêpes Sucrées ")
prix_crepe_min = st.sidebar.number_input("Prix crêpe MIN (MAD)", value=25)
prix_crepe_max = st.sidebar.number_input("Prix crêpe MAX (MAD)", value=35)
cout_crepe_min = st.sidebar.number_input("Coût crêpe MIN (MP)", value=8)
cout_crepe_max = st.sidebar.number_input("Coût crêpe MAX (MP)", value=12)

# Gaufres Sucrées
st.sidebar.markdown("### 🧇 Gaufres Sucrées")
prix_gaufre_min = st.sidebar.number_input("Prix gaufre MIN (MAD)", value=18)
prix_gaufre_max = st.sidebar.number_input("Prix gaufre MAX (MAD)", value=38)
cout_gaufre_min = st.sidebar.number_input("Coût gaufre MIN (MP)", value=7)
cout_gaufre_max = st.sidebar.number_input("Coût gaufre MAX (MP)", value=11)

# Pancakes
st.sidebar.markdown("### 🥞 Pancakes")
prix_pancake_min = st.sidebar.number_input("Prix pancake MIN (MAD)", value=27)
prix_pancake_max = st.sidebar.number_input("Prix pancake MAX (MAD)", value=37)
cout_pancake_min = st.sidebar.number_input("Coût pancake MIN (MP)", value=9)
cout_pancake_max = st.sidebar.number_input("Coût pancake MAX (MP)", value=13)

# Coupes Glacées
st.sidebar.markdown("### 🍦 Coupes Glacées")
prix_glace_min = st.sidebar.number_input("Prix coupe glacée MIN (MAD)", value=30)
prix_glace_max = st.sidebar.number_input("Prix coupe glacée MAX (MAD)", value=40)
cout_glace_min = st.sidebar.number_input("Coût coupe glacée MIN (MP)", value=10)
cout_glace_max = st.sidebar.number_input("Coût coupe glacée MAX (MP)", value=14)

# Salades & Bowls
st.sidebar.markdown("### 🍓 Salades & Bowls Fraîcheur")
prix_bowl_min = st.sidebar.number_input("Prix bowl/salade MIN (MAD)", value=25)
prix_bowl_max = st.sidebar.number_input("Prix bowl/salade MAX (MAD)", value=35)
cout_bowl_min = st.sidebar.number_input("Coût bowl/salade MIN (MP)", value=8)
cout_bowl_max = st.sidebar.number_input("Coût bowl/salade MAX (MP)", value=12)

# Smoothies & Jus
st.sidebar.markdown("### 🥤 Smoothies & Jus Frais")
prix_jus_min = st.sidebar.number_input("Prix jus/smoothie MIN (MAD)", value=15)
prix_jus_max = st.sidebar.number_input("Prix jus/smoothie MAX (MAD)", value=25)
cout_jus_min = st.sidebar.number_input("Coût jus/smoothie MIN (MP)", value=5)
cout_jus_max = st.sidebar.number_input("Coût jus/smoothie MAX (MP)", value=9)

# Boissons Chaudes
st.sidebar.markdown("### ☕ Boissons Chaudes")
prix_boisson_chaude_min = st.sidebar.number_input("Prix boisson chaude MIN (MAD)", value=10)
prix_boisson_chaude_max = st.sidebar.number_input("Prix boisson chaude MAX (MAD)", value=20)
cout_boisson_chaude_min = st.sidebar.number_input("Coût boisson chaude MIN (MP)", value=3)
cout_boisson_chaude_max = st.sidebar.number_input("Coût boisson chaude MAX (MP)", value=7)

# === Paramètres de gestion ===
st.sidebar.header("⚙️ Commandes journalières")
st.sidebar.markdown("### Plage Commandes par jour")
# Crêpes
crepe_min = st.sidebar.number_input("Commandes crêpe MIN", value=80)
crepe_max = st.sidebar.number_input("Commandes crêpe MAX", value=120)
# Gaufres
gaufre_min = st.sidebar.number_input("Commandes gaufre MIN", value=60)
gaufre_max = st.sidebar.number_input("Commandes gaufre MAX", value=100)
# Pancakes
pancake_min = st.sidebar.number_input("Commandes pancake MIN", value=50)
pancake_max = st.sidebar.number_input("Commandes pancake MAX", value=70)
# Coupes Glacées
glace_min = st.sidebar.number_input("Commandes coupe glacée MIN", value=40)
glace_max = st.sidebar.number_input("Commandes coupe glacée MAX", value=60)
# Salades & Bowls
bowl_min = st.sidebar.number_input("Commandes bowl/salade MIN", value=30)
bowl_max = st.sidebar.number_input("Commandes bowl/salade MAX", value=50)
# Smoothies & Jus
jus_min = st.sidebar.number_input("Commandes jus/smoothie MIN", value=50)
jus_max = st.sidebar.number_input("Commandes jus/smoothie MAX", value=90)
# Boissons Chaudes
boisson_min = st.sidebar.number_input("Commandes boisson chaude MIN", value=70)
boisson_max = st.sidebar.number_input("Commandes boisson chaude MAX", value=110)

commandes_min = {
    "crepe": crepe_min, "gaufre": gaufre_min,
    "pancake": pancake_min, "glace": glace_min,
    "bowl": bowl_min, "jus": jus_min, "boisson": boisson_min
}
commandes_max = {
    "crepe": crepe_max, "gaufre": gaufre_max,
    "pancake": pancake_max, "glace": glace_max,
    "bowl": bowl_max, "jus": jus_max, "boisson": boisson_max
}

jours_mois = st.sidebar.slider("Jours d'activité par mois", 20, 31, 30)
associes = st.sidebar.number_input("Nombre d'associés", value=6)
impot_taux = st.sidebar.slider("Taux impôt (%)", 0, 50, 20) / 100

# === Charges d'Investissement ===
equipements_range = {
    "Crépier": (6000, 8000),
    "Gauffrier": (3000, 4500),
    "Plaque & Pancakes": (500, 800),
    "Blender": (1000, 2000),
    "Extracteur de jus": (1500, 3000),
    "Machine à café": (30000, 30000),
    "Vitrine 2 glaces": (15000, 20000),
    "Réfrigérateur": (5000, 5000),
    "Congélateur": (3000, 3000),
    "Presse agrume": (1000, 2500),
    "Ustensiles": (4000, 4000),
    "Produits initiaux": (20000, 20000)
}

amenagement_range = {
    "Peinture & Travaux": (10000, 10000),
    "Décoration & Lumières": (20000, 20000),
    "Étagères": (3500, 3500),
    "Comptoir": (5000, 5000),
    "Tables + Chaises": (2500, 2500),
    "Panneaux (extérieur)": (10000, 10000),
    "TV + Caisse": (10000, 10000),
    "Caméras": (3000, 3000)
}

divers_range = {
    "Loyer 2 mois": (18000, 18000),
    "Publicités de lancement": (15000, 15000)
}

equipements_min = sum(v[0] for v in equipements_range.values())
equipements_max = sum(v[1] for v in equipements_range.values())
amenagement_min = sum(v[0] for v in amenagement_range.values())
amenagement_max = sum(v[1] for v in amenagement_range.values())
divers_min = sum(v[0] for v in divers_range.values())
divers_max = sum(v[1] for v in divers_range.values())

charges_fixes_totales_min = equipements_min + amenagement_min + divers_min
charges_fixes_totales_max = equipements_max + amenagement_max + divers_max

# === Charges mensuelles ===
st.sidebar.header("🗖️ Charges Mensuelles")
loyer_min = st.sidebar.number_input("Loyer MIN (MAD)", value=6300)
loyer_max = st.sidebar.number_input("Loyer MAX (MAD)", value=7700)
salaire_employes_min = st.sidebar.number_input("Salaires employés (2) MIN (MAD)", value=5400)
salaire_employes_max = st.sidebar.number_input("Salaires employés (2) MAX (MAD)", value=6600)
salaire_menage_min = st.sidebar.number_input("Femme de ménage MIN (MAD)", value=900)
salaire_menage_max = st.sidebar.number_input("Femme de ménage MAX (MAD)", value=1100)
electricite_min = st.sidebar.number_input("Électricité MIN (MAD)", value=3600)
electricite_max = st.sidebar.number_input("Électricité MAX (MAD)", value=4400)
internet_min = st.sidebar.number_input("Internet MIN (MAD)", value=270)
internet_max = st.sidebar.number_input("Internet MAX (MAD)", value=330)
publicite_min = st.sidebar.number_input("Publicité / Réseaux MIN (MAD)", value=1800)
publicite_max = st.sidebar.number_input("Publicité / Réseaux MAX (MAD)", value=2200)
divers_mensuels_min = st.sidebar.number_input("Divers mensuels MIN (MAD)", value=900)
divers_mensuels_max = st.sidebar.number_input("Divers mensuels MAX (MAD)", value=1100)

charges_mensuelles_min = sum([
    loyer_min, salaire_employes_min, salaire_menage_min,
    electricite_min, internet_min, publicite_min, divers_mensuels_min
])
charges_mensuelles_max = sum([
    loyer_max, salaire_employes_max, salaire_menage_max,
    electricite_max, internet_max, publicite_max, divers_mensuels_max
])

# === Simulation ===
revenu_brut_min = (
    commandes_min["crepe"] * prix_crepe_min +
    commandes_min["gaufre"] * prix_gaufre_min +
    commandes_min["pancake"] * prix_pancake_min +
    commandes_min["glace"] * prix_glace_min +
    commandes_min["bowl"] * prix_bowl_min +
    commandes_min["jus"] * prix_jus_min +
    commandes_min["boisson"] * prix_boisson_chaude_min
) * jours_mois
revenu_brut_max = (
    commandes_max["crepe"] * prix_crepe_max +
    commandes_max["gaufre"] * prix_gaufre_max +
    commandes_max["pancake"] * prix_pancake_max +
    commandes_max["glace"] * prix_glace_max +
    commandes_max["bowl"] * prix_bowl_max +
    commandes_max["jus"] * prix_jus_max +
    commandes_max["boisson"] * prix_boisson_chaude_max
) * jours_mois

cout_total_min = (
    commandes_min["crepe"] * cout_crepe_min +
    commandes_min["gaufre"] * cout_gaufre_min +
    commandes_min["pancake"] * cout_pancake_min +
    commandes_min["glace"] * cout_glace_min +
    commandes_min["bowl"] * cout_bowl_min +
    commandes_min["jus"] * cout_jus_min +
    commandes_min["boisson"] * cout_boisson_chaude_min
) * jours_mois
cout_total_max = (
    commandes_max["crepe"] * cout_crepe_max +
    commandes_max["gaufre"] * cout_gaufre_max +
    commandes_max["pancake"] * cout_pancake_max +
    commandes_max["glace"] * cout_glace_max +
    commandes_max["bowl"] * cout_bowl_max +
    commandes_max["jus"] * cout_jus_max +
    commandes_max["boisson"] * cout_boisson_chaude_max
) * jours_mois

benefice_avant_impot_min = revenu_brut_min - cout_total_max - charges_mensuelles_max
benefice_avant_impot_max = revenu_brut_max - cout_total_min - charges_mensuelles_min

impot_min = max(0, benefice_avant_impot_min * impot_taux)
impot_max = max(0, benefice_avant_impot_max * impot_taux)

profit_net_min = benefice_avant_impot_min - impot_min
profit_net_max = benefice_avant_impot_max - impot_max

part_associe_min = profit_net_min / associes
part_associe_max = profit_net_max / associes

# === Affichage résultats ===
st.subheader("📊 Résultats de Simulation")
df_range = pd.DataFrame([
    {"Metric": "Revenu Brut",      "Min": revenu_brut_min,      "Max": revenu_brut_max},
    {"Metric": "Coût MP",          "Min": cout_total_min,        "Max": cout_total_max},
    {"Metric": "Bénéfice Avant Impôt", "Min": benefice_avant_impot_min, "Max": benefice_avant_impot_max},
    {"Metric": "Impôt",            "Min": impot_min,             "Max": impot_max},
    {"Metric": "Profit Net",       "Min": profit_net_min,        "Max": profit_net_max},
    {"Metric": "Part par Associé", "Min": part_associe_min,      "Max": part_associe_max},
])
st.dataframe(df_range.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}"}))

st.subheader("📈 Graphique : Profit Net & Part Associé")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(["Profit Net Min", "Profit Net Max", "Part par Associé Min", "Part par Associé Max"], [profit_net_min, profit_net_max, part_associe_min, part_associe_max])
ax.set_ylabel("MAD")
ax.set_title("Profit Net mensuel & Part Associé")
ax.grid(True)
st.pyplot(fig)

st.subheader("💼 Charges d’Investissement")
df_inv = pd.DataFrame([
    {"Catégorie": "Équipements",                  "Min": equipements_min,          "Max": equipements_max},
    {"Catégorie": "Aménagement / Design Intérieur","Min": amenagement_min,         "Max": amenagement_max},
    {"Catégorie": "Divers",                       "Min": divers_min,              "Max": divers_max},
    {"Catégorie": "TOTAL",                        "Min": charges_fixes_totales_min,"Max": charges_fixes_totales_max},
])
st.dataframe(df_inv.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}"}))

st.subheader("📊 Résultats de Simulation (Min & Max)")
df_profit = pd.DataFrame([
    {"Metric": "Profit Net",       "Min": profit_net_min,   "Max": profit_net_max},
    {"Metric": "Part par Associé", "Min": part_associe_min, "Max": part_associe_max},
])
st.dataframe(df_profit.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}"}))
