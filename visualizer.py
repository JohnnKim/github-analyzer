import matplotlib.pyplot as plt

def pie_chart(lang_data):
    labels = list(lang_data.keys())
    sizes = list(lang_data.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Language Distribution')
    plt.axis('equal')
    plt.show()