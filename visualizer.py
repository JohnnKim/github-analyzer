import matplotlib.pyplot as plt

def pie_chart(lang_data):
    # Extract the labels (language names) and their corresponding counts
    labels = list(lang_data.keys())
    sizes = list(lang_data.values())

    # Create a square figure for better visual proportions
    plt.figure(figsize=(8, 8))

    # Generate the pie chart with percentage labels
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Add a title to the chart
    plt.title('Language Distribution')

    # Equal aspect ratio ensures the pie is drawn as a circle
    plt.axis('equal')

    # Display the chart window
    plt.show()
