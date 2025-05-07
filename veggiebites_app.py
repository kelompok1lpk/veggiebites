import streamlit as st

# Ganti dengan direct image URL kamu
background_url = "https://i.ibb.co.com/xqwsXfq8/IMG-0774.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SESSION STATE UNTUK NAVIGASI ----------
if 'page' not in st.session_state:
    st.session_state.page = 0

# ---------- HALAMAN-HALAMAN ----------
def halaman_1():
    st.markdown(
        """
        <h1 style="
            font-weight: 1000;
            color: #1A1A1A;
            text-shadow: 1px 1px 3px rgba(255,255,255,0.6);
            background-color: rgba(255, 255, 255, 0.6);
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        ">
            🥦Helloooww welcome at VeggieBites guys!!
        </h1>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("Cari tahu yukk tipe vegetarian kamu yang mana biar kita bisa bantu kasih menu sehat yang sesuai buat kamuu><.")

    pilihan = st.radio(
        "Kamu termasuk tipe vegetarian yang mana nih?",
        [
            "Lacto-ovo (telur & susu masih aku makan sieh)",
            "Lacto (only susu, telur big no no)",
            "Ovo (telur oke sieh, tapi susu ga dulu deh)",
            "Vegan total (no hewani et all)"
        ]
    )
    
    if st.button("Next"):
        st.session_state.page += 1


def halaman_2():
    st.title("Kebutuhan Nutrisi Kamu")
    st.markdown("Sebagai vegetarian, kamu perlu perhatian khusus pada beberapa nutrisi ini loh:")
    st.markdown("""
    - Protein: Tempe, tahu, kacang-kacangan, Telur, Biji Chia, Quinoa, Bayam
    - Zat Besi: Bayam, Brokoli, Kacang Merah, Buncis, Lentil
    - Vitamin B12: Susu Kedelai Fortifikasi, suplemen, Serealia, Nori
    - Kalsium: Tahu, Almond, Sayur Hijau, Susu Kedelai
    - Omega-3: Flaxseed, Spirulina, Chlorella
    """)
    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1


def halaman_3():
    st.title("Rekomendasi Menu Vegetarian Buat Kamu")
    st.subheader("1. 💚Smoothie Green💚")
    st.markdown("Bahan: Bayam, pisang, susu almond, chia seed")
    st.subheader("2. 🫑Tofu Stir Fry🥕")
    st.markdown("Bahan: Tahu, paprika, wortel, kecap asin")
    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1


def halaman_4():
    st.title("Cari Pengganti Bahan")
    bahan_input = st.text_input("Masukkan nama bahan yang mau diganti:")
    pengganti = {
        "susu": "susu almond / oat milk",
        "telur": "chia egg (chia + air)",
        "daging": "jamur, tempe, atau tofu",
        "keju": "keju vegan berbasis kacang"
    }
    if st.button("Search"):
        hasil = pengganti.get(bahan_input.lower(), "Bahan tidak ditemukan")
        st.success(f"Pengganti untuk {bahan_input}: {hasil}")

    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1


def halaman_5():
    st.title("Terima Kasih Telah Berkunjung!")
    st.markdown("Semoga VeggieBites bermanfaat untuk kamu!")
    if st.button("Back"):
        st.session_state.page -= 1


# ini juga
halaman_fungsi = [halaman_1, halaman_2, halaman_3, halaman_4, halaman_5]

# tambahin nih
halaman_fungsi[st.session_state.page]()
