import streamlit as st
from data import data
import matplotlib.pyplot as plt
import seaborn as sns

st.title('EDA Process')
st.divider()

st.subheader("Data Distribution")

df = data.getDataFrame()

st.write(df.describe(include='all'))

st.markdown(
'''
The descriptive table above show severals important insight for each column:
- payment sequential (numerical discrete):
  - value range 1 - 29
  - mean = 1.09 and median = 1, this shows that the data distribution is `positive skewed`

- payment type (category nominal):
  - there are 5 categories and the most common one is `credit_card` by ~74.0%, this shows that payment type with credit outnumbered other categories
  
- payment installment (numerical discrete):
  - value range 0 - 24
  - mean = 2.85 and median = 1, this shows that the data distribution is `positive skewed` as well

- payment value (numerical continue):
  - value range 0 - ~13,664
  - mean = ~154 and median = 100, this shows the data distribution also `positive skewed`
'''
)

fig, axs = plt.subplots(3, 1, figsize=(10, 5))

axs[0].set(
    title='Payment Sequential Distribution',
    xlabel='Payment Sequential'
)

sns.boxplot(
    x=df['payment_sequential'],
    ax=axs[0]
)

axs[1].set(
    title='Payment Installment Distribution',
    xlabel='Payment Installment'
)

sns.boxplot(
    x=df['payment_installments'],
    ax=axs[1]
)

axs[2].set(
    title='Payment Value Distribution',
    xlabel='Payment Value'
)

sns.boxplot(
    x=df['payment_value'],
    ax=axs[2]
)

plt.tight_layout()

st.pyplot(fig)

st.markdown(
'''
> The boxplots above confirm that the data has positive skewness
'''
)

st.divider()

st.subheader('Data Correlation')
st.write(df.corr(numeric_only=True))