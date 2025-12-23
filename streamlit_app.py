"""
Streamlit Dashboard - PhotoFlow Analytics
==========================================
Bu dashboard, PhotoFlow uygulamasının verilerini görselleştirir.

Streamlit Nedir?
-----------------
Streamlit, Python ile hızlıca interaktif web uygulamaları ve dashboard'lar 
oluşturmanızı sağlayan açık kaynaklı bir framework'tür.

Temel Özellikleri:
- 📊 Veri Görselleştirme: Grafikler, tablolar, haritalar kolayca oluşturulur
- 🔄 Reaktif: Kod değiştiğinde otomatik güncellenir  
- 🎛️ Widget'lar: Butonlar, slider'lar, selectbox'lar ile etkileşim
- 📦 Kolay Kullanım: Minimum kod ile maksimum sonuç
- 🚀 Hızlı Prototipleme: ML modellerini saniyeler içinde demo'ya çevirir

Çalıştırmak için: streamlit run streamlit_app.py
"""

import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Sayfa yapılandırması
st.set_page_config(
    page_title="PhotoFlow Dashboard",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a25 0%, #12121a 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    .streamlit-info {
        background: linear-gradient(135deg, rgba(255, 75, 75, 0.1) 0%, rgba(255, 107, 107, 0.05) 100%);
        border: 1px solid rgba(255, 75, 75, 0.3);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# API URL
API_BASE_URL = "http://localhost:8000"


def get_api_data(endpoint: str, token: str = None):
    """API'dan veri çek"""
    try:
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = requests.get(f"{API_BASE_URL}{endpoint}", headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException:
        return None


# Sidebar
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)
    st.title("📸 PhotoFlow")
    st.markdown("---")
    
    # Streamlit Hakkında
    st.markdown("### 🎯 Streamlit Nedir?")
    st.info("""
    **Streamlit**, Python ile hızlıca interaktif web uygulamaları 
    oluşturmanızı sağlayan açık kaynaklı bir framework'tür.
    
    - 🐍 Sadece Python bilgisi yeterli
    - ⚡ Saniyeler içinde prototip
    - 📊 Veri bilimi için ideal
    """)
    
    st.markdown("---")
    
    # Giriş formu
    st.markdown("### 🔐 API Bağlantısı")
    
    if "token" not in st.session_state:
        st.session_state.token = None
    
    if st.session_state.token is None:
        email = st.text_input("📧 E-posta", placeholder="ornek@email.com")
        password = st.text_input("🔑 Şifre", type="password")
        
        if st.button("🚀 Giriş Yap", use_container_width=True):
            try:
                response = requests.post(
                    f"{API_BASE_URL}/login",
                    data={"username": email, "password": password},
                    timeout=5
                )
                if response.status_code == 200:
                    st.session_state.token = response.json().get("access_token")
                    st.success("✅ Giriş başarılı!")
                    st.rerun()
                else:
                    st.error("❌ Giriş başarısız!")
            except requests.exceptions.RequestException:
                st.error("⚠️ API'ya bağlanılamadı!")
    else:
        st.success("✅ Bağlantı aktif")
        if st.button("🚪 Çıkış Yap", use_container_width=True):
            st.session_state.token = None
            st.rerun()


# Ana sayfa
st.markdown('<h1 class="main-header">📸 PhotoFlow Dashboard</h1>', unsafe_allow_html=True)

# Streamlit açıklama kutusu
with st.expander("🎯 Streamlit Hakkında Bilgi", expanded=False):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Streamlit Nedir?
        
        Streamlit, Python ile **hızlıca interaktif web uygulamaları** ve 
        **veri dashboard'ları** oluşturmanızı sağlayan açık kaynaklı bir framework'tür.
        
        **Ana Kullanım Alanları:**
        - 📊 Veri analizi ve görselleştirme
        - 🤖 Makine öğrenimi model demo'ları
        - 📈 İş zekası dashboard'ları
        - 🔬 Bilimsel hesaplama arayüzleri
        """)
    
    with col2:
        st.markdown("""
        ### Temel Özellikler
        
        | Özellik | Açıklama |
        |---------|----------|
        | 🔄 **Reaktif** | Kod değişince otomatik güncellenir |
        | 🎛️ **Widget'lar** | Buton, slider, selectbox vb. |
        | 📦 **Kolay** | Minimum kod, maksimum sonuç |
        | 🚀 **Hızlı** | Saniyeler içinde prototip |
        | 🐍 **Pythonic** | Sadece Python bilgisi yeter |
        """)

st.markdown("---")

# Metrikler
st.markdown("### 📊 Uygulama Metrikleri")

col1, col2, col3, col4 = st.columns(4)

# API durumu
api_status = get_api_data("/") is not None

with col1:
    if api_status:
        st.metric(label="🟢 API Durumu", value="Aktif", delta="Bağlı")
    else:
        st.metric(label="🔴 API Durumu", value="Kapalı", delta="Bağlantı yok")

with col2:
    st.metric(label="📸 Streamlit", value="v1.52.2", delta="Güncel")

with col3:
    st.metric(label="⚡ FastAPI", value="Backend", delta="Çalışıyor" if api_status else "Kapalı")

with col4:
    st.metric(label="🗄️ SQLite", value="test.db", delta="Veritabanı")

st.markdown("---")

# Streamlit Özellikleri Demo
st.markdown("### 🎛️ Streamlit Widget Demo'ları")

tab1, tab2, tab3 = st.tabs(["📊 Grafikler", "🎚️ Kontroller", "📝 Formlar"])

with tab1:
    st.markdown("#### Örnek Grafik Türleri")
    
    # Örnek veri
    chart_data = pd.DataFrame({
        "Gün": ["Pzt", "Sal", "Çar", "Per", "Cum", "Cmt", "Paz"],
        "Paylaşım": [12, 19, 8, 15, 22, 30, 25],
        "Görüntülenme": [120, 190, 80, 150, 220, 300, 250]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**📈 Çizgi Grafik**")
        st.line_chart(chart_data.set_index("Gün"))
    
    with col2:
        st.markdown("**📊 Bar Grafik**")
        st.bar_chart(chart_data.set_index("Gün"))

with tab2:
    st.markdown("#### İnteraktif Kontroller")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        slider_val = st.slider("🎚️ Slider", 0, 100, 50)
        st.write(f"Seçilen değer: **{slider_val}**")
    
    with col2:
        select_val = st.selectbox("📋 Seçim Kutusu", ["Seçenek 1", "Seçenek 2", "Seçenek 3"])
        st.write(f"Seçilen: **{select_val}**")
    
    with col3:
        toggle_val = st.toggle("🔘 Toggle", value=True)
        st.write(f"Durum: **{'Açık' if toggle_val else 'Kapalı'}**")
    
    # Progress bar
    st.markdown("**📊 Progress Bar**")
    progress = st.progress(0)
    if st.button("▶️ Animasyonu Başlat"):
        import time
        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)
        st.balloons()

with tab3:
    st.markdown("#### Form Örneği")
    
    with st.form("demo_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 İsim")
            email = st.text_input("📧 E-posta")
        
        with col2:
            age = st.number_input("🎂 Yaş", min_value=0, max_value=120)
            city = st.selectbox("🏙️ Şehir", ["İstanbul", "Ankara", "İzmir", "Bursa"])
        
        message = st.text_area("💬 Mesaj")
        
        submitted = st.form_submit_button("📤 Gönder", use_container_width=True)
        
        if submitted:
            st.success(f"✅ Form gönderildi! Merhaba {name}!")

st.markdown("---")

# API Verisi (giriş yapılmışsa)
if st.session_state.token:
    st.markdown("### 📷 Son Paylaşımlar")
    
    images = get_api_data("/images", st.session_state.token)
    
    if images and len(images) > 0:
        cols = st.columns(4)
        for idx, img in enumerate(images[:8]):
            with cols[idx % 4]:
                st.image(f"{API_BASE_URL}/uploads/{img['filename']}", use_container_width=True)
                st.caption(img.get("caption", "Açıklama yok")[:30])
    else:
        st.info("📭 Henüz paylaşım yok. PhotoFlow'a gidip paylaşım yapın!")
else:
    st.info("🔐 API verilerini görmek için sol taraftaki menüden giriş yapın.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 1rem;">
    <p>🚀 Streamlit ile oluşturuldu | 📸 PhotoFlow Dashboard</p>
    <p style="font-size: 0.8rem;">
        Bu dashboard, Streamlit'in gücünü göstermek için tasarlanmıştır.
    </p>
</div>
""", unsafe_allow_html=True)

