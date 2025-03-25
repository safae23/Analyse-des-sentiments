from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import matplotlib.pyplot as plt
import seaborn as sns

def score(x):
    blob1 = TextBlob(x)
    return blob1.sentiment.polarity


def analyse(x):
        if x >0:
            return 'Positive 😍'
        elif x <0:
            return 'Negative 😡'
        else:
            return 'Neutral 🙂'
st.header(':red[Sentiment Analysis] :red[---] :blush: :red[--] :neutral_face: :red[--] :angry: :red[---]')
with st.expander('Analyze text :page_with_curl: '):
    text = st.text_input('Text here :lower_left_ballpoint_pen: : ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
        st.write('Sentiment: ', analyse(round(blob.sentiment.polarity, 2)))

    pre = st.text_input('Clean text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
                                 stopwords=True, lowercase=True, numbers=True, punct=True))

with st.expander('Analyze CSV :open_file_folder:'):
    upl = st.file_uploader('upload file')

    if upl:
        df = pd.read_excel(upl)
        del df['Unnamed: 0']
        df['score'] = df['reviewText'].apply(score)

        df['analysis'] = df['score'].apply(analyse)

        st.write(df.head(10))

        # Calcul du pourcentage de valeurs positives, négatives et neutres
        positive_percentage = (df['analysis'] == 'Positive 😍').mean() * (100*100/45)
        neutral_percentage = (df['analysis'] == 'Neutral 🙂').mean() * (100 * 100 / 45)
        negative_percentage = (df['analysis'] == 'Negative 😡').mean() * (100*100/45)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        # Visualisation avec matplotlib
        plt.figure(figsize=(8, 6))
        sns.barplot(x=['Positive','Neutral', 'Negative'], y=[positive_percentage,neutral_percentage, negative_percentage ])
        plt.title("Distribution of sentiment Analysis")
        plt.ylabel('Percentage')
        st.pyplot()

        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',

        )