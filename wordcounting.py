import re
from collections import Counter
import matplotlib.pyplot as plt
from pymystem3 import Mystem
from wordcloud import WordCloud

STOP_WORDS = {
    'в', 'на', 'по', 'из', 'с', 'к', 'у', 'о', 'за', 'под', 'над', 'для', 'без', 'до', 'при', 'через', 'после', 'перед', 'между', 'со', 'во',
    'ни', 'от', 'про','при',  
    'такой', 'свой',                
    'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они',
    'мой', 'твой', 'его', 'её', 'их', 'наш', 'ваш',
    'который', 'этот', 'тот', 'весь', 'каждый', 'другой',
    'это',  
    'и', 'а', 'но', 'да', 'или', 'же', 'ли', 'бы', 'ну', 'вот', 'вон','не', 'также',
    'ещё', 'уже', 'только', 'даже', 'как', 'так', 'что', 'чтобы', 'если', 'когда', 'потому', 'очень', 'еще',
    'быть', 'стать', 'являться', 'мочь', 'хотеть', 'идти', 'сказать', 'говорить', 'значить',
    'нет', 'да', 'можно', 'нужно', 'надо',
    'риа', 'новость', 'июн'
}

mystem = Mystem()

def read_text(filename):
    with open(filename, 'r',encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^а-яё\s]', '', text)
    words = text.split()
    return words

def filter_stop_words(words,stop_words):
    return [w for w in words if w not in stop_words]

def lemmatize_words(words):
    text = ' '.join(words)
    lemmas = mystem.lemmatize(text)
    cleaned = [w for w in lemmas if w.strip()]
    return cleaned

def count_words(words):
    words_counts = Counter(words)
    return words_counts
    

def plot_top(words_counts):
    words, counts = zip(*words_counts)
    plt.figure(figsize=(10,6))
    plt.bar(words, counts)
    plt.title('20 самых частотных слов:')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top20.png')
    plt.show()

def generate_wordcloud(counter, output_file='wordcloud.png'):
    font_path = 'C:/Windows/Fonts/arial.ttf' 
    wc = WordCloud(
        font_path=font_path,
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='viridis'
    )
    wc.generate_from_frequencies(counter)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f'词云已保存为 {output_file}')
    plt.show()
    

if __name__ == '__main__':
    all_lemmas = []
    for i in range(1, 11):
        text = read_text(f'news{i}.txt')
        words = clean_text(text)
        lemmas = lemmatize_words(words)
        lemmas = filter_stop_words(lemmas,STOP_WORDS)
        all_lemmas.extend(lemmas) 
    counter = count_words(all_lemmas)
    top20 = counter.most_common(20)
    print('20 самых частотных слов:')
    for word,count in top20:
        print(f'{word}:{count}')
    plot_top(top20)
    print('准备生成词云...')
    generate_wordcloud(counter, 'russian_wordcloud.png')