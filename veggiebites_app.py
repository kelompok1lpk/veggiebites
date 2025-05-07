import streamlit as st

# ---------- CONFIGURASI PAGE ----------
st.set_page_config(page_title="Menu Sehat Vegetarian", layout="centered")

# ---------- STYLING GEMES ----------
page_bg_img = '''
<style>
body {
background-image: url("https://i.ibb.co/GTX4kSM/bg-gemes.jpg");
background-size: cover;
}
div.stButton > button {
    background-color: #FFD3DA;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 8em;
    margin: 1em 0.5em;
}
h1, h2, h3 {
    color: #FF6F91;
    text-align: center;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# ---------- SESSION STATE UNTUK NAVIGASI ----------
if 'page' not in st.session_state:
    st.session_state.page = 0

# ---------- KONTEN SETIAP HALAMAN ----------
def halaman_1():
    st.title("🥦Hellooww welcome at VeggieBites guys!!")
    st.markdown("*Cari tahu yukk tipe vegetarian kamu yang mana biar kita bisa bantu kasih menu sehat yang sesuai buat kamuu><.*")
    pilihan = st.radio("Kamu termasuk tipe vegetarian yang mana nih?", 
        ["Lacto-ovo (telur & susu masih aku makan sieh)",
         "Lacto (only susu, telur big no no no)",
         "Ovo (telur oke sieh, tapi susu ga dulu deh)",
         "Vegan total (no hewani at all)"])
    st.session_state["tipe_vegetarian"] = pilihan
    if st.button("Next"):
        st.session_state.page += 1

def halaman_2():
    st.title("Kebutuhan Nutrisi Kamu")
    st.markdown("Sebagai vegetarian, kamu perlu perhatian khusus pada beberapa nutrisi ini loh:")
    st.markdown("""
    - *Protein*: Tempe, tahu, kacang-kacangan, Telur, Biji Chia, Quinoa, Bayam
    - *Zat Besi*: Bayam, Brokoli, Kacang Merah, Buncis, Lentil, Aprikot, Selada Air, Kangkung
    - *Vitamin B12*: Susu Kedelai Fortifikasi, suplemen, Serealia, Nori, Margarin Nabati, Susu, Keju, Yoghurt, Sereal Sarapan (Malt-O-Meal Raisin Bran), Apel, Pisang, Blueberry, Jeruk, Kismis
    - *Kalsium*: Tahu, Almond, Sayur Hijau, Susu Kedelai, Kubis, Okra, Kiwi, Pepaya, Jambu Biji
    - *Omega-3*: Flaxseed, Spirulina, Chlorella, Biji Rami, Kacang Kenari
    """)
    st.markdown("Tenang guys, nanti kita kasih menunya juga kok!")
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page -= 1
    if col2.button("Next"):
        st.session_state.page += 1

def halaman_3():
    st.title("Rekomendasi Menu Vegetarian Buat Kamu Si VeggieLovers")

    st.subheader("1. 💚Smoothie Green💚")
    st.markdown("*Bahan:* Bayam, pisang, susu almond, chia seed")
    st.markdown("*Cara buat:* Blender semua bahan sampai halus dan sajikan dingin.")

    st.subheader("2. 🫑Tofu Stir Fry🥕")
    st.markdown("*Bahan:* Tahu, paprika, wortel, kecap asin, minyak wijen")
    st.markdown("*Cara buat:* Tumis semua bahan hingga matang, sajikan dengan nasi.")

    st.subheader("3. 🍫Overnight Oat Choco-Berry🍓")
    st.markdown("*Bahan:* Oat, susu oat, kakao bubuk, stroberi")
    st.markdown("*Cara buat:* Campur bahan, simpan di kulkas semalam.")

    st.subheader("4. 🥜Salad Kacang🥜")
    st.markdown("*Bahan:* Kacang merah, jagung, tomat, alpukat")
    st.markdown("*Cara buat:* Campur semua bahan dengan dressing lemon & olive oil.")

    st.subheader("5. 🥬Veggie Wrap🥬")
    st.markdown("*Bahan:* Tortilla, selada, wortel, hummus, timun")
    st.markdown("*Cara buat:* Isi tortilla dengan semua bahan dan gulung.")

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page -= 1
    if col2.button("Next"):
        st.session_state.page += 1

def halaman_4():
    st.title("Butuh Pengganti Bahan?")
    st.markdown("Masukkan bahan yang ingin diganti, nanti kita bantu kasih alternatifnya!")

    bahan = st.text_input("Contoh: susu, telur, daging, keju, dll")
    if bahan:
        pengganti = {
            "susu": "susu almond / oat milk",
            "telur": "chia egg (chia + air)",
            "daging": "jamur, tempe, atau tofu",
            "keju": "keju vegan berbasis kacang",
            "daging sapi/ayam": "tempe, tahu, jamur tiram, jackfruit (nangka muda), seitan (gluten gandum), lentil",
            "daging giling": "kacang hitam, kacang merah, walnut cincang, tahu hancur",
            "susu sapi": "susu almond, susu kedelai, oat milk, coconut milk, cashew milk",
            "keju cheddar/parmesan": "keju nabati dari kacang mete, nutritional yeast (untuk rasa cheesy)",
            "cream cheese": "tahu sutra + lemon + garam (di-blend)telur",
            "mentega": "minyak kelapa, margarin vegan, alpukat",
            "mayones": "mayones vegan (tanpa telur), campuran tofu + mustard + lemonTahu sutra + lemon",     
            }
        hasil = pengganti.get(bahan.lower(), "bahan yang kamu cari ga ada nih, cari yang lain yuk")
        st.success(f"Pengganti untuk *{bahan}*: {hasil}")

        
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page -= 1
    if col2.button("Next"):
        st.session_state.page += 1

def halaman_5():
    st.title("Thank you for visiting our website!!")
    st.markdown("^^Semoga VeggieBites bisa selalu membantumu yaa^^")
    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page -= 1
# ---------- JALANKAN HALAMAN ----------
halaman_fungsi = [halaman_1, halaman_2, halaman_3, halaman_4, halaman_5]
halaman_fungsi[st.session_state.page]()
