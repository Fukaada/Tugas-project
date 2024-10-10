import numpy as np

# 1. np.array() -> Membuat array dari list atau tuple.
# Parameter: Iterable (seperti list, tuple)
data = np.array([1, 2, 3, 4])
print("Array data:", data)  
# Output: [1 2 3 4]

# 2. np.arange() -> Membuat array dengan rentang angka.
# Parameter: (start, stop, step) - start: mulai, stop: berhenti (exclusive), step: langkah.
data_nomor = np.arange(2, 21, 2)
print("Array dengan arange:", data_nomor)
# Output: [ 2  4  6  8 10 12 14 16 18 20]

# 3. np.zeros() -> Membuat array yang semua elemennya adalah 0.
# Parameter: shape - bentuk array (baris, kolom).
data_zeros = np.zeros((3, 3))
print("Array zeros:", data_zeros)
# Output: [[0. 0. 0.]
#          [0. 0. 0.]
#          [0. 0. 0.]]

# 4. np.ones() -> Membuat array yang semua elemennya adalah 1.
# Parameter: shape - bentuk array (baris, kolom).
data_ones = np.ones((2, 4))
print("Array ones:", data_ones)
# Output: [[1. 1. 1. 1.]
#          [1. 1. 1. 1.]]

# 5. np.random.rand() -> Membuat array dengan elemen acak antara 0 dan 1.
# Parameter: shape - bentuk array (baris, kolom).
data_random = np.random.rand(3, 2)
print("Array random:", data_random)
# Output: array acak 3x2

# 6. np.sum() -> Menjumlahkan semua elemen dalam array.
# Parameter: array - array yang akan dijumlahkan.
data = np.array([10, 20, 30, 40, 50])
hasil_sum = np.sum(data)
print("Jumlah elemen array:", hasil_sum)
# Output: 150

# 7. np.mean() -> Menghitung rata-rata elemen dalam array.
# Parameter: array - array yang akan dihitung rata-ratanya.
hasil_mean = np.mean(data)
print("Rata-rata elemen array:", hasil_mean)
# Output: 30.0

# 8. np.max() -> Mengambil nilai maksimum dalam array.
# Parameter: array - array yang akan dicari nilai maksimumnya.
nilai_maks = np.max(data)
print("Nilai maksimum:", nilai_maks)
# Output: 50

# 9. np.min() -> Mengambil nilai minimum dalam array.
# Parameter: array - array yang akan dicari nilai minimumnya.
nilai_min = np.min(data)
print("Nilai minimum:", nilai_min)
# Output: 10

# 10. np.transpose() -> Transpose array (baris menjadi kolom dan sebaliknya).
# Parameter: array - array yang akan di-transpose.
data_matrix = np.array([[1, 2, 3], [4, 5, 6]])
hasil_transpose = np.transpose(data_matrix)
print("Transpose array:", hasil_transpose)
# Output: [[1 4]
#          [2 5]
#          [3 6]]

# 11. np.append() -> Menambahkan elemen ke array.
# Parameter: (array, elemen yang akan ditambahkan)
data_awal = np.array([1, 2, 3])
data_ditambah = np.append(data_awal, 4)
print("Array setelah ditambah elemen:", data_ditambah)
# Output: [1 2 3 4]

# 12. np.dot() -> Menghitung dot product dua array.
# Parameter: array_a, array_b - dua array yang akan dihitung dot product-nya.
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
hasil_dot = np.dot(array_a, array_b)
print("Dot product array:", hasil_dot)
# Output: 32 (1*4 + 2*5 + 3*6)

# 13. np.multiply() -> Mengalikan elemen-elemen dua array secara elemen per elemen.
# Parameter: array_a, array_b - dua array yang akan dikalikan.
hasil_kali = np.multiply(array_a, array_b)
print("Perkalian elemen array:", hasil_kali)
# Output: [ 4 10 18]

# 14. np.char.add() -> Menambahkan string ke setiap elemen array string.
# Parameter: dua array atau string yang akan digabungkan.
produk = np.array(['Baju', 'Celana', 'Topi'])
tersedia_produk = np.char.add('Tersedia: ', produk)
print("Array string:", tersedia_produk)
# Output: ['Tersedia: Baju' 'Tersedia: Celana' 'Tersedia: Topi']

import numpy as np

# 1. np.reshape() -> Mengubah bentuk (dimensi) array.
# Parameter: newshape - tuple dengan dimensi baru.
array_awal = np.array([1, 2, 3, 4, 5, 6])
array_reshape = np.reshape(array_awal, (2, 3))
print("Reshape array:", array_reshape)
# Output: [[1 2 3]
#          [4 5 6]]

# 2. np.ravel() -> Mengubah array multidimensi menjadi array satu dimensi (flatten).
# Parameter: array - array multidimensi yang ingin diflatkan.
array_multidim = np.array([[1, 2], [3, 4]])
array_flat = np.ravel(array_multidim)
print("Array flatten:", array_flat)
# Output: [1 2 3 4]

# 3. np.hstack() -> Menggabungkan dua array secara horizontal (menambah kolom).
# Parameter: array1, array2 - dua array yang akan digabungkan.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array_hstack = np.hstack((array1, array2))
print("Array hstack:", array_hstack)
# Output: [1 2 3 4 5 6]

# 4. np.vstack() -> Menggabungkan dua array secara vertikal (menambah baris).
# Parameter: array1, array2 - dua array yang akan digabungkan.
array_vstack = np.vstack((array1, array2))
print("Array vstack:", array_vstack)
# Output: [[1 2 3]
#          [4 5 6]]

# 5. np.hsplit() -> Membagi array secara horizontal menjadi beberapa bagian.
# Parameter: array, jumlah bagian.
array_to_split = np.array([[1, 2, 3], [4, 5, 6]])
array_hsplit = np.hsplit(array_to_split, 3)
print("Array hsplit:", array_hsplit)
# Output: [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]

# 6. np.vsplit() -> Membagi array secara vertikal menjadi beberapa bagian.
# Parameter: array, jumlah bagian.
array_vsplit = np.vsplit(array_to_split, 2)
print("Array vsplit:", array_vsplit)
# Output: [array([[1, 2, 3]]), array([[4, 5, 6]])]

# 7. np.concatenate() -> Menggabungkan dua array di sepanjang axis tertentu.
# Parameter: (tuples of arrays, axis)
array_concatenate = np.concatenate((array1, array2), axis=0)
print("Array concatenate:", array_concatenate)
# Output: [1 2 3 4 5 6]

# 8. np.sqrt() -> Menghitung akar kuadrat dari setiap elemen array.
# Parameter: array - array yang akan dihitung akar kuadratnya.
array_sqrt = np.sqrt(np.array([1, 4, 9, 16]))
print("Array sqrt:", array_sqrt)
# Output: [1. 2. 3. 4.]

# 9. np.log() -> Menghitung logaritma natural dari setiap elemen array.
# Parameter: array - array yang akan dihitung logaritma naturalnya.
array_log = np.log(np.array([1, np.e, np.e**2]))
print("Array log:", array_log)
# Output: [0. 1. 2.]

# 10. np.exp() -> Menghitung eksponensial dari setiap elemen array.
# Parameter: array - array yang akan dihitung eksponensialnya.
array_exp = np.exp(np.array([0, 1, 2]))
print("Array exp:", array_exp)
# Output: [ 1.  2.71828183  7.3890561 ]

# 11. np.median() -> Menghitung median dari elemen-elemen dalam array.
# Parameter: array - array yang akan dihitung mediannya.
data_angka = np.array([1, 3, 3, 6, 7, 8, 9])
median_data = np.median(data_angka)
print("Median array:", median_data)
# Output: 6.0

# 12. np.cumsum() -> Menghitung jumlah kumulatif dari elemen-elemen array.
# Parameter: array - array yang akan dihitung jumlah kumulatifnya.
array_cumsum = np.cumsum(np.array([1, 2, 3, 4]))
print("Array cumsum:", array_cumsum)
# Output: [ 1  3  6 10]

# 13. np.diff() -> Menghitung perbedaan antara elemen-elemen bertetangga.
# Parameter: array - array yang akan dihitung perbedaannya.
array_diff = np.diff(np.array([1, 2, 4, 7, 0]))
print("Array diff:", array_diff)
# Output: [ 1  2  3 -7]

# 14. np.sort() -> Mengurutkan elemen-elemen array secara ascending.
# Parameter: array - array yang akan diurutkan.
array_unsorted = np.array([3, 1, 2, 5, 4])
array_sorted = np.sort(array_unsorted)
print("Array sorted:", array_sorted)
# Output: [1 2 3 4 5]

# 15. np.unique() -> Mengambil elemen unik dalam array dan mengembalikannya dalam array yang terurut.
# Parameter: array - array yang akan dicari elemen uniknya.
array_with_duplicates = np.array([1, 2, 2, 3, 4, 4, 5])
array_unique = np.unique(array_with_duplicates)
print("Array unique:", array_unique)
# Output: [1 2 3 4 5]

# 16. np.argmax() -> Mengembalikan indeks elemen maksimum dalam array.
# Parameter: array - array yang akan dicari indeks elemen maksimumnya.
array = np.array([1, 5, 2, 8, 3])
index_max = np.argmax(array)
print("Indeks elemen maksimum:", index_max)
# Output: 3

# 17. np.argmin() -> Mengembalikan indeks elemen minimum dalam array.
# Parameter: array - array yang akan dicari indeks elemen minimumnya.
index_min = np.argmin(array)
print("Indeks elemen minimum:", index_min)
# Output: 0

# 18. np.linspace() -> Membuat array dengan nilai yang diatur secara merata dalam interval tertentu.
# Parameter: start, stop, num (jumlah elemen yang ingin dihasilkan).
array_linspace = np.linspace(0, 10, 5)
print("Array linspace:", array_linspace)
# Output: [ 0.   2.5  5.   7.5 10. ]

# 19. np.meshgrid() -> Menghasilkan grid koordinat dari dua array 1D.
# Parameter: array1, array2 - dua array 1D yang akan dijadikan grid.
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print("Meshgrid X:", X)
print("Meshgrid Y:", Y)
# Output:
# Meshgrid X: [[1 2 3]
#              [1 2 3]]
# Meshgrid Y: [[4 4 4]
#              [5 5 5]]


