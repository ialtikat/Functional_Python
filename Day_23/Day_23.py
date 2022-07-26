"""
    Python dilindeki kümeler bu iş için pratik kullanım sağlar. 
    Kümeler dersindeki birleşim, kesişim, farkı işlemleri aşağıdaki gibidir.
"""

x = {"python", "java", "perl", "scala"}
y = {"ruby", "python", "java", "php"}

fark = x -y # x kumesinde olup, y'de omayanlar.
# {'perl', 'scala'}

birlesim = x | y # iki kümenin birleşimi
# {'perl', 'python', 'php', 'scala', 'ruby', 'java'}

kesisim = x & y # iki kümenin kesişimi
# {'python', 'java'}

simetrik_fark = x^y # Simetrik fark = birleşim - kesişim
# {'perl', 'php', 'scala', 'ruby'}

print(fark, birlesim, kesisim, simetrik_fark)