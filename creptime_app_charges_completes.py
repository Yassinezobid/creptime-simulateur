import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Complet", layout="wide")
st.title("🥞 Simulateur de Rentabilité - Crêp'Time (Meknès)")

# === Produits : prix, coût ===
st.sidebar.header("🧾 Paramètres Produits & Marges")

# Crêpes
st.sidebar.markdown("### 🧁 Crêpes")
prix_crepe = st.sidebar.number_input("Prix crêpe (MAD)", value=30)
cout_crepe = st.sidebar.number_input("Coût crêpe (MP)", value=10)

# Jus / Smoothies
st.sidebar.markdown("### 🍹 Jus / Smoothies")
prix_jus = st.sidebar.number_input("Prix jus (MAD)", value=20)
cout_jus = st.sidebar.number_input("Coût jus (MP)", value=7)

# Café
st.sidebar.markdown("### ☕ Café")
prix_cafe = st.sidebar.number_input("Prix café (MAD)", value=12)
cout_cafe = st.sidebar.number_input("Coût café (MP)", value=3)

# === Paramètres de gestion ===
st.sidebar.header("⚙️ Commandes journalières")
commandes_crepe_min = st.sidebar.number_input("Commandes crêpe (min)", value=0)
commandes_crepe_max = st.sidebar.number_input("Commandes crêpe (max)", value=200)
commandes_crepe_pas = st.sidebar.number_input("Pas crêpe", value=20)

commandes_jus_min = st.sidebar.number_input("Commandes jus (min)", value=0)
commandes_jus_max = st.sidebar.number_input("Commandes jus (max)", value=150)
commandes_jus_pas = st.sidebar.number_input("Pas jus", value=15)

commandes_cafe_min = st.sidebar.number_input("Commandes café (min)", value=0)
commandes_cafe_max = st.sidebar.number_input("Commandes café (max)", value=150)
commandes_cafe_pas = st.sidebar.number_input("Pas café", value=15)

jours_mois = st.sidebar.slider("Jours d'activité par mois", 20, 31, 30)
associes = st.sidebar.number_input("Nombre d'associés", value=6)
impot_taux = st.sidebar.slider("Taux impôt (%)", 0, 50, 20) / 100

# === Charges fixes ===
st.sidebar.header("🏗️ Charges Fixes")
local = st.sidebar.number_input("Droit au local", value=100000)
travaux = st.sidebar.number_input("Travaux / déco", value=25000)
materiel = st.sidebar.number_input("Matériel cuisine", value=50000)
mobilier = st.sidebar.number_input("Mobilier", value=20000)
ambiance = st.sidebar.number_input("Ambiance / TV / déco", value=15000)
stock = st.sidebar.number_input("Stock initial", value=10000)
divers_fixes = st.sidebar.number_input("Divers (fixe)", value=10000)

charges_fixes_totales = sum([local, travaux, materiel, mobilier, ambiance, stock, divers_fixes])
part_fixe_associe = charges_fixes_totales / associes

# === Charges mensuelles ===
st.sidebar.header("📆 Charges Mensuelles")
loyer = st.sidebar.number_input("Loyer", value=4000)
salaire_employes = st.sidebar.number_input("Salaires employés (2)", value=4000)
salaire_menage = st.sidebar.number_input("Femme de ménage", value=1000)
electricite = st.sidebar.number_input("Électricité", value=1500)
internet = st.sidebar.number_input("Internet", value=500)
publicite = st.sidebar.number_input("Publicité / Réseaux", value=500)
divers_mensuels = st.sidebar.number_input("Divers mensuels", value=1000)

charges_mensuelles = sum([
    loyer, salaire_employes, salaire_menage,
    electricite, internet, publicite, divers_mensuels
])
part_mensuelle_associe = charges_mensuelles / associes

# === Simulation ===
data = []
for nb_crepe in range(commandes_crepe_min, commandes_crepe_max + 1, commandes_crepe_pas):
    for nb_jus in range(commandes_jus_min, commandes_jus_max + 1, commandes_jus_pas):
        for nb_cafe in range(commandes_cafe_min, commandes_cafe_max + 1, commandes_cafe_pas):
            revenu_brut = (
                nb_crepe * prix_crepe +
                nb_jus * prix_jus +
                nb_cafe * prix_cafe
            ) * jours_mois
            cout_total = (
                nb_crepe * cout_crepe +
                nb_jus * cout_jus +
                nb_cafe * cout_cafe
            ) * jours_mois
            benefice_avant_impot = revenu_brut - cout_total - charges_mensuelles
            impot = max(0, benefice_avant_impot * impot_taux)
            profit_net = benefice_avant_impot - impot
            part_associe = profit_net / associes
            data.append([
                nb_crepe, nb_jus, nb_cafe,
                revenu_brut, cout_total, benefice_avant_impot,
                impot, profit_net, part_associe
            ])

df = pd.DataFrame(data, columns=[
    "Cmd Crêpes", "Cmd Jus", "Cmd Café",
    "Revenu Brut", "Coût MP", "Bénéfice Avant Impôt",
    "Impôt", "Profit Net", "Part par Associé"
])

# === Affichage résultats ===
st.subheader("📊 Résultats de Simulation")
st.dataframe(df.style.format("{:,.0f}"))

st.subheader("📈 Graphique : Profit Net & Part Associé")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df["Profit Net"], label="Profit Net", color="orange")
ax.plot(df["Part par Associé"], label="Part par Associé", color="green", linestyle="--")
ax.set_title("Profit Net mensuel selon les commandes")
ax.set_xlabel("Combinaisons de commandes")
ax.set_ylabel("MAD")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# === Résumé des Charges ===
st.subheader("💼 Charges Fixes")
df_fixes = pd.DataFrame({
    "Poste": ["Local", "Travaux", "Cuisine", "Mobilier", "Ambiance", "Stock", "Divers"],
    "Montant": [local, travaux, materiel, mobilier, ambiance, stock, divers_fixes]
})
df_fixes.loc["Total"] = ["TOTAL", charges_fixes_totales]
st.dataframe(df_fixes)

st.markdown(f"💰 **Part Fixe Associé : {part_fixe_associe:,.0f} MAD**")

st.subheader("📅 Charges Mensuelles")
df_mensuelles = pd.DataFrame({
    "Poste": ["Loyer", "Salaires", "Ménage", "Électricité", "Internet", "Publicité", "Divers"],
    "Montant": [loyer, salaire_employes, salaire_menage, electricite, internet, publicite, divers_mensuels]
})
df_mensuelles.loc["Total"] = ["TOTAL", charges_mensuelles]
st.dataframe(df_mensuelles)

st.markdown(f"💸 **Part Mensuelle Associé : {part_mensuelle_associe:,.0f} MAD**")
