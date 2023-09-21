import streamlit as st
from data import data
import pandas as pd
from util import util
from babel.numbers import format_currency, format_number
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


df = data.getDataFrame(dataset_path='data/order_payments_dataset.csv')

st.title('Analysis Result')
st.divider()

st.subheader('Payment Type')

with st.container():
    payment_type_freq = df[['payment_type']].groupby('payment_type')\
                        .value_counts().to_frame(name='freq').sort_values(by=['freq'], ascending=False)

    col1, col2 = st.columns(2)

    with col1:
        
        st.metric(
            label='Most Used Payment Type',
            value=util.reformatIndexToStr(str(payment_type_freq.index[0]))
        )

    with col2:

        st.metric(
            label='Payment Frequency',
            value=format_number(
                payment_type_freq.sum()['freq'],
                locale='en_US'
            )
        )

    col_colors = ['grey' if(freq < max(payment_type_freq['freq'])) else 'orange' for freq in payment_type_freq['freq']]

    fig, ax = plt.subplots()

    ax = sns.barplot(
        data=payment_type_freq,
        x='freq',
        y=payment_type_freq.index,
        orient='h',
        palette=col_colors,
        ax=ax
    )

    ax.set(
        title='Frequency of Payment Type',
        xlabel='Frequency',
        ylabel='Payment Type'
    )

    ax.tick_params(axis='x', rotation=45)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

    st.pyplot(fig)



with st.container():
    col1, col2 = st.columns(2)

    payment_sum_by_type = df.groupby('payment_type').agg(
        payment_sum = pd.NamedAgg(column='payment_value',
                                aggfunc='sum')
    ).sort_values(by=['payment_sum'], ascending=False)

    with col1:
        
        st.metric(
            label='Most Used Payment Type',
            value=util.reformatIndexToStr(str(payment_sum_by_type.index[0]))
        )

    with col2:
        total_payment_str = format_currency(
            payment_sum_by_type.sum()['payment_sum'], 
            'USD', 
            locale='en_US'
        )

        st.metric(
            label='Total Payment',
            value=total_payment_str
        )

    col_colors = ['gray' if(sum < max(payment_sum_by_type['payment_sum'])) else 'orange' for sum in payment_sum_by_type['payment_sum']]

    fig, ax = plt.subplots()

    sns.barplot(
        data=payment_sum_by_type,
        x='payment_sum',
        y=payment_sum_by_type.index,
        palette=col_colors,
        ax=ax
    )

    ax.set(
        title='Total Payment by Payment Type',
        xlabel='Total Payment',
        ylabel='Payment Type'
    )

    ax.tick_params(axis='x', rotation=45)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

    st.pyplot(fig)

st.divider()

st.subheader('Payment Type Distribution')
with st.container():
    installment_and_value_by_type = df.loc[
        :, 
        ['payment_installments', 'payment_value', 'payment_type']
    ]

    fig, ax = plt.subplots()

    sns.scatterplot(
        data=installment_and_value_by_type,
        x='payment_installments',
        y='payment_value',
        hue='payment_type',
        ax=ax
    )

    ax.set(
        title='Distribution of Payment Type on Payment Value vs Payment Installment',
        xlabel='Payment Installment',
        ylabel='Payment Value'
    )

    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

    st.pyplot(fig)

    st.markdown(
    '''
        The payment type distribution on payment value vs payment installment shows some interesting informations:
        - The distribution of payment using credit card has positive skewness and the range is from 0 -24. The payment installment using credit card centered in 5 - 10.
        - There's a extreme payment value done using credit card with 1 installment with value 14,000.
        - The other payment categories are lie on first installment. Among these 4 payment categories, buleto has several transactions with value from 6,000 - ~7,800
    '''
    )