import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Complet", layout="wide")
st.title("🥞 Simulateur de Rentabilité - Crêp'Time (Meknès)")

# === Produits : prix, coût, consommation ===
st.sidebar.header("🧾 Paramètres Produits & Marges")

# Crêpes
st.sidebar.markdown("### 🧁 Crêpes")
prix_crepe = st.sidebar.number_input("Prix crêpe (MAD)", value=30)
cout_crepe = st.sidebar.number_input("Coût crêpe (MP)", value=10)
conso_crepe = st.sidebar.number_input("Consommation crêpe / client", value=1.0)

# Jus / Smoothies
st.sidebar.markdown("### 🍹 Jus / Smoothies")
prix_jus = st.sidebar.number_input("Prix jus (MAD)", value=20)
cout_jus = st.sidebar.number_input("Coût jus (MP)", value=7)
conso_jus = st.sidebar.number_input("Consommation jus / client", value=0.5)

# Café
st.sidebar.markdown("### ☕ Café")
prix_cafe = st.sidebar.number_input("Prix café (MAD)", value=12)
cout_cafe = st.sidebar.number_input("Coût café (MP)", value=3)
conso_cafe = st.sidebar.number_input("Consommation café / client", value=0.5)

# Glace
st.sidebar.markdown("### 🍨 Glace")
prix_glace = st.sidebar.number_input("Prix glace (MAD)", value=15)
cout_glace = st.sidebar.number_input("Coût glace (MP)", value=5)
conso_glace = st.sidebar.number_input("Consommation glace / client", value=0.3)

# Calcul marge nette/client
marge_crepe = prix_crepe - cout_crepe
marge_jus = prix_jus - cout_jus
marge_cafe = prix_cafe - cout_cafe
marge_glace = prix_glace - cout_glace
panier_moyen = (
    marge_crepe * conso_crepe +
    marge_jus * conso_jus +
    marge_cafe * conso_cafe +
    marge_glace * conso_glace
)

# === Paramètres de gestion ===
st.sidebar.header("⚙️ Paramètres de gestion")
commandes_crepe_min = st.sidebar.slider("Commandes crêpe (min)", 0, 300, 50)
commandes_crepe_max = st.sidebar.slider("Commandes crêpe (max)", 0, 300, 150)
commandes_crepe_pas = st.sidebar.slider("Pas commandes crêpe", 1, 50, 25)

commandes_jus_min = st.sidebar.slider("Commandes jus (min)", 0, 300, 30)
commandes_jus_max = st.sidebar.slider("Commandes jus (max)", 0, 300, 100)
commandes_jus_pas = st.sidebar.slider("Pas commandes jus", 1, 50, 25)

commandes_cafe_min = st.sidebar.slider("Commandes café (min)", 0, 300, 20)
commandes_cafe_max = st.sidebar.slider("Commandes café (max)", 0, 300, 100)
commandes_cafe_pas = st.sidebar.slider("Pas commandes café", 1, 50, 25)

jours_mois = st.sidebar.slider("Jours d'activité par mois", 20, 31, 30)
associes = st.sidebar.number_input("Nombre d'associés", value=6)
impot_taux = st.sidebar.slider("Taux impôt (%)", 0, 50, 20) / 100

# === Charges fixes détaillées ===
st.sidebar.header("🏗️ Charges Fixes (Investissement)")
local = st.sidebar.number_input("Droit au local", value=100000)
travaux = st.sidebar.number_input("Travaux / déco", value=25000)
materiel = st.sidebar.number_input("Matériel cuisine", value=50000)
mobilier = st.sidebar.number_input("Mobilier", value=20000)
ambiance = st.sidebar.number_input("Ambiance / TV / déco", value=15000)
stock = st.sidebar.number_input("Stock initial", value=10000)
divers_fixes = st.sidebar.number_input("Divers (fixe)", value=10000)

charges_fixes_totales = sum([local, travaux, materiel, mobilier, ambiance, stock, divers_fixes])
part_fixe_associe = charges_fixes_totales / associes

# === Charges mensuelles détaillées ===
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

# === Affichage ===
st.subheader("📊 Résultats de Simulation")
st.dataframe(df.style.format("{:,.0f}"))

st.subheader("📈 Graphique : Profit Net & Part Associé")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df.index, df["Profit Net"], color='orange', label="Profit Net")
ax.plot(df.index, df["Part par Associé"], marker='o', color='green', label="Part par Associé")
ax.set_title("Profit Net mensuel selon les commandes")
ax.set_xlabel("Variations de commandes")
ax.set_ylabel("MAD")
ax.grid(True)
ax.legend()
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
