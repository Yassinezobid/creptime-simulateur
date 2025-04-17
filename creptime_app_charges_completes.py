import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Complet", layout="wide")
st.title("🥞 Simulateur de Rentabilité - Crêp'Time (Meknès)")

# === Produits : prix, coût ===
st.sidebar.header("💾 Paramètres Produits & Marges")

# Crêpes Sucrées
st.sidebar.markdown("### 🥞 Crêpes Sucrées ")
prix_crepe = st.sidebar.number_input("Prix crêpe (MAD)", value=30)
cout_crepe = st.sidebar.number_input("Coût crêpe (MP)", value=10)

# Gaufres Sucrées
st.sidebar.markdown("### 🧇 Gaufres Sucrées")
prix_gaufre = st.sidebar.number_input("Prix gaufre (MAD)", value=28)
cout_gaufre = st.sidebar.number_input("Coût gaufre (MP)", value=9)

# Pancakes
st.sidebar.markdown("### 🥞 Pancakes")
prix_pancake = st.sidebar.number_input("Prix pancake (MAD)", value=32)
cout_pancake = st.sidebar.number_input("Coût pancake (MP)", value=11)

# Coupes Glacées
st.sidebar.markdown("### 🍦 Coupes Glacées")
prix_glace = st.sidebar.number_input("Prix coupe glacée (MAD)", value=35)
cout_glace = st.sidebar.number_input("Coût coupe glacée (MP)", value=12)

# Salades & Bowls
st.sidebar.markdown("### 🍓 Salades & Bowls Fraîcheur")
prix_bowl = st.sidebar.number_input("Prix bowl/salade (MAD)", value=30)
cout_bowl = st.sidebar.number_input("Coût bowl/salade (MP)", value=10)

# Smoothies & Jus
st.sidebar.markdown("### 🥤 Smoothies & Jus Frais")
prix_jus = st.sidebar.number_input("Prix jus/smoothie (MAD)", value=20)
cout_jus = st.sidebar.number_input("Coût jus/smoothie (MP)", value=7)

# Boissons Chaudes
st.sidebar.markdown("### ☕ Boissons Chaudes")
prix_boisson_chaude = st.sidebar.number_input("Prix boisson chaude (MAD)", value=15)
cout_boisson_chaude = st.sidebar.number_input("Coût boisson chaude (MP)", value=5)

# === Paramètres de gestion ===
st.sidebar.header("⚙️ Commandes journalières")
commandes = {
    "crepe": st.sidebar.number_input("Commandes crêpe", value=100),
    "gaufre": st.sidebar.number_input("Commandes gaufre", value=80),
    "pancake": st.sidebar.number_input("Commandes pancake", value=60),
    "glace": st.sidebar.number_input("Commandes coupe glacée", value=50),
    "bowl": st.sidebar.number_input("Commandes bowl/salade", value=40),
    "jus": st.sidebar.number_input("Commandes jus/smoothie", value=70),
    "boisson": st.sidebar.number_input("Commandes boisson chaude", value=90),
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
    commandes["crepe"] * prix_crepe +
    commandes["gaufre"] * prix_gaufre +
    commandes["pancake"] * prix_pancake +
    commandes["glace"] * prix_glace +
    commandes["bowl"] * prix_bowl +
    commandes["jus"] * prix_jus +
    commandes["boisson"] * prix_boisson_chaude
) * jours_mois
revenu_brut_max = (
    commandes["crepe"] * prix_crepe +
    commandes["gaufre"] * prix_gaufre +
    commandes["pancake"] * prix_pancake +
    commandes["glace"] * prix_glace +
    commandes["bowl"] * prix_bowl +
    commandes["jus"] * prix_jus +
    commandes["boisson"] * prix_boisson_chaude
) * jours_mois

cout_total_min = (
    commandes["crepe"] * cout_crepe +
    commandes["gaufre"] * cout_gaufre +
    commandes["pancake"] * cout_pancake +
    commandes["glace"] * cout_glace +
    commandes["bowl"] * cout_bowl +
    commandes["jus"] * cout_jus +
    commandes["boisson"] * cout_boisson_chaude
) * jours_mois
cout_total_max = (
    commandes["crepe"] * cout_crepe +
    commandes["gaufre"] * cout_gaufre +
    commandes["pancake"] * cout_pancake +
    commandes["glace"] * cout_glace +
    commandes["bowl"] * cout_bowl +
    commandes["jus"] * cout_jus +
    commandes["boisson"] * cout_boisson_chaude
) * jours_mois

benefice_avant_impot_min = revenu_brut_min - cout_total_max - charges_mensuelles_max
benefice_avant_impot_max = revenu_brut_max - cout_total_min - charges_mensuelles_min

impot_min = max(0, benefice_avant_impot_min * impot_taux)
impot_max = max(0, benefice_avant_impot_max * impot_taux)

profit_net_min = benefice_avant_impot_min - impot_min
profit_net_max = benefice_avant_impot_max - impot_max

part_associe_min = profit_net_min / associes
part_associe_max = profit_net_max / associes

# === Compute averages ===
charges_fixes_totales_moy = (charges_fixes_totales_min + charges_fixes_totales_max) / 2
charges_mensuelles_moy = (charges_mensuelles_min + charges_mensuelles_max) / 2
revenu_brut_moy = (revenu_brut_min + revenu_brut_max) / 2
cout_total_moy = (cout_total_min + cout_total_max) / 2
benefice_avant_impot_moy = (benefice_avant_impot_min + benefice_avant_impot_max) / 2
impot_moy = (impot_min + impot_max) / 2
profit_net_moy = (profit_net_min + profit_net_max) / 2
part_associe_moy = (part_associe_min + part_associe_max) / 2

# === Affichage résultats ===
st.subheader("📊 Résultats de Simulation")
df_range = pd.DataFrame([
    {"Metric": "Revenu Brut",      "Min": revenu_brut_min,      "Max": revenu_brut_max,      "Moyenne": revenu_brut_moy},
    {"Metric": "Coût MP",          "Min": cout_total_min,        "Max": cout_total_max,        "Moyenne": cout_total_moy},
    {"Metric": "Bénéfice Avant Impôt", "Min": benefice_avant_impot_min, "Max": benefice_avant_impot_max, "Moyenne": benefice_avant_impot_moy},
    {"Metric": "Impôt",            "Min": impot_min,             "Max": impot_max,             "Moyenne": impot_moy},
    {"Metric": "Profit Net",       "Min": profit_net_min,        "Max": profit_net_max,        "Moyenne": profit_net_moy},
    {"Metric": "Part par Associé", "Min": part_associe_min,      "Max": part_associe_max,      "Moyenne": part_associe_moy},
])
st.dataframe(df_range.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}", "Moyenne": "{:,.0f}"}))

st.subheader("📈 Graphique : Profit Net & Part Associé")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(["Profit Net Min", "Profit Net Max", "Part par Associé Min", "Part par Associé Max"], [profit_net_min, profit_net_max, part_associe_min, part_associe_max])
ax.set_ylabel("MAD")
ax.set_title("Profit Net mensuel & Part Associé")
ax.grid(True)
st.pyplot(fig)

st.subheader("💼 Charges d’Investissement")
df_inv = pd.DataFrame([
    {"Catégorie": "Équipements",                  "Min": equipements_min,          "Max": equipements_max,          "Moyenne": (equipements_min + equipements_max) / 2},
    {"Catégorie": "Aménagement / Design Intérieur","Min": amenagement_min,         "Max": amenagement_max,         "Moyenne": (amenagement_min + amenagement_max) / 2},
    {"Catégorie": "Divers",                       "Min": divers_min,              "Max": divers_max,              "Moyenne": (divers_min + divers_max) / 2},
    {"Catégorie": "TOTAL",                        "Min": charges_fixes_totales_min,"Max": charges_fixes_totales_max, "Moyenne": charges_fixes_totales_moy},
])
st.dataframe(df_inv.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}", "Moyenne": "{:,.0f}"}))

st.subheader("📊 Résultats de Simulation (Min & Max)")
df_profit = pd.DataFrame([
    {"Metric": "Profit Net",       "Min": profit_net_min,   "Max": profit_net_max,   "Moyenne": profit_net_moy},
    {"Metric": "Part par Associé", "Min": part_associe_min, "Max": part_associe_max, "Moyenne": part_associe_moy},
])
st.dataframe(df_profit.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}", "Moyenne": "{:,.0f}"}))
