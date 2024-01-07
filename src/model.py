from transformers import pipeline

clf = pipeline(
    task = 'sentiment-analysis', 
    model = 'SkolkovoInstitute/russian_toxicity_classifier')

text = ['У нас в есть убунты и текникал превью.',
    	'Как минимум два малолетних дегенерата в треде, мда.',
        'иди на хер']


def analyse(text):
    text=[text]
    result=clf(text)
    print(result)
    return result

print(analyse("Кто любит жаб? Они крутые."))