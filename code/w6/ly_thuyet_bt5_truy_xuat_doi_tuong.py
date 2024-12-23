import pickle

# Deserialize đối tượng
with open('dl_tu_dien.pkl', 'rb') as file:
    loaded_data = pickle.load(file)
    print(loaded_data)