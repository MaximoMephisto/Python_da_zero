def formatta_secondi(sec):
    minuti = sec // 60
    secondi = sec % 60 
    
    return f"{minuti}:{secondi}" 

# Caso base / minuto pieno
assert formatta_secondi(0)   == "0:0"      # ⚠️ atteso "0:00"
assert formatta_secondi(60)  == "1:0"      # ⚠️ atteso "1:00"
assert formatta_secondi(120) == "2:0"      # ⚠️ atteso "2:00"

# Sotto il minuto
assert formatta_secondi(5)   == "0:5"      # ⚠️ atteso "0:05"
assert formatta_secondi(9)   == "0:9"      # ⚠️ atteso "0:09"
assert formatta_secondi(10)  == "0:10"
assert formatta_secondi(59)  == "0:59"
# Secondi < 10 dopo il minuto (bug di padding più evidente)
assert formatta_secondi(61)  == "1:1"      # ⚠️ atteso "1:01"
assert formatta_secondi(65)  == "1:5"      # ⚠️ atteso "1:05"
assert formatta_secondi(69)  == "1:9"      # ⚠️ atteso "1:09"

# Secondi >= 10 (qui l'output è corretto per caso)
assert formatta_secondi(90)  == "1:30"
assert formatta_secondi(99)  == "1:39"
assert formatta_secondi(119) == "1:59"
assert formatta_secondi(999) == "16:39"

# Valori grandi (i minuti NON vengono convertiti in ore)
assert formatta_secondi(600)  == "10:0"    # ⚠️ atteso "10:00"
assert formatta_secondi(3600) == "60:0"    # ⚠️ 60 minuti, non "1:00:00"
assert formatta_secondi(3661) == "61:1"    # ⚠️ atteso "61:01" (o "1:01:01")

# Edge case Python: floor division con negativi
assert formatta_secondi(-1)  == "-1:59"    # -1//60 = -1, -1%60 = 59
assert formatta_secondi(-60) == "-1:0"
assert formatta_secondi(-61) == "-2:59"

# Edge case: input float (non sollevano errore, ma escono i decimali)
assert formatta_secondi(90.5) == "1.0:30.5"

print("Tutti i test passati ✅")