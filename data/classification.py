import fastf1

def get_classification(provider):
    # 1️⃣ Pega todas as voltas
    laps = provider.get_laps()

    # 2️⃣ Remove voltas inválidas (sem tempo)
    laps = laps.dropna(subset=['LapTime'])

    # 3️⃣ Melhor volta de cada piloto
    best_laps = laps.loc[laps.groupby('Driver')['LapTime'].idxmin()]

    # 4️⃣ Ordena pela melhor volta e reseta índice
    classification = best_laps.sort_values('LapTime').reset_index(drop=True)

    # 5️⃣ Adiciona a posição correta
    classification['Position'] = classification.index + 1

    # 6️⃣ Calcula o GAP em Timedelta
    leader_lap = classification.iloc[0]['LapTime']
    classification['Gap'] = classification['LapTime'] - leader_lap

    # 7️⃣ Formata o GAP bonitinho com 2 casas decimais
    def format_gap(row):
        if row['Position'] == 1:
            return '-'
        else:
            return f"+{row['Gap'].total_seconds():.2f}"

    classification['Gap'] = classification.apply(format_gap, axis=1)

    # 8️⃣ Formata LapTime para mm:ss.sss
    classification['LapTime'] = classification['LapTime'].apply(lambda x: f"{int(x.total_seconds()//60)}:{x.total_seconds()%60:.3f}")

    # 9️⃣ Reordena colunas
    classification = classification[['Position', 'Driver', 'LapTime', 'Gap', 'Compound']]

    return classification