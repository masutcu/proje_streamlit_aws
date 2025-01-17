import streamlit as st 

# text /file
st.title("Streamlit Tutorioal") # H1 başlık ekler
st.text("Hello Streamlit") # metin ekler
# makaleden kopyalarken cift tirnaklari degistirmek gerek, hata veriyor
st.text("Hello Mehmet Ali") # metin ekler
st.markdown("**markdown text**")

st.success("Green Text")  # Yeşil bant yazı ekler
st.info("Blue text")  # Mavi bant yazı ekler

#resim ekleme
from PIL import Image
img=Image.open('car.jpg')
st.image(img, width=600, caption="Car Prediction")

# alt başlık ekleme
st.header("This is a header")   # alt başlık ekler
st.subheader("This is a subheader")  # daha küçük bir alt başlık ekler
st.write("Writing example text ")  # bilgilendirme text'i ekler

# video dosyası ekleme
# youtube dan eklemek için
#st.video(video)
#st.video('https://www.youtube.com/watch?v=4Jvw37NoumY&t=39s')
#video=open("intro-1.mp4", "rb") # bilgisayara yüklü video
st.video('https://www.youtube.com/watch?v=xhGwjUKbiC4')  # youtube’dan bir videoyu eklemek için

# chekbox eklemek
if st.checkbox("On/Off"):
    st.text("You Selected box")
    
# chekbox eklemek -> isaretleyince gorunmesini istedigimiz kodlari if'in altina yazabiliriz
# radio button   olusturma
car=st.radio("Select your car ", ("BMV", "Audi"))
if car == "BMV" :
    st.success("Congrats")
else:
    st.info("Good car")
# get help  (Herhangi bir nesnenin yardım dokümantasyonunu gösterir)
#st.help(st.slider)

# select box  (Açılır menü ekler)
menu=st.selectbox("Your program is ", ["DS", "DEV", "Cyber"])
st.write("Your program is", menu)

# multiselect (Birden fazla seçenek seçilebilen bir kutu ekler)
career = st.multiselect("Select your career", ["IT", "Engineer", "Doctor"])
st.write("Your career is", career)

# slider  (Kullanıcının değer seçebilmesi için kaydırıcı ekler)
points=st.slider("How many points" ,1,10)

# button (Bir buton ekler)
if st.button("Tıkla"):
    st.write("Butona tıklandı")
if st.button("Prediction"):  # buradan sonra yapilan predictionlar icin kodlar yazilir
    st.write("Prediction yapildi")

# text input  (Metin girişi için bir kutu ekler)
name= st.text_input("Enter your name:")
if st.button("Run"):
    st.success(name.title())   # girilen ismin ilk harfini “.title() “ ile büyük harfe çevirir

# text area  (Metin girişi için bir yazım alanı ekler)
area= st.text_area("paragraf yazabilirsiniz:")

# date input (Tarih seçimi için bir kutu ekler)
import datetime
today=st.date_input("Today is" , datetime.datetime.now())  # now() ile bugünün tarihini ekler

# rakam şeklinde input
st.number_input('Pick a number', 0, 10)

# multiple line  code (Çoklu satır halinde kod satırı yazımı)
with st.echo():   # Kodu ve kodun çıktısını aynı anda gösterir.
    import pandas as pd
    import numpy as np
    import streamlit  as st

# code raw   (tek satırlık kod şeklinde yazdırmak için )
st.code("import pandas as pd")

# sidebar  (Yan panel alanı ekler)
st.sidebar.title("Yan panel başlık yazısı")

#sidebar
st.sidebar.title("Sayının karesini hesaplama")
st.sidebar.markdown("## alt baslik")
a=st.sidebar.slider("input",0,10,2,1)
# sonuclar icin
st.write("# sidebar input result") # sidebarda gozukmuyor cunku o tarafa yazdirmadik
st.success(a*a)


# Dosya Yükleme
import pandas as pd      # ilgili kütüphane import edilir
# Dosya yükleme widget'ını ekleyin. Örnek dosya Advertising.csv olsun.
uploaded_file = st.file_uploader("Advertising.csv", type=["csv"])

# Eğer bir dosya yüklendiyse, bu dosyayı pandas ile okuyun
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)  # DataFrame'i ekrana yazdır

# Plotly ile bir scatter plot oluşturalım. Örneğin, TV reklam bütçesi ile satışları karşılaştıralım.Advertising.csv dosyası ile yapalım
import plotly.express as px
fig = px.scatter(data, x='TV', y='sales', title='TV Reklamları vs. Satışlar') # data onceden okutulmali tabii
st.plotly_chart(fig)

# Vega-Lite ile bir bar chart oluşturalım. Örneğin, radyo reklam bütçesinin ortalamasını gösterelim. Advertising.csv dosyasını kullanıyoruz
bar_chart = {
    "mark": "bar",
    "encoding": {
        "x": {"field": "radio", "bin": True, "type": "quantitative"},
        "y": {"aggregate": "average", "field": "sales", "type": "quantitative"}
    }
}
st.vega_lite_chart(data, bar_chart)
# st.pyplot(): Bu fonksiyon, Matplotlib ile oluşturulan grafikleri göstermek için kullanılır. Örneğin, TV reklam bütçesi ile satışları bir scatter plot ile gösterelim. Advertising.csv dosyasını kullanıyoruz
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.scatter(data['TV'], data['sales'], color='blue')
plt.title('TV Reklamları vs. Satışlar')
plt.xlabel('TV Reklam Bütçesi')
plt.ylabel('Satışlar')
st.pyplot(plt)

#map eklemek için 
# st.map():Bu fonksiyon, coğrafi veri görselleştirmesi için kullanılır. Advertising.csv bu tür verilere sahip olmadığı için bu fonksiyonun kullanımı bu veri seti için uygun değil. Ancak, genel bir örnek vermek gerekirse:
# Örnek veri
map_data = pd.DataFrame({
    'lat': [37.76, 37.77, 37.78],
    'lon': [-122.4, -122.5, -122.6]
})
st.map(map_data)

#linechart
# st.line_chart():Bu fonksiyon, çizgi grafikleri göstermek için kullanılır. Örneğin, veri setindeki satışları bir çizgi grafiği ile gösterelim:
st.line_chart(data['sales'])

#st.altair_chart():Altair ile bir bar chart oluşturalım. Örneğin, radyo reklam bütçesi ile satışları karşılaştıralım. Advertising.csv dosyasını kullanıyoruz:
import altair as alt
chart = alt.Chart(data).mark_bar().encode(
    x='radio',
    y='sales',
    color='sales'
).properties(
    title='Radyo Reklamları vs. Satışlar'
)
st.altair_chart(chart, use_container_width=True)


# Veri çerçevesini görüntüler
# NOT: öncesinde terminalde  pip install tabulate  yapmalısınız
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
st.code(
    df.to_markdown(),
    #lang="markdown",
    #linenumbers=True,
)
# st.checkbox ( Onay kutusu oluşturur)
if st.checkbox('Onayla'): st.write('Onaylandı!')

st.balloons()     # Eğlenceli bir görünüm olarak sayfaya balon ve kar tanesi efekti ekliyor
st.snow()

# html tarzda gorunum icin:
st.markdown(
    """
    <div style='background-color: orange; padding: 10px;'>
    <h1 style='color: white; text-align: center;'>Streamlit Arayüzü</h1>
    </div>
    """,
    unsafe_allow_html=True
)


