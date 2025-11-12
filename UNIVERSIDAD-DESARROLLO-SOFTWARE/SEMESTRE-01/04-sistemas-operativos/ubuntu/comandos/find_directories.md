find <directory> -name <file_name> / 
    *string* *.list

// por modificaciones recientes en este caso menor o igual a 7 dias.
find /var -mtime -7
-maxdepth 2 para acceder hata 2 subdirectorios
a-time fecha de acceso

helper
man <command>

grep <pattern> <file_name>
para busqueda recursiva r
grep -r <pattern> .
para minusculas y mayusculs i
grep -ir <pattern> .
para saber en que linea esta n
grep -inr <pattern> .

busca el numero especificado\
grep -r2 <pattern>
