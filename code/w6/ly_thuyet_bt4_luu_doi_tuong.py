import pickle

# Tạo đối tượng từ điển
# Serialize đối tượng
data_vao = {'name': 'Sinh vien HUB 3', 'age': 30}
#data_vao2 = {'name': 'Sinh vien HUB 3', 'age': 30}
with open('dl_tu_dien.pkl', 'wb') as file:
    pickle.dump(data_vao, file)
    #pickle.dump(data_vao2, file)