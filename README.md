# Belajar Analisis Data dengan Python @ Dicoding

# Analisis Air Quality Dataset

## Latar Belakang

Proyek ini melakukan analisis komprehensif dari dataset kondisi udara di Beijing, China. Tujuan analisis adalah untuk mengidentifikasi tren kecepatan angin (WSPM) setiap bulannya di salah satu distrik yaitu Dongsi, hal tersebut berkaitan dengan analisis selanjutnya yaitu meninjau korelasi kecepatan angin (WSPM) terhadap penyebaran polusi udara  (PM2.5, PM10, NO2, SO2, O3), korelasi antara suhu (TEMP) dengan polusi udara (PM2.5, PM10, NO2, SO2, O3), serta korelasi antara satu polutan dengan polutan lainnya (PM2.5, PM10, NO2, SO2, O3). Repositori ini mencakup file README, notebook analisis, dataset, dan dashboard Streamlit yang memperlihatkan hasil eksplorasi data secara interaktif.

## Penulis

- **Nama:** Dina Lestari
- **Email:** lestaridina096@gmail.com
- **MyProfil Dicoding:** dinals

## Berkas

- `proyek_akhir_dina.ipynb`: Notebook Jupyter yang berisi analisis data.
- `README.md`: File berisi penjelasan mengenai proyek
- `url.txt`: File berisi link dashboard
- `requirements.txt`: File berisi library/module yang dipakai dalam proyek
- `data`: Direktori yang berisi file dataset & deskripsi dataset
- `dashboard`: Direktori yang berisi aplikasi dashboard Streamlit

## Hasil Analisis

- **Pertanyaan:**
    - Bagaimana tren kecepatan angin setiap bulannya di station Dongsi?
    - Bagaimana korelasi antara suhu (TEMP) dengan polusi udara (PM2.5, PM10, NO2, SO2, O3) di station Dongsi?
    - Bagaimana korelasi kecepatan angin (WSPM) terhadap penyebaran polusi udara  (PM2.5, PM10, NO2, SO2, O3) di station Dongsi?
    - Bagaimana korelasi antar berbagai polutan (PM2.5, PM10, NO2, SO2, O3) di station Dongsi?

- **Pertanyaan 1:** 
    - Dapat diketahui, pada Distrik Dongsi kecepatan angin cenderung tinggi dari bulan ke 4 (April) sampai bulan ke 5 (Mei).

- **Pertanyaan 2:**
    - Korelasi antara Temparature dengan polutan di station dongsi menunjukkan **korelasi positif yang sedang** pada O3. Artinya, ada hubungan yang cukup kuat antara kenaikan suhu dan peningkatan konsentrasi O3 (ozon).

- **Pertanyaan 3:**
    -  Korelasi antara kecepatan angin (WSPM) dengan meningkatkanya polutan di station dongsi menunjukkan **korelasi positif yang lemah** pada O3. Ini berarti ada keterkaitan antara peningkatan kecepatan angin dan kenaikan konsentrasi O3, tetapi hubungan tersebut tidak kuat. Artinya ketika kecepatan angin meningkat, konsentrasi O3 juga cenderung sedikit meningkat atau efeknya tidak terlalu besar.

- **Pertanyaan 4:**
    - Korelasi antara PM2.5 dengan PM10 memiliki nilai **korelasi positif yang tinggi**, ini artinya ketika salah satu polutan meningkat maka polutan yang lainnya juga akan meningkat. sedangkan dengan SO2 dan NO2 memiliki **korelasi positif sedang**.
    - Korelasi PM10 dengan SO2 dan NO2 memiliki **korelasi positif sedang**.
    - korelasi SO2 dengan NO2 memiliki **korelasi positif rendah**.
    - Polutan O3 memiliki **korelasi negatif** dengan polutan lainnya (PM2.5, PM10, SO2, NO2)

## Cara Menjalankan

- Notebook Jupyter dapat dilihat langsung di GitHub atau dijalankan dalam lingkungan yang mendukung Jupyter Notebook Python.
- Dashboard Streamlit dapat dijalankan secara lokal dengan navigasi ke direktori `dashboard` dan menjalankan `streamlit run dashboard.py` pada terminal/shell.

## Environment

### Setup environment

conda create --name submission python=3.9
conda activate submission
pip install -r requirements.txt 

### Run streamlit app

streamlit run dashboard.py
https://beijing-aq-dlstr9.streamlit.app/  
