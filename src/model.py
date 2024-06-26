from transformers import pipeline

# Создание классификатора для анализа тональности текста
clf = pipeline(
    task="sentiment-analysis",
    model="SkolkovoInstitute/russian_toxicity_classifier"
)

# Примеры текстов для анализа
text = [
    "У нас в есть убунты и текникал превью.",
    "Как минимум два малолетних дегенерата в треде, мда.",
    "иди на хер"
]


# Функция для анализа текста
def analyse(text):
    text = [text]
    result = clf(text)
    # print(result)
    return result


# Проверка функции при запуске скрипта
if __name__ == 'main':
    print(analyse("Кто любит жаб? Они крутые."))
