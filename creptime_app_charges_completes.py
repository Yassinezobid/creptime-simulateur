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
st.sidebar.header("🏗️ Charges d'Investissement")
st.sidebar.markdown("### 🛠️ Équipements")
crepier_min = st.sidebar.number_input("Crépier MIN (MAD)", value=6000)
crepier_max = st.sidebar.number_input("Crépier MAX (MAD)", value=8000)
gauffrier_min = st.sidebar.number_input("Gauffrier MIN (MAD)", value=3000)
gauffrier_max = st.sidebar.number_input("Gauffrier MAX (MAD)", value=4500)
plaque_min = st.sidebar.number_input("Plaque & Pancakes MIN (MAD)", value=500)
plaque_max = st.sidebar.number_input("Plaque & Pancakes MAX (MAD)", value=800)
blender_min = st.sidebar.number_input("Blender MIN (MAD)", value=1000)
blender_max = st.sidebar.number_input("Blender MAX (MAD)", value=2000)
extracteur_min = st.sidebar.number_input("Extracteur de jus MIN (MAD)", value=1500)
extracteur_max = st.sidebar.number_input("Extracteur de jus MAX (MAD)", value=3000)
machine_cafe_min = st.sidebar.number_input("Machine à café MIN (MAD)", value=30000)
machine_cafe_max = st.sidebar.number_input("Machine à café MAX (MAD)", value=30000)
vitrine_min = st.sidebar.number_input("Vitrine 2 glaces MIN (MAD)", value=15000)
vitrine_max = st.sidebar.number_input("Vitrine 2 glaces MAX (MAD)", value=20000)
frigo_min = st.sidebar.number_input("Réfrigérateur MIN (MAD)", value=5000)
frigo_max = st.sidebar.number_input("Réfrigérateur MAX (MAD)", value=5000)
congel_min = st.sidebar.number_input("Congélateur MIN (MAD)", value=3000)
congel_max = st.sidebar.number_input("Congélateur MAX (MAD)", value=3000)
presse_min = st.sidebar.number_input("Presse agrume MIN (MAD)", value=1000)
presse_max = st.sidebar.number_input("Presse agrume MAX (MAD)", value=2500)
ustensiles_min = st.sidebar.number_input("Ustensiles MIN (MAD)", value=4000)
ustensiles_max = st.sidebar.number_input("Ustensiles MAX (MAD)", value=4000)
produits_init_min = st.sidebar.number_input("Produits initiaux MIN (MAD)", value=20000)
produits_init_max = st.sidebar.number_input("Produits initiaux MAX (MAD)", value=20000)

st.sidebar.markdown("### 🧱 Aménagement / Design Intérieur")
peinture_min = st.sidebar.number_input("Peinture & Travaux MIN (MAD)", value=10000)
peinture_max = st.sidebar.number_input("Peinture & Travaux MAX (MAD)", value=10000)
deco_min = st.sidebar.number_input("Décoration & Lumières MIN (MAD)", value=20000)
deco_max = st.sidebar.number_input("Décoration & Lumières MAX (MAD)", value=20000)
etageres_min = st.sidebar.number_input("Étagères MIN (MAD)", value=3500)
etageres_max = st.sidebar.number_input("Étagères MAX (MAD)", value=3500)
comptoir_min = st.sidebar.number_input("Comptoir MIN (MAD)", value=5000)
comptoir_max = st.sidebar.number_input("Comptoir MAX (MAD)", value=5000)
tables_min = st.sidebar.number_input("Tables + Chaises MIN (MAD)", value=2500)
tables_max = st.sidebar.number_input("Tables + Chaises MAX (MAD)", value=2500)
panneaux_min = st.sidebar.number_input("Panneaux (extérieur) MIN (MAD)", value=10000)
panneaux_max = st.sidebar.number_input("Panneaux (extérieur) MAX (MAD)", value=10000)
tv_min = st.sidebar.number_input("TV + Caisse MIN (MAD)", value=10000)
tv_max = st.sidebar.number_input("TV + Caisse MAX (MAD)", value=10000)
cameras_min = st.sidebar.number_input("Caméras MIN (MAD)", value=3000)
cameras_max = st.sidebar.number_input("Caméras MAX (MAD)", value=3000)

st.sidebar.markdown("### 📦 Divers")
loyer2_min = st.sidebar.number_input("Loyer 2 mois MIN (MAD)", value=18000)
loyer2_max = st.sidebar.number_input("Loyer 2 mois MAX (MAD)", value=18000)
publanc_min = st.sidebar.number_input("Publicités de lancement MIN (MAD)", value=15000)
publanc_max = st.sidebar.number_input("Publicités de lancement MAX (MAD)", value=15000)

equipements_min = sum([
    crepier_min, gauffrier_min, plaque_min, blender_min, extracteur_min,
    machine_cafe_min, vitrine_min, frigo_min, congel_min,
    presse_min, ustensiles_min, produits_init_min
])
equipements_max = sum([
    crepier_max, gauffrier_max, plaque_max, blender_max, extracteur_max,
    machine_cafe_max, vitrine_max, frigo_max, congel_max,
    presse_max, ustensiles_max, produits_init_max
])
amenagement_min = sum([
    peinture_min, deco_min, etageres_min, comptoir_min,
    tables_min, panneaux_min, tv_min, cameras_min
])
amenagement_max = sum([
    peinture_max, deco_max, etageres_max, comptoir_max,
    tables_max, panneaux_max, tv_max, cameras_max
])
divers_min = loyer2_min + publanc_min
divers_max = loyer2_max + publanc_max

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
    commandes_min["crepe"] * prix_crepe +
    commandes_min["gaufre"] * prix_gaufre +
    commandes_min["pancake"] * prix_pancake +
    commandes_min["glace"] * prix_glace +
    commandes_min["bowl"] * prix_bowl +
    commandes_min["jus"] * prix_jus +
    commandes_min["boisson"] * prix_boisson_chaude
) * jours_mois
revenu_brut_max = (
    commandes_max["crepe"] * prix_crepe +
    commandes_max["gaufre"] * prix_gaufre +
    commandes_max["pancake"] * prix_pancake +
    commandes_max["glace"] * prix_glace +
    commandes_max["bowl"] * prix_bowl +
    commandes_max["jus"] * prix_jus +
    commandes_max["boisson"] * prix_boisson_chaude
) * jours_mois

cout_total_min = (
    commandes_min["crepe"] * cout_crepe +
    commandes_min["gaufre"] * cout_gaufre +
    commandes_min["pancake"] * cout_pancake +
    commandes_min["glace"] * cout_glace +
    commandes_min["bowl"] * cout_bowl +
    commandes_min["jus"] * cout_jus +
    commandes_min["boisson"] * cout_boisson_chaude
) * jours_mois
cout_total_max = (
    commandes_max["crepe"] * cout_crepe +
    commandes_max["gaufre"] * cout_gaufre +
    commandes_max["pancake"] * cout_pancake +
    commandes_max["glace"] * cout_glace +
    commandes_max["bowl"] * cout_bowl +
    commandes_max["jus"] * cout_jus +
    commandes_max["boisson"] * cout_boisson_chaude
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
st.markdown(f"💸 **Profit Net Moyenne : {profit_net_moy:,.0f} MAD**")
