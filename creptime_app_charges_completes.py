
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crêp'Time - Simulateur Complet", layout="wide")
st.title("📊 Simulateur de Rentabilité - Crêp'Time (Meknès)")

# --- Paramètres de base ---
st.sidebar.header("🔧 Paramètres modifiables")

panier_moyen = st.sidebar.number_input("💸 Panier moyen par client (MAD)", value=30)
jours_mois = st.sidebar.slider("📅 Jours d'activité par mois", 20, 31, 30)
associes = st.sidebar.number_input("👥 Nombre d'associés", value=6, step=1)
impot_taux = st.sidebar.slider("💼 Taux d'imposition (%)", 0, 50, 20) / 100

# --- Charges Fixes (Investissement unique) ---
st.sidebar.markdown("### 🧱 Charges Fixes (Investissement Initial)")
loyer_initial = st.sidebar.number_input("🔑 Droit d'entrée / Local", value=100000)
travaux = st.sidebar.number_input("🎨 Travaux / peinture / déco", value=25000)
materiel_cuisine = st.sidebar.number_input("🍳 Matériel de cuisine", value=50000)
mobilier = st.sidebar.number_input("🪑 Mobilier", value=20000)
ambiance = st.sidebar.number_input("📺 TV / ambiance / déco", value=15000)
stock_initial = st.sidebar.number_input("📦 Stock de départ", value=10000)
divers_fixes = st.sidebar.number_input("📁 Divers / imprévus", value=10000)

total_fixes = sum([loyer_initial, travaux, materiel_cuisine, mobilier, ambiance, stock_initial, divers_fixes])
part_fixe_par_associe = total_fixes / associes

# --- Charges Mensuelles ---
st.sidebar.markdown("### 📆 Charges Mensuelles")
loyer_mensuel = st.sidebar.number_input("🏠 Loyer mensuel", value=4000)
employes = st.sidebar.number_input("👨‍🍳 Salaires employés", value=4000)
femme_menage = st.sidebar.number_input("🧹 Femme de ménage", value=1000)
electricite = st.sidebar.number_input("💡 Électricité & eau", value=1500)
internet = st.sidebar.number_input("🌐 Internet", value=500)
publicite = st.sidebar.number_input("📢 Publicité / Réseaux", value=500)
forfait_6g = st.sidebar.number_input("📱 Forfait 6G + Réseaux", value=500)
divers_mensuels = st.sidebar.number_input("📦 Autres charges mensuelles", value=1000)

total_mensuelles = sum([
    loyer_mensuel, employes, femme_menage,
    electricite, internet, publicite, forfait_6g, divers_mensuels
])
part_mensuelle_par_associe = total_mensuelles / associes

# --- Simulation dynamique ---
st.sidebar.markdown("### 👥 Simulation Clients")
clients_min = st.sidebar.slider("Clients/jour (minimum)", 5, 50, 25)
clients_max = st.sidebar.slider("Clients/jour (maximum)", 50, 100, 80)
pas = st.sidebar.slider("Pas de variation (clients)", 1, 10, 5)

clients_range = list(range(clients_min, clients_max + 1, pas))
data = []

for clients in clients_range:
    revenu_brut = clients * panier_moyen * jours_mois
    benefice_avant_impot = revenu_brut - total_mensuelles
    impot = max(0, benefice_avant_impot * impot_taux)
    profit_net = benefice_avant_impot - impot
    part_associe = profit_net / associes
    data.append([
        clients, revenu_brut, benefice_avant_impot, impot, profit_net, part_associe
    ])

df = pd.DataFrame(data, columns=[
    "Clients/Jour", "Revenu Brut (MAD)", "Bénéfice Avant Impôt",
    "Impôt (MAD)", "Profit Net (MAD)", "Part par Associé (MAD)"
])

# --- Affichage principal ---
st.subheader("📊 Tableau de Rentabilité")
st.dataframe(df.style.format("{:,.0f}"))

# --- Graphiques ---
st.subheader("📈 Visualisation des Profits")

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df["Clients/Jour"], df["Profit Net (MAD)"], color='skyblue', label='Profit Net')
ax.plot(df["Clients/Jour"], df["Part par Associé (MAD)"], marker='o', color='green', label='Part Associé')
for seuil in [20, 25, 30]:
    ax.axvline(x=seuil, color='red' if seuil == 25 else 'gray', linestyle='--', label=f"Seuil {seuil} clients/jour")
ax.set_title("Évolution du Profit Net & Part Associé selon la Fréquentation")
ax.set_xlabel("Clients par jour")
ax.set_ylabel("MAD")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# --- Affichage Charges Fixes & Mensuelles ---
st.subheader("📦 Détail des Charges Initiales (Fixes)")
charges_fixes_df = pd.DataFrame({
    "Poste": ["Droit local", "Travaux", "Cuisine", "Mobilier", "Ambiance", "Stock", "Divers"],
    "Montant (MAD)": [loyer_initial, travaux, materiel_cuisine, mobilier, ambiance, stock_initial, divers_fixes]
})
charges_fixes_df.loc["Total"] = ["TOTAL", total_fixes]
st.dataframe(charges_fixes_df)

st.markdown(f"💰 **Part individuelle sur les charges fixes : {part_fixe_par_associe:,.0f} MAD**")

st.subheader("📅 Détail des Charges Mensuelles")
charges_mensuelles_df = pd.DataFrame({
    "Poste": ["Loyer", "Salaires", "Femme de ménage", "Électricité", "Internet", "Publicité", "Forfait 6G", "Divers"],
    "Montant (MAD)": [
        loyer_mensuel, employes, femme_menage,
        electricite, internet, publicite, forfait_6g, divers_mensuels
    ]
})
charges_mensuelles_df.loc["Total"] = ["TOTAL", total_mensuelles]
st.dataframe(charges_mensuelles_df)

st.markdown(f"💡 **Part individuelle mensuelle : {part_mensuelle_par_associe:,.0f} MAD**")
