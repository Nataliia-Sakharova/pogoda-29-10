st.divider()
    # Tabela z wynikami

    st.subheader("Tabela z wynikami")

    rows = df.head(int(selected_rows))
    st.dataframe(rows)

    st.divider()

    # Wykresy liniowe

    st.subheader("Temperatura w czasie")

    temp_chart = df.set_index(
        "timestamp"
    )[["temp","feels_like"]]

    st.line_chart(temp_chart)

    # Wykres z wyborem kolumny

    st.subheader("Customowy wykres")

    custom_chart = df.set_index(
        "timestamp"
    )[[selected_col]]

    st.line_chart(custom_chart)