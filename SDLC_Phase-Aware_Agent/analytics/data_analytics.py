import matplotlib.pyplot as plt
from src.file_manager import DATA_DIR

def data_analysis(data):
    data = data.dropna(subset=["description"])
    description_counts = data["description"].value_counts()
    description_length= data["description"].str.len()
    description_avg = description_length.mean()
    print("\nDescription usage count:\n")
    print(description_counts)
    print("\n Description average length : \n",description_avg)

def data_plotting(data):
    description_counts = data["description"].value_counts()

    description_counts.plot(
        kind="bar",
        title="Description Frequency by Project",
        color="skyblue"
    )

    plt.xlabel("Description")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
   