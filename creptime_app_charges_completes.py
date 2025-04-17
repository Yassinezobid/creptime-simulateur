import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Mensuel", layout="wide")
st.title("🥞 Simulateur de Profit Net Mensuel")

# === Paramètres Produits ===
st.sidebar.header("💾 Paramètres Produits")
prix_crepe = st.sidebar.number_input("Prix crêpe (MAD)", value=30)
cout_crepe = st.sidebar.number_input("Coût crêpe (MAD)", value=10)
prix_gaufre = st.sidebar.number_input("Prix gaufre (MAD)", value=28)
cout_gaufre = st.sidebar.number_input("Coût gaufre (MAD)", value=9)
prix_pancake = st.sidebar.number_input("Prix pancake (MAD)", value=32)
cout_pancake = st.sidebar.number_input("Coût pancake (MAD)", value=11)
prix_glace = st.sidebar.number_input("Prix coupe glacée (MAD)", value=35)
cout_glace = st.sidebar.number_input("Coût coupe glacée (MAD)", value=12)
prix_bowl = st.sidebar.number_input("Prix bowl/salade (MAD)", value=30)
cout_bowl = st.sidebar.number_input("Coût bowl/salade (MAD)", value=10)
prix_jus = st.sidebar.number_input("Prix jus/smoothie (MAD)", value=20)
cout_jus = st.sidebar.number_input("Coût jus/smoothie (MAD)", value=7)
prix_boisson = st.sidebar.number_input("Prix boisson chaude (MAD)", value=15)
cout_boisson = st.sidebar.number_input("Coût boisson chaude (MAD)", value=5)

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
