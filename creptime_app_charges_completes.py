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

# === Charges fixes ===
st.sidebar.header("🏗️ Charges d'Investissement")

st.sidebar.markdown("### 🛠️ Équipements")
equipements = {
    "Crépier": st.sidebar.slider("Crépier (MAD)", 6000, 8000, 7000),
    "Gauffrier": st.sidebar.slider("Gauffrier (MAD)", 3000, 4500, 3750),
    "Plaque & Pancakes": st.sidebar.slider("Plaque & Pancakes (MAD)", 500, 800, 650),
    "Blender": st.sidebar.slider("Blender (MAD)", 1000, 2000, 1500),
    "Extracteur de jus": st.sidebar.slider("Extracteur de jus (MAD)", 1500, 3000, 2250),
    "Machine à café": st.sidebar.slider("Machine à café (MAD)", 29000, 31000, 30000),
    "Vitrine 2 glaces": st.sidebar.slider("Vitrine 2 glaces (MAD)", 15000, 20000, 17500),
    "Réfrigérateur": st.sidebar.slider("Réfrigérateur (MAD)", 4800, 5200, 5000),
    "Congélateur": st.sidebar.slider("Congélateur (MAD)", 2800, 3200, 3000),
    "Presse agrume": st.sidebar.slider("Presse agrume (MAD)", 1000, 2500, 1750),
    "Ustensiles": st.sidebar.slider("Ustensiles (MAD)", 3800, 4200, 4000),
    "Produits initiaux": st.sidebar.slider("Produits initiaux (MAD)", 18000, 22000, 20000)
}

st.sidebar.markdown("### 🧱 Aménagement / Design Intérieur")
amenagement = {
    "Peinture & Travaux": st.sidebar.slider("Peinture & Travaux (MAD)", 9000, 11000, 10000),
    "Décoration & Lumières": st.sidebar.slider("Décoration & Lumières (MAD)", 19000, 21000, 20000),
    "Étagères": st.sidebar.slider("Étagères (MAD)", 3300, 3700, 3500),
    "Comptoir": st.sidebar.slider("Comptoir (MAD)", 4800, 5200, 5000),
    "Tables + Chaises": st.sidebar.slider("Tables + Chaises (MAD)", 2300, 2700, 2500),
    "Panneaux (extérieur)": st.sidebar.slider("Panneaux (extérieur) (MAD)", 9000, 11000, 10000),
    "TV + Caisse": st.sidebar.slider("TV + Caisse (MAD)", 9500, 10500, 10000),
    "Caméras": st.sidebar.slider("Caméras (MAD)", 2800, 3200, 3000)
}

st.sidebar.markdown("### 📦 Divers")
divers = {
    "Loyer 2 mois": st.sidebar.slider("Loyer 2 mois (MAD)", 17000, 19000, 18000),
    "Publicités de lancement": st.sidebar.slider("Publicités de lancement (MAD)", 14000, 16000, 15000)
}

equipements_min = 6000+3000+500+1000+1500+29000+15000+4800+2800+1000+3800+18000
equipements_max = 8000+4500+800+2000+3000+31000+20000+5200+3200+2500+4200+22000

amenagement_min = 9000+19000+3300+4800+2300+9000+9500+2800
amenagement_max = 11000+21000+3700+5200+2700+11000+10500+3200

divers_min = 17000+14000
divers_max = 19000+16000

charges_fixes_totales_min = equipements_min + amenagement_min + divers_min
charges_fixes_totales_max = equipements_max + amenagement_max + divers_max

part_fixe_associe = charges_fixes_totales_min / associes

# === Charges mensuelles ===
st.sidebar.header("🗖️ Charges Mensuelles")
loyer = st.sidebar.number_input("Loyer", value=7000)
salaire_employes = st.sidebar.number_input("Salaires employés (2)", value=6000)
salaire_menage = st.sidebar.number_input("Femme de ménage", value=1000)
electricite = st.sidebar.number_input("Électricité", value=4000)
internet = st.sidebar.number_input("Internet", value=300)
publicite = st.sidebar.number_input("Publicité / Réseaux", value=2000)
divers_mensuels = st.sidebar.number_input("Divers mensuels", value=1000)
charges_mensuelles = sum([
    loyer, salaire_employes, salaire_menage,
    electricite, internet, publicite, divers_mensuels
])
part_mensuelle_associe = charges_mensuelles / associes

# === Simulation ===
revenu_brut_min = (
    commandes["crepe"] * prix_crepe_min +
    commandes["gaufre"] * prix_gaufre_min +
    commandes["pancake"] * prix_pancake_min +
    commandes["glace"] * prix_glace_min +
    commandes["bowl"] * prix_bowl_min +
    commandes["jus"] * prix_jus_min +
    commandes["boisson"] * prix_boisson_chaude_min
) * jours_mois
revenu_brut_max = (
    commandes["crepe"] * prix_crepe_max +
    commandes["gaufre"] * prix_gaufre_max +
    commandes["pancake"] * prix_pancake_max +
    commandes["glace"] * prix_glace_max +
    commandes["bowl"] * prix_bowl_max +
    commandes["jus"] * prix_jus_max +
    commandes["boisson"] * prix_boisson_chaude_max
) * jours_mois

cout_total_min = (
    commandes["crepe"] * cout_crepe_min +
    commandes["gaufre"] * cout_gaufre_min +
    commandes["pancake"] * cout_pancake_min +
    commandes["glace"] * cout_glace_min +
    commandes["bowl"] * cout_bowl_min +
    commandes["jus"] * cout_jus_min +
    commandes["boisson"] * cout_boisson_chaude_min
) * jours_mois
cout_total_max = (
    commandes["crepe"] * cout_crepe_max +
    commandes["gaufre"] * cout_gaufre_max +
    commandes["pancake"] * cout_pancake_max +
    commandes["glace"] * cout_glace_max +
    commandes["bowl"] * cout_bowl_max +
    commandes["jus"] * cout_jus_max +
    commandes["boisson"] * cout_boisson_chaude_max
) * jours_mois

benefice_avant_impot_min = revenu_brut_min - cout_total_max - charges_mensuelles
benefice_avant_impot_max = revenu_brut_max - cout_total_min - charges_mensuelles

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
df_ranges = pd.DataFrame([
    {"Catégorie": "Équipements",                  "Min": equipements_min,          "Max": equipements_max},
    {"Catégorie": "Aménagement / Design Intérieur","Min": amenagement_min,         "Max": amenagement_max},
    {"Catégorie": "Divers",                       "Min": divers_min,              "Max": divers_max},
    {"Catégorie": "TOTAL",                        "Min": charges_fixes_totales_min,"Max": charges_fixes_totales_max},
])
st.dataframe(df_ranges.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}"}))

st.subheader("📅 Charges Mensuelles")
df_mensuelles = pd.DataFrame({
    "Poste": ["Loyer", "Salaires", "Ménage", "Électricité", "Internet", "Publicité", "Divers"],
    "Montant": [loyer, salaire_employes, salaire_menage, electricite, internet, publicite, divers_mensuels]
})
df_mensuelles.loc["Total"] = ["TOTAL", charges_mensuelles]
st.dataframe(df_mensuelles)
st.markdown(f"💸 **Part Mensuelle Associé : {part_mensuelle_associe:,.0f} MAD**")
