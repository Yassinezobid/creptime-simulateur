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

# === Charges fixes ===
st.sidebar.header("🏗️ Charges d'Investissement")

st.sidebar.markdown("### 🛠️ Équipements")
equipements = {
    "Crépier": st.sidebar.slider("Crépier (MAD)", 6000, 8000, 7000),
    "Gauffrier": st.sidebar.slider("Gauffrier (MAD)", 3000, 4500, 3750),
    "Plaque & Pancakes": st.sidebar.slider("Plaque & Pancakes (MAD)", 500, 800, 650),
    "Blender": st.sidebar.slider("Blender (MAD)", 1000, 2000, 1500),
    "Extracteur de jus": st.sidebar.slider("Extracteur de jus (MAD)", 1500, 3000, 2250),
    "Machine à café": st.sidebar.slider("Machine à café (MAD)", 30000, 30000, 30000),
    "Vitrine 2 glaces": st.sidebar.slider("Vitrine 2 glaces (MAD)", 15000, 20000, 17500),
    "Réfrigérateur": st.sidebar.slider("Réfrigérateur (MAD)", 5000, 5000, 5000),
    "Congélateur": st.sidebar.slider("Congélateur (MAD)", 3000, 3000, 3000),
    "Presse agrume": st.sidebar.slider("Presse agrume (MAD)", 1000, 2500, 1750),
    "Ustensiles": st.sidebar.slider("Ustensiles (MAD)", 4000, 4000, 4000),
    "Produits initiaux": st.sidebar.slider("Produits initiaux (MAD)", 20000, 20000, 20000)
}

st.sidebar.markdown("### 🧱 Aménagement / Design Intérieur")
amenagement = {
    "Peinture & Travaux": st.sidebar.slider("Peinture & Travaux (MAD)", 10000, 10000, 10000),
    "Décoration & Lumières": st.sidebar.slider("Décoration & Lumières (MAD)", 20000, 20000, 20000),
    "Étagères": st.sidebar.slider("Étagères (MAD)", 3500, 3500, 3500),
    "Comptoir": st.sidebar.slider("Comptoir (MAD)", 5000, 5000, 5000),
    "Tables + Chaises": st.sidebar.slider("Tables + Chaises (MAD)", 2500, 2500, 2500),
    "Panneaux (extérieur)": st.sidebar.slider("Panneaux (extérieur) (MAD)", 10000, 10000, 10000),
    "TV + Caisse": st.sidebar.slider("TV + Caisse (MAD)", 10000, 10000, 10000),
    "Caméras": st.sidebar.slider("Caméras (MAD)", 3000, 3000, 3000)
}

st.sidebar.markdown("### 📦 Divers")
divers = {
    "Loyer 2 mois": st.sidebar.slider("Loyer 2 mois (MAD)", 18000, 18000, 18000),
    "Publicités de lancement": st.sidebar.slider("Publicités de lancement (MAD)", 15000, 15000, 15000)
}

charges_fixes_totales = sum(equipements.values()) + sum(amenagement.values()) + sum(divers.values())
part_fixe_associe = charges_fixes_totales / associes

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
revenu_brut = (
    commandes["crepe"] * prix_crepe +
    commandes["gaufre"] * prix_gaufre +
    commandes["pancake"] * prix_pancake +
    commandes["glace"] * prix_glace +
    commandes["bowl"] * prix_bowl +
    commandes["jus"] * prix_jus +
    commandes["boisson"] * prix_boisson_chaude
) * jours_mois

cout_total = (
    commandes["crepe"] * cout_crepe +
    commandes["gaufre"] * cout_gaufre +
    commandes["pancake"] * cout_pancake +
    commandes["glace"] * cout_glace +
    commandes["bowl"] * cout_bowl +
    commandes["jus"] * cout_jus +
    commandes["boisson"] * cout_boisson_chaude
) * jours_mois

benefice_avant_impot = revenu_brut - cout_total - charges_mensuelles
impot = max(0, benefice_avant_impot * impot_taux)
profit_net = benefice_avant_impot - impot
part_associe = profit_net / associes

# === Affichage résultats ===
st.subheader("📊 Résultats de Simulation")
df = pd.DataFrame([{
    "Revenu Brut": revenu_brut,
    "Coût MP": cout_total,
    "Bénéfice Avant Impôt": benefice_avant_impot,
    "Impôt": impot,
    "Profit Net": profit_net,
    "Part par Associé": part_associe
}])
st.dataframe(df.style.format("{:,.0f}"))

st.subheader("📈 Graphique : Profit Net & Part Associé")
fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(["Profit Net", "Part par Associé"], [profit_net, part_associe])
ax.set_ylabel("MAD")
ax.set_title("Profit Net mensuel & Part Associé")
ax.grid(True)
st.pyplot(fig)

st.subheader("💼 Charges d’Investissement")
df_fixes = pd.DataFrame([
    ["Crépier", equipements["Crépier"]],
    ["Gauffrier", equipements["Gauffrier"]],
    ["Plaque & Pancakes", equipements["Plaque & Pancakes"]],
    ["Blender", equipements["Blender"]],
    ["Extracteur de jus", equipements["Extracteur de jus"]],
    ["Machine à café", equipements["Machine à café"]],
    ["Vitrine 2 glaces", equipements["Vitrine 2 glaces"]],
    ["Réfrigérateur", equipements["Réfrigérateur"]],
    ["Congélateur", equipements["Congélateur"]],
    ["Presse agrume", equipements["Presse agrume"]],
    ["Ustensiles", equipements["Ustensiles"]],
    ["Produits initiaux", equipements["Produits initiaux"]],
    ["Peinture & Travaux", amenagement["Peinture & Travaux"]],
    ["Décoration & Lumières", amenagement["Décoration & Lumières"]],
    ["Étagères", amenagement["Étagères"]],
    ["Comptoir", amenagement["Comptoir"]],
    ["Tables + Chaises", amenagement["Tables + Chaises"]],
    ["Panneaux (extérieur)", amenagement["Panneaux (extérieur)"]],
    ["TV + Caisse", amenagement["TV + Caisse"]],
    ["Caméras", amenagement["Caméras"]],
    ["Loyer 2 mois", divers["Loyer 2 mois"]],
    ["Publicités de lancement", divers["Publicités de lancement"]],
    ["TOTAL", charges_fixes_totales]
], columns=["Poste", "Montant"])
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
