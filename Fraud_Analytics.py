import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# New custom color palette
custom_palette = ["#ecd5bb", "#D0E6F0", "#710117"]

# Load dataset
file_path = "C:/Users/aryan/OneDrive/Desktop/DA Projects/AIML/Fraud Analytics Dataset - npci_data.csv"
df = pd.read_csv(file_path)

# Convert the 'dt_txn_comp' to datetime
df['dt_txn_comp'] = pd.to_datetime(df['dt_txn_comp'])
df['month'] = df['dt_txn_comp'].dt.month

# Set the seaborn style for consistent styling
sns.set(style="whitegrid", rc={"figure.figsize": (12, 6)})

# Chart 1: Monthly Fluctuation of Fraud Incidents
fraud_counts = df.groupby('month').size().reset_index(name='fraud_count')

plt.figure(figsize=(14, 7))
sns.lineplot(x="month", y="fraud_count", data=fraud_counts, marker='o', linewidth=2.5, color=custom_palette[2])
plt.title("Monthly Fluctuation of Fraud Incidents", fontsize=16, color=custom_palette[2])
plt.xlabel('Month', fontsize=14, color=custom_palette[2])
plt.ylabel('Number of Fraud Incidents', fontsize=14, color=custom_palette[2])
plt.xticks(range(1, 13), fontsize=12, color=custom_palette[2])
plt.yticks(fontsize=12, color=custom_palette[2])
plt.grid(True, linestyle='--', color=custom_palette[0])
plt.show()

# Chart 2: Total Amount of Fraudulent Transactions by Credit Type
fraud_amount_by_credit_type = df.groupby('cred_type')['payee_settlement_amount'].sum().reset_index()

plt.figure(figsize=(14, 7))
sns.barplot(x='cred_type', y='payee_settlement_amount', data=fraud_amount_by_credit_type, palette=custom_palette)
plt.title("Total Amount of Fraudulent Transactions by Credit Type", fontsize=16, color=custom_palette[2])
plt.xlabel('Credit Type', fontsize=14, color=custom_palette[2])
plt.ylabel('Total Amount', fontsize=14, color=custom_palette[2])
plt.xticks(rotation=45, fontsize=12, color=custom_palette[2])
plt.yticks(fontsize=12, color=custom_palette[2])
plt.grid(True, linestyle='--', color=custom_palette[0])
plt.show()

# Chart 3: Top 10 Payer States by Fraud Transaction Amount
top_payer_states_amount = df.groupby('payer_state')['payee_settlement_amount'].sum().nlargest(10).reset_index()

plt.figure(figsize=(14, 7))
sns.barplot(x='payee_settlement_amount', y='payer_state', data=top_payer_states_amount, orient='h', palette=custom_palette)
plt.title('Top 10 Payer States by Fraud Transaction Amount', fontsize=16, color=custom_palette[2])
plt.xlabel('Total Fraud Amount', fontsize=14, color=custom_palette[2])
plt.ylabel('Payer State', fontsize=14, color=custom_palette[2])
plt.grid(True, linestyle='--', color=custom_palette[0])
plt.show()

# Chart 4: Fraud Transaction Amount by Payer State
fraud_amount_per_payer_state = df.groupby('payer_state')['payee_settlement_amount'].sum().nlargest(10).reset_index()
fraud_amount_per_payer_state = fraud_amount_per_payer_state.sort_values(by='payee_settlement_amount', ascending=False)

plt.figure(figsize=(14, 7))
sns.barplot(x='payer_state', y='payee_settlement_amount', data=fraud_amount_per_payer_state, palette=custom_palette)
plt.title('Fraud Transaction Amount by Payer State', fontsize=16, color=custom_palette[2])
plt.xlabel('Payer State', fontsize=14, color=custom_palette[2])
plt.ylabel('Total Fraud Amount', fontsize=14, color=custom_palette[2])
plt.xticks(rotation=90, fontsize=12, color=custom_palette[2])
plt.yticks(fontsize=12, color=custom_palette[2])
plt.grid(True, linestyle='--', color=custom_palette[0])
plt.show()

# Chart 5: Distribution of Fraud Transaction Amounts by Time of Day
fraud_amount_by_time = df.groupby('time_of_day')['payee_settlement_amount'].sum().reset_index()

plt.figure(figsize=(10, 10))
plt.pie(fraud_amount_by_time['payee_settlement_amount'], labels=fraud_amount_by_time['time_of_day'], 
        autopct='%1.1f%%', startangle=140, colors=custom_palette)
plt.title('Distribution of Fraud Transaction Amounts by Time of Day', fontsize=16, color=custom_palette[2])
plt.show()
