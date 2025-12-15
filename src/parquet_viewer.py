import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="CSV/Parquet Viewer", layout="wide")
st.title("Visualizador de CSV / Parquet Interativo")

# --------------------------
# Carregar ficheiro
# --------------------------
uploaded_file = st.file_uploader(
    "Carrega ficheiro Parquet ou CSV", type=["parquet", "csv"]
)

if uploaded_file is not None:
    # Ler ficheiro
    if uploaded_file.name.lower().endswith(".parquet"):
        df = pd.read_parquet(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)

    st.success(f"✅ Ficheiro `{uploaded_file.name}` carregado com sucesso!")

    # Converter colunas de datas automaticamente
    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

    st.subheader("📊 Dados carregados")
    st.dataframe(df, use_container_width=True, height=400)
    st.write(f"➡️ Número de linhas: **{len(df)}**")

    # --------------------------
    # Preparar colunas
    # --------------------------
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    datetime_cols = df.select_dtypes(include=["datetime"]).columns.tolist()

    # --------------------------
    # Seleção do intervalo
    # --------------------------
    st.subheader("Intervalo a visualizar")

    if "timestamp" in df.columns and pd.api.types.is_datetime64_any_dtype(
        df["timestamp"]
    ):
        # Garantir que timestamp é datetime
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        min_date = df["timestamp"].min().date()
        max_date = df["timestamp"].max().date()

        # Input de intervalo de datas
        date_range = st.date_input(
            "Selecione o intervalo de datas",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date,
        )

        # Filtrar df pelo intervalo selecionado
        start_date, end_date = (
            pd.to_datetime(date_range[0]),
            pd.to_datetime(date_range[1]),
        )
        df_filtered = df[
            (df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)
        ]
    else:
        # Fallback para índice
        num_samples = st.number_input(
            "Número de samples a mostrar",
            min_value=10,
            max_value=len(df),
            value=100,
            step=10,
        )

        max_start = max(len(df) - num_samples, 0)

        start_idx = st.number_input(
            "Índice inicial", min_value=0, max_value=max_start, value=0, step=1
        )

        end_idx = start_idx + num_samples
        df_filtered = df.iloc[start_idx:end_idx]

    st.write(f"➡️ Número de linhas selecionadas: **{len(df_filtered)}**")

    # --------------------------
    # Seleção do eixo X
    # --------------------------
    x_axis = st.selectbox(
        "Escolha a feature para o eixo X (datas/horas ou números, opcional):",
        ["None"] + numeric_cols + datetime_cols,
    )
    if x_axis == "None":
        x_values = list(range(len(df_filtered)))
        x_label = "Index"
    else:
        x_values = df_filtered[x_axis]
        x_label = x_axis

    # --------------------------
    # Seleção múltipla de colunas Y
    # --------------------------
    st.subheader("Seleção de features para plotar (multi-select)")

    selected_cols = st.multiselect(
        "Selecione colunas numéricas para o eixo Y",
        options=numeric_cols,
        default=numeric_cols[:1] if numeric_cols else [],
    )

    # --------------------------
    # Gerar gráfico
    # --------------------------
    if selected_cols:
        plot_df = df_filtered[selected_cols].copy()
        plot_df[x_label] = x_values

        fig = px.line(
            plot_df,
            x=x_label,
            y=selected_cols,
            title="Gráfico Multi-feature Interativo",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Selecione pelo menos uma coluna numérica para plotar.")

else:
    st.info("👆 Carrega um ficheiro para começar.")
