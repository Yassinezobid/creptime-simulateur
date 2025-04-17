import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Crêp'Time - Simulateur Mensuel", layout="wide")
st.title("🥞 Simulateur de Profit Net Mensuel")
# Logo de l’application (chargement sécurisé)
if os.path.exists("logo.png"):
    st.image("logo.png", width=200)
else:
    st.warning("Logo introuvable : placez 'logo.png' dans le dossier de l’application.")

# === Paramètres Produits ===
st.sidebar.markdown("<h2 style='color:#ff6347'>💾 Paramètres Produits</h2>", unsafe_allow_html=True)

# -- Crêpes Sucrées --
st.sidebar.markdown("<h3 style='color:#d2691e'>🥞 Crêpes Sucrées</h3>", unsafe_allow_html=True)
prix_crepe = st.sidebar.number_input("Prix crêpe (MAD)", value=30)
cout_crepe = st.sidebar.number_input("Coût crêpe (MAD)", value=10)
st.sidebar.write("")

# -- Gaufres Sucrées --
st.sidebar.markdown("<h3 style='color:#dda0dd'>🧇 Gaufres Sucrées</h3>", unsafe_allow_html=True)
prix_gaufre = st.sidebar.number_input("Prix gaufre (MAD)", value=28)
cout_gaufre = st.sidebar.number_input("Coût gaufre (MAD)", value=9)
st.sidebar.write("")

# -- Pancakes --
st.sidebar.markdown("<h3 style='color:#ffb6c1'>🥞 Pancakes</h3>", unsafe_allow_html=True)
prix_pancake = st.sidebar.number_input("Prix pancake (MAD)", value=32)
cout_pancake = st.sidebar.number_input("Coût pancake (MAD)", value=11)
st.sidebar.write("")

# -- Coupes Glacées --
st.sidebar.markdown("<h3 style='color:#87cefa'>🍦 Coupes Glacées</h3>", unsafe_allow_html=True)
prix_glace = st.sidebar.number_input("Prix coupe glacée (MAD)", value=35)
cout_glace = st.sidebar.number_input("Coût coupe glacée (MAD)", value=12)
st.sidebar.write("")

# -- Salades & Bowls --
st.sidebar.markdown("<h3 style='color:#98fb98'>🍓 Salades & Bowls Fraîcheur</h3>", unsafe_allow_html=True)
prix_bowl = st.sidebar.number_input("Prix bowl/salade (MAD)", value=30)
cout_bowl = st.sidebar.number_input("Coût bowl/salade (MAD)", value=10)
st.sidebar.write("")

# -- Smoothies & Jus --
st.sidebar.markdown("<h3 style='color:#ffa07a'>🥤 Smoothies & Jus Frais</h3>", unsafe_allow_html=True)
prix_jus = st.sidebar.number_input("Prix jus/smoothie (MAD)", value=20)
cout_jus = st.sidebar.number_input("Coût jus/smoothie (MAD)", value=7)
st.sidebar.write("")

# -- Boissons Chaudes --
st.sidebar.markdown("<h3 style='color:#d2b48c'>☕ Boissons Chaudes</h3>", unsafe_allow_html=True)
prix_boisson = st.sidebar.number_input("Prix boisson chaude (MAD)", value=15)
cout_boisson = st.sidebar.number_input("Coût boisson chaude (MAD)", value=5)
st.sidebar.write("")

# === Commandes journalières min/max ===
st.sidebar.header("⚙️ Commandes Journalières")
st.sidebar.markdown("Définissez la fourchette de commandes par jour")
crepe_min = st.sidebar.number_input("Crêpes MIN / jour", value=80)
crepe_max = st.sidebar.number_input("Crêpes MAX / jour", value=120)
gaufre_min = st.sidebar.number_input("Gaufres MIN / jour", value=60)
gaufre_max = st.sidebar.number_input("Gaufres MAX / jour", value=100)
pancake_min = st.sidebar.number_input("Pancakes MIN / jour", value=50)
pancake_max = st.sidebar.number_input("Pancakes MAX / jour", value=70)
glace_min = st.sidebar.number_input("Coupes glacées MIN / jour", value=40)
glace_max = st.sidebar.number_input("Coupes glacées MAX / jour", value=60)
bowl_min = st.sidebar.number_input("Bowls MIN / jour", value=30)
bowl_max = st.sidebar.number_input("Bowls MAX / jour", value=50)
jus_min = st.sidebar.number_input("Jus MIN / jour", value=50)
jus_max = st.sidebar.number_input("Jus MAX / jour", value=90)
boisson_min = st.sidebar.number_input("Boissons chaudes MIN / jour", value=70)
boisson_max = st.sidebar.number_input("Boissons chaudes MAX / jour", value=110)

# === Charges mensuelles min/max ===
st.sidebar.header("💸 Charges Mensuelles")
st.sidebar.markdown("Définissez la fourchette de chaque charge")
loyer_min = st.sidebar.number_input("Loyer MIN (MAD)", value=6300)
loyer_max = st.sidebar.number_input("Loyer MAX (MAD)", value=7700)
sal_employes_min = st.sidebar.number_input("Salaires employés MIN", value=5400)
sal_employes_max = st.sidebar.number_input("Salaires employés MAX", value=6600)
sal_menage_min = st.sidebar.number_input("Ménage MIN", value=900)
sal_menage_max = st.sidebar.number_input("Ménage MAX", value=1100)
elec_min = st.sidebar.number_input("Électricité MIN", value=3600)
elec_max = st.sidebar.number_input("Électricité MAX", value=4400)
int_min = st.sidebar.number_input("Internet MIN", value=270)
int_max = st.sidebar.number_input("Internet MAX", value=330)
pub_min = st.sidebar.number_input("Pub MIN", value=1800)
pub_max = st.sidebar.number_input("Pub MAX", value=2200)
div_min = st.sidebar.number_input("Divers MIN", value=900)
div_max = st.sidebar.number_input("Divers MAX", value=1100)

# === Autres paramètres ===
jours_mois = st.sidebar.slider("Jours d’activité/mois", 20, 31, 30)
associes = st.sidebar.number_input("Nombre d’associés", value=6)
impot_taux = st.sidebar.slider("Taux d’impôt (%)", 0, 50, 20) / 100

st.sidebar.header("🏗️ Charges d'Investissement")
st.sidebar.markdown("Saisissez la fourchette pour chaque poste d'investissement")

# Équipements
crepier_inv_min = st.sidebar.number_input("Crépier MIN (MAD)", value=6000)
crepier_inv_max = st.sidebar.number_input("Crépier MAX (MAD)", value=8000)
gauffre_inv_min = st.sidebar.number_input("Gauffrier MIN (MAD)", value=3000)
gauffre_inv_max = st.sidebar.number_input("Gauffrier MAX (MAD)", value=4500)
plaque_inv_min = st.sidebar.number_input("Plaque & Pancakes MIN (MAD)", value=500)
plaque_inv_max = st.sidebar.number_input("Plaque & Pancakes MAX (MAD)", value=800)
blender_inv_min = st.sidebar.number_input("Blender MIN (MAD)", value=1000)
blender_inv_max = st.sidebar.number_input("Blender MAX (MAD)", value=2000)
extracteur_inv_min = st.sidebar.number_input("Extracteur de jus MIN (MAD)", value=1500)
extracteur_inv_max = st.sidebar.number_input("Extracteur de jus MAX (MAD)", value=3000)
cafe_inv_min = st.sidebar.number_input("Machine à café MIN (MAD)", value=30000)
cafe_inv_max = st.sidebar.number_input("Machine à café MAX (MAD)", value=30000)
vitrine_inv_min = st.sidebar.number_input("Vitrine 2 glaces MIN (MAD)", value=15000)
vitrine_inv_max = st.sidebar.number_input("Vitrine 2 glaces MAX (MAD)", value=20000)
frigo_inv_min = st.sidebar.number_input("Réfrigérateur MIN (MAD)", value=5000)
frigo_inv_max = st.sidebar.number_input("Réfrigérateur MAX (MAD)", value=5000)
congel_inv_min = st.sidebar.number_input("Congélateur MIN (MAD)", value=3000)
congel_inv_max = st.sidebar.number_input("Congélateur MAX (MAD)", value=3000)
presse_inv_min = st.sidebar.number_input("Presse agrume MIN (MAD)", value=1000)
presse_inv_max = st.sidebar.number_input("Presse agrume MAX (MAD)", value=2500)
ustensiles_inv_min = st.sidebar.number_input("Ustensiles MIN (MAD)", value=4000)
ustensiles_inv_max = st.sidebar.number_input("Ustensiles MAX (MAD)", value=4000)
produits_inv_min = st.sidebar.number_input("Produits initiaux MIN (MAD)", value=20000)
produits_inv_max = st.sidebar.number_input("Produits initiaux MAX (MAD)", value=20000)

# Aménagement / Design Intérieur
peinture_inv_min = st.sidebar.number_input("Peinture & Travaux MIN (MAD)", value=10000)
peinture_inv_max = st.sidebar.number_input("Peinture & Travaux MAX (MAD)", value=10000)
deco_inv_min = st.sidebar.number_input("Décoration & Lumières MIN (MAD)", value=20000)
deco_inv_max = st.sidebar.number_input("Décoration & Lumières MAX (MAD)", value=20000)
etageres_inv_min = st.sidebar.number_input("Étagères MIN (MAD)", value=3500)
etageres_inv_max = st.sidebar.number_input("Étagères MAX (MAD)", value=3500)
comptoir_inv_min = st.sidebar.number_input("Comptoir MIN (MAD)", value=5000)
comptoir_inv_max = st.sidebar.number_input("Comptoir MAX (MAD)", value=5000)
tables_inv_min = st.sidebar.number_input("Tables + Chaises MIN (MAD)", value=2500)
tables_inv_max = st.sidebar.number_input("Tables + Chaises MAX (MAD)", value=2500)
panneaux_inv_min = st.sidebar.number_input("Panneaux extérieur MIN (MAD)", value=10000)
panneaux_inv_max = st.sidebar.number_input("Panneaux extérieur MAX (MAD)", value=10000)
tv_inv_min = st.sidebar.number_input("TV + Caisse MIN (MAD)", value=10000)
tv_inv_max = st.sidebar.number_input("TV + Caisse MAX (MAD)", value=10000)
cameras_inv_min = st.sidebar.number_input("Caméras MIN (MAD)", value=3000)
cameras_inv_max = st.sidebar.number_input("Caméras MAX (MAD)", value=3000)

# Divers investissement
loyer2_inv_min = st.sidebar.number_input("Loyer 2 mois MIN (MAD)", value=18000)
loyer2_inv_max = st.sidebar.number_input("Loyer 2 mois MAX (MAD)", value=18000)
pubinv_min = st.sidebar.number_input("Publicités lancement MIN (MAD)", value=15000)
pubinv_max = st.sidebar.number_input("Publicités lancement MAX (MAD)", value=15000)

# Totaux investissement
equip_min = sum([crepier_inv_min, gauffre_inv_min, plaque_inv_min, blender_inv_min, extracteur_inv_min,
                  cafe_inv_min, vitrine_inv_min, frigo_inv_min, congel_inv_min,
                  presse_inv_min, ustensiles_inv_min, produits_inv_min])
equip_max = sum([crepier_inv_max, gauffre_inv_max, plaque_inv_max, blender_inv_max, extracteur_inv_max,
                  cafe_inv_max, vitrine_inv_max, frigo_inv_max, congel_inv_max,
                  presse_inv_max, ustensiles_inv_max, produits_inv_max])
amen_min = sum([peinture_inv_min, deco_inv_min, etageres_inv_min, comptoir_inv_min,
                 tables_inv_min, panneaux_inv_min, tv_inv_min, cameras_inv_min])
amen_max = sum([peinture_inv_max, deco_inv_max, etageres_inv_max, comptoir_inv_max,
                 tables_inv_max, panneaux_inv_max, tv_inv_max, cameras_inv_max])
div_inv_min = loyer2_inv_min + pubinv_min
div_inv_max = loyer2_inv_max + pubinv_max
total_inv_min = equip_min + amen_min + div_inv_min
total_inv_max = equip_max + amen_max + div_inv_max


# === Construction des dicts ===
commandes_min = {
    "crepe": crepe_min, "gaufre": gaufre_min, "pancake": pancake_min,
    "glace": glace_min, "bowl": bowl_min, "jus": jus_min, "boisson": boisson_min
}
commandes_max = {
    "crepe": crepe_max, "gaufre": gaufre_max, "pancake": pancake_max,
    "glace": glace_max, "bowl": bowl_max, "jus": jus_max, "boisson": boisson_max
}
charges_min = [loyer_min, sal_employes_min, sal_menage_min, elec_min, int_min, pub_min, div_min]
charges_max = [loyer_max, sal_employes_max, sal_menage_max, elec_max, int_max, pub_max, div_max]

# === Calculs min / max ===
# Revenus
revenu_min = sum(commandes_min[k] * v for k, v in [
    ("crepe", prix_crepe), ("gaufre", prix_gaufre), ("pancake", prix_pancake),
    ("glace", prix_glace), ("bowl", prix_bowl), ("jus", prix_jus),
    ("boisson", prix_boisson)
]) * jours_mois
revenu_max = sum(commandes_max[k] * v for k, v in [
    ("crepe", prix_crepe), ("gaufre", prix_gaufre), ("pancake", prix_pancake),
    ("glace", prix_glace), ("bowl", prix_bowl), ("jus", prix_jus),
    ("boisson", prix_boisson)
]) * jours_mois

# Coûts
cout_min = sum(commandes_min[k] * v for k, v in [
    ("crepe", cout_crepe), ("gaufre", cout_gaufre), ("pancake", cout_pancake),
    ("glace", cout_glace), ("bowl", cout_bowl), ("jus", cout_jus),
    ("boisson", cout_boisson)
]) * jours_mois
cout_max = sum(commandes_max[k] * v for k, v in [
    ("crepe", cout_crepe), ("gaufre", cout_gaufre), ("pancake", cout_pancake),
    ("glace", cout_glace), ("bowl", cout_bowl), ("jus", cout_jus),
    ("boisson", cout_boisson)
]) * jours_mois

# Charges mensuelles totales
ch_min = sum(charges_min)
ch_max = sum(charges_max)

# Bénéfice avant impôt
baimin = revenu_min - cout_max - ch_max
baimax = revenu_max - cout_min - ch_min

# Impôt
impot_min = max(0, baimin * impot_taux)
impot_max = max(0, baimax * impot_taux)

# Profit net
pn_min = baimin - impot_min
pn_max = baimax - impot_max

# Part par associé
pa_min = pn_min / associes
pa_max = pn_max / associes

# Moyennes
revenu_moy = (revenu_min + revenu_max) / 2
cout_moy = (cout_min + cout_max) / 2
ch_moy = (ch_min + ch_max) / 2
bai_moy = (baimin + baimax) / 2
impot_moy = (impot_min + impot_max) / 2
pn_moy = (pn_min + pn_max) / 2
pa_moy = (pa_min + pa_max) / 2

# === Affichage ===
st.subheader("📊 Résultats Mensuels")
df = pd.DataFrame([
    {"Metric": "Revenu Brut",      "Min": revenu_min,   "Max": revenu_max,   "Moyenne": revenu_moy},
    {"Metric": "Coût Total",       "Min": cout_min,     "Max": cout_max,     "Moyenne": cout_moy},
    {"Metric": "Charges Mensuelles","Min": ch_min,      "Max": ch_max,       "Moyenne": ch_moy},
    {"Metric": "Bénéf. Avant Impôt","Min": baimin,      "Max": baimax,       "Moyenne": bai_moy},
    {"Metric": "Impôt",            "Min": impot_min,    "Max": impot_max,    "Moyenne": impot_moy},
    {"Metric": "Profit Net",       "Min": pn_min,       "Max": pn_max,       "Moyenne": pn_moy},
    {"Metric": "Part/Assoc",       "Min": pa_min,       "Max": pa_max,       "Moyenne": pa_moy},
])
st.dataframe(df.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}", "Moyenne": "{:,.0f}"}))

st.subheader("📈 Graphique Comparatif")
fig, ax = plt.subplots(figsize=(10,4))
ax.bar(
    ["PN Min","PN Moy","PN Max"],
    [pn_min, pn_moy, pn_max],
    alpha=0.7
)
ax.set_ylabel("MAD")
ax.set_title("Profit Net\nPire cas / Moyenne / Meilleur cas")
ax.grid(axis="y", linestyle="--")
st.pyplot(fig)

st.subheader("💼 Charges d'Investissement")
df_inv = pd.DataFrame([
    {"Catégorie": "Équipements",                  "Min": equip_min,      "Max": equip_max,      "Moyenne": (equip_min+equip_max)/2},
    {"Catégorie": "Aménagement / Design Intérieur","Min": amen_min,       "Max": amen_max,       "Moyenne": (amen_min+amen_max)/2},
    {"Catégorie": "Divers",                       "Min": div_inv_min,    "Max": div_inv_max,    "Moyenne": (div_inv_min+div_inv_max)/2},
    {"Catégorie": "TOTAL",                        "Min": total_inv_min,  "Max": total_inv_max,  "Moyenne": (total_inv_min+total_inv_max)/2},
])
st.dataframe(df_inv.style.format({"Min": "{:,.0f}", "Max": "{:,.0f}", "Moyenne": "{:,.0f}"}))

# Graphique charges investissement
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.bar(
    ["Inv Min","Inv Moy","Inv Max"],
    [total_inv_min,(total_inv_min+total_inv_max)/2,total_inv_max],
    color=['#ffa07a','#20b2aa','#ffa07a']
)
ax2.set_ylabel("MAD")
ax2.set_title("Charges d'Investissement\nPire cas / Moyenne / Meilleur cas")
ax2.grid(axis="y", linestyle="--")
st.pyplot(fig2)
